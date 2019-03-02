# PROJECT : django-easy-captcha
# TIME : 2018/11/25 10:15
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from django.urls import reverse
from django.test import TestCase
from decaptcha.settings import url_prefix, cookie_name
from decaptcha.models import CaptchaRecord


class DecaptchaTest(TestCase):
    def setUp(self):
        self.url_new = reverse('{PREFIX}:new'.format(PREFIX=url_prefix))
        self.url_match = reverse('{PREFIX}:match'.format(PREFIX=url_prefix))
        self.url_get = reverse('{PREFIX}:get'.format(PREFIX=url_prefix))

    def test_model(self):
        challenge = CaptchaRecord.generate()
        self.assertTrue(challenge)

    def test_get_captcha(self):
        challenge, hashkey = CaptchaRecord.get_captcha()
        record = CaptchaRecord.objects.filter(challenge=challenge, hashkey=hashkey)
        self.assertTrue(record.exists())

    def test_url_new(self):
        response = self.client.post(self.url_new)
        self.assertTrue(response)

        data = response.json()
        url = data['url']
        key = data['key']

        self.assertTrue(url)
        self.assertTrue(key)

        record = CaptchaRecord.objects.get(hashkey=key)
        self.assertTrue(record)

        image = self.client.get(url)
        self.assertEqual(image.status_code, 200)

    def test_url_match(self):
        challenge, hashkey = CaptchaRecord.get_captcha()
        response = self.client.post(self.url_match, data={
            'challenge': challenge,
            'hashkey': hashkey
        })

        self.assertEqual(response.json()['status'], 0)

        response = self.client.post(self.url_match, data={
            'challenge': challenge,
            'hashkey': 'foo'
        })

        self.assertEqual(response.json()['status'], 1)

    def test_url_get(self):
        response = self.client.get(self.url_get)
        k1 = response.cookies[cookie_name]
        k2 = CaptchaRecord.objects.all().order_by('-id')[0].hashkey
        self.assertEqual(k1.value, k2)

