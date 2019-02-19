# PROJECT : django-easy-captcha
# TIME : 2018/11/18 11:01
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

import time
import hashlib
import datetime
from importlib import import_module
from random import randrange
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_text
from decaptcha.settings import timeout, max_random_key, challenge


class CaptchaRecord(models.Model):
    challenge = models.CharField(max_length=255, verbose_name=_('Chanllenge'))
    hashkey = models.CharField(max_length=255, verbose_name=_('Hashkey'))
    timeout = models.DateTimeField(auto_now_add=True, verbose_name=_('Timeout'))

    @classmethod
    def generate(cls):
        challenge_ = cls._get_challenge()
        timeout_ = timezone.now() + datetime.timedelta(minutes=int(timeout))
        key_ = (
                smart_text(randrange(0, max_random_key)) +
                smart_text(time.time()) +
                smart_text(challenge, errors='ignore')
            ).encode('utf8')
        hashkey_ = hashlib.sha1(key_).hexdigest()
        del key_
        cls.objects.create(challenge=challenge_, hashkey=hashkey_, timeout=timeout_)
        return challenge_, hashkey_

    @staticmethod
    def _get_challenge():
        func = load_string(challenge)
        return func()


def load_string(module_str):
    m = module_str.split('.')
    module = import_module('.'.join(m[:-1]))
    ret = getattr(module, m[-1])
    return ret
