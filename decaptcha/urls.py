# PROJECT : django-easy-captcha
# TIME : 2018/11/25 10:16
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from django.urls import path
from decaptcha.views import new, image, match, get


urlpatterns = [
    path('new', new, name='new'),
    path('image/<key>', image, name='image'),
    path('match', match, name='match'),
    path('get', get, name='get')
]

app_name = 'decaptcha'
