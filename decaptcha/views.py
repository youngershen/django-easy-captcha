# PROJECT : django-easy-captcha
# TIME : 2018/11/25 10:16
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from django.urls import reverse
from django.http import Http404
from django.views.generic import View
from django.http.response import JsonResponse, FileResponse
from decaptcha.models import CaptchaRecord


class New(View):
    http_method_names = ['get']

    def get(self, request):
        k, _ = self.captcha()
        url = self.get_url(k)
        json = {
            'key': k,
            'url': url
        }
        return JsonResponse(data=json)

    @staticmethod
    def captcha():
        k, i = CaptchaRecord.get_captcha()
        return k, i

    @staticmethod
    def get_url(key):
        url = reverse('captcha:image', args=(key, ))
        return url


class Image(View):
    def get(self, request, key):
        i = self.get_image(key)
        return FileResponse(i)

    @staticmethod
    def get_image(key):
        try:
            record = CaptchaRecord.objects.get(hashkey=key)
        except CaptchaRecord.DoesNotExist:
            raise Http404()
        else:
            return record.get_image()


class Match(View):
    def get(self, request, key):
        pass

    def get_image(self, key):
        pass


new = New.as_view()
image = Image.as_view()
match = Match.as_view()
