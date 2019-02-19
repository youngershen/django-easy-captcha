# PROJECT : django-easy-captcha
# TIME : 2018/11/25 10:16
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from django.urls import path
from captcha.views import captcha


urlpatterns = [
    path('captcha', captcha, name='captcha'),
]

