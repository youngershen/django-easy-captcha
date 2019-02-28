# PROJECT : django-easy-captcha
# TIME : 2018/11/25 15:56
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

import random
from decaptcha import settings


class Base:
    name = 'base'

    def __index__(self):
        self.length = settings.length

    def get(self):
        raise NotImplemented


class RandomSimpleChars(Base):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

    def get(self):
        ret = []
        for i in range(self.length):
            ret.append(random.choices(self.chars))

        return ''.join(ret).strip()


class RandomChars(RandomSimpleChars):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789' \
            '<>?}{+-*/!@#$%^&()_='
