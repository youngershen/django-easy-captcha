# PROJECT : django-easy-captcha
# TIME : 2018/11/25 10:16
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext as _
from django.urls import reverse
from django.http import Http404
from django.views.generic import View
from django.http.response import JsonResponse, HttpResponse
from decaptcha.models import CaptchaRecord
from decaptcha.validators import Captcha as CaptchaValidator
from decaptcha.settings import url_prefix, cookie_name


class New(View):
    http_method_names = ['post']

    def post(self, request):
        data = self.captcha()
        return JsonResponse(data=data)

    def captcha(self):
        _, k = CaptchaRecord.get_captcha()
        url = self.get_url(k)
        return {'key': k, 'url': url}

    @staticmethod
    def get_url(key):
        url = reverse('{PREFIX}:image'.format(PREFIX=url_prefix), args=(key, ))
        return url


class Image(View):
    http_method_names = ['get']

    def get(self, request, key):
        return self.response(key)

    def response(self, key, size=None):
        i = self.get_image(key, size)
        response = HttpResponse(content_type='image/png')
        response.write(i.read())
        response['Content-length'] = i.tell()
        return response

    @staticmethod
    def get_image(key, size=None):
        try:
            record = CaptchaRecord.objects.get(hashkey=key)
        except CaptchaRecord.DoesNotExist:
            raise Http404()
        else:
            return record.get_image(size)


class Match(View):
    http_method_names = ['post']

    def post(self, request):
        status = self.match(request)

        if status:
            data = {
                'status': 0,
            }
        else:
            data = {
                'status': 1,
                'message': _('input code mismatch the challenge')
            }

        return JsonResponse(data=data)

    def match(self, request):
        validator = CaptchaValidator(self.data(request))
        validator.validate()
        if validator.status:
            c = validator.get('challenge')
            k = validator.get('hashkey')
            return CaptchaRecord.match(c, k)
        else:
            return False

    @staticmethod
    def data(request):
        challenge = request.POST.get('challenge', None)
        hashkey = request.POST.get('hashkey', None)

        if not hashkey:
            hashkey = request.COOKIES[cookie_name]

        return {
            'challenge': challenge,
            'hashkey': hashkey
        }


class Get(New, Image):
    http_method_names = ['get']

    def get(self, request, key=None):
        data = self.captcha()
        response = self.response(key=data['key'], size=self.get_size())
        response.set_cookie(key=cookie_name, value=data['key'])
        return response

    def get_size(self):
        width = self.request.GET.get('width')
        height = self.request.GET.get('height')

        if width and height:
            try:
                width = int(width)
                height = int(height)
            except ValueError:
                size = None
            else:
                size = (width, height)
        else:
            size = None

        return size


new = csrf_exempt(New.as_view())
match = csrf_exempt(Match.as_view())
image = Image.as_view()
get = Get.as_view()

