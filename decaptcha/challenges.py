# PROJECT : django-easy-captcha
# TIME : 2018/11/25 15:56
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531

import random
from decaptcha import settings


def random_char_challenge():
    chars, ret = 'abcdefghijklmnopqrstuvwxyz', ''
    for i in range(settings.length):
        ret += random.choice(chars)
    return ret

