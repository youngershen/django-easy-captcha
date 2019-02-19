# PROJECT : django-easy-captcha
# TIME : 2018/11/25 10:15
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com
from django.test import TestCase
from decaptcha.models import CaptchaRecord
from decaptcha.utils import get_captcha


class DecaptchaTest(TestCase):
    def setUp(self):
        pass

    def test_model(self):
        challenge = CaptchaRecord.generate()
        self.assertTrue(challenge)

    def test_get_captcha(self):
        key, image = get_captcha()
        self.assertTrue(key)
        self.assertTrue(image)
