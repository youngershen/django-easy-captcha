# PROJECT : django-easy-captcha
# TIME : 2018/11/25 10:16
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from django.views.generic import View
from django.http.response import JsonResponse
from captcha.models import CaptchaRecord


class Captcha(View):
    http_method_names = ['get']

    def get(self):
        k, i = self.captcha()
        json = {
            'k': k
        }
        return JsonResponse(data=json)

    @staticmethod
    def captcha():
        k, i = CaptchaRecord.get_captcha()
        return k, i


captcha = Captcha.as_view()
