# PROJECT : django-easy-captcha
# TIME : 2018/11/25 16:47
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
from decaptcha.models import CaptchaRecord, load_string
from decaptcha.settings import generator, size


def get_generator():
    generator_ = load_string(generator)
    return generator_()


def get_captcha():
    challenge, key = CaptchaRecord.generate()
    generator_ = get_generator()
    image = generator_.make_captcha(challenge, image_size=size)
    return key, image

