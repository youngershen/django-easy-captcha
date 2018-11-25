# PROJECT : django-easy-captcha
# TIME : 2018/11/25 10:24
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from django.conf import settings

generator = getattr(settings, 'CAPTCHA_GENERATOR', 'captcha.generator.simple_generator')
size = getattr(settings, 'CAPTCHA_SIZE', (100, 40))
timeout = getattr(settings, 'CAPTCHA_TIMEOUT', 30)  # minutes
length = getattr(settings, 'CAPTCHA_LENGTH', 4)
challenge = getattr(settings, 'CAPTCHA_CHALLENGE', 'decaptcha.challenges.random_char_challenge')
max_random_key = getattr(settings, 'CAPTCHA_MAX_RANDOM_KEY', 18446744073709551616)  # 2 << 63

