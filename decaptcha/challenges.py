# PROJECT : django-easy-captcha
# TIME : 2018/11/25 15:56
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

import random
from functools import reduce
from decaptcha import settings


class Base:
    name = 'base'
    length = settings.length

    @classmethod
    def get(cls):
        raise NotImplemented


class RandomSimpleChars(Base):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

    @classmethod
    def get(cls):
        ret = reduce(lambda x, y: x+y,
                     [str(random.choice(cls.chars)) for _ in range(cls.length)])
        return ''.join(ret).strip()


class RandomChars(RandomSimpleChars):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789' \
            '<>?}{+-*/!@#$%^&()_='
