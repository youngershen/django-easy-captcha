# PROJECT : django-easy-captcha
# TIME : 19-2-20 下午3:45
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from validator import Validator


class Captcha(Validator):
    challenge = 'required'
    hashkey = 'required'

