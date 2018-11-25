# PROJECT : django-easy-captcha
# TIME : 2018/11/18 11:01
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
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
    hashkey = models.CharField(max_length=255, verbose_name=_('Hashkeys'))
    timeout = models.DateTimeField(auto_now_add=True, verbose_name=_('Timeout'))

    def generate(self):
        self.challenge = self._get_challenge()
        self.timeout = timezone.now() + datetime.timedelta(minutes=int(timeout))
        key_ = (
                smart_text(randrange(0, max_random_key)) +
                smart_text(time.time()) +
                smart_text(self.challenge, errors='ignore')
            ).encode('utf8')
        self.hashkey = hashlib.sha1(key_).hexdigest()
        del key_
        self.save()

    def _get_challenge(self):
        func = import_module(challenge)
        return func()