# PROJECT : django-easy-captcha
# TIME : 2018/11/25 10:24
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from django.conf import settings

generator = getattr(settings, 'DECAPTCHA_GENERATOR', 'captcha.DefaultGenerator')
cookie_name = getattr(settings, 'DECAPTCHA_COOKIE_NAME', 'decaptcha')
size = getattr(settings, 'DECAPTCHA_SIZE', (100, 40))
timeout = getattr(settings, 'DECAPTCHA_TIMEOUT', 10)  # minutes
length = getattr(settings, 'DECAPTCHA_LENGTH', 4)
challenge = getattr(settings, 'DECAPTCHA_CHALLENGE', 'decaptcha.challenges.RandomSimpleChars')
url_prefix = getattr(settings, 'DECAPTCHA_URL_PREFIX', 'decaptcha')
max_random_key = getattr(settings, 'DECAPTCHA_MAX_RANDOM_KEY', 18446744073709551616)  # 2 << 63

