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
from random import randrange
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_text
from decaptcha.settings import timeout, max_random_key, challenge
from decaptcha.utils import load_string, get_generator
from decaptcha.settings import size


class CaptchaRecord(models.Model):
    challenge = models.CharField(max_length=255, verbose_name=_('Chanllenge'))
    hashkey = models.CharField(max_length=255, verbose_name=_('Hashkey'))
    timeout = models.DateTimeField(blank=True, null=True, verbose_name=_('Timeout'))

    @classmethod
    def match(cls, c, k):
        now = timezone.now()
        records = cls.objects.filter(challenge=c, hashkey=k, timeout__gte=now)
        return records.exists()

    @classmethod
    def get_expired_records(cls):
        now = timezone.now()
        records = cls.objects.filter(timeout__lte=now)
        return records

    @classmethod
    def delete_expired_records(cls):
        records = cls.get_expired_records()
        if records:
            records.delete()

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

    @classmethod
    def get_captcha(cls):
        c, k = cls.generate()
        return c, k

    @staticmethod
    def _get_challenge():
        clazz = load_string(challenge)
        return clazz.get()

    def get_image(self):
        generator_ = get_generator()
        i = generator_.make_captcha(self.challenge.upper(), image_size=size)
        from io import BytesIO
        f = BytesIO()
        i.save(f, format='png')
        f.seek(0)
        return f

