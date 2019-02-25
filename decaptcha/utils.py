# PROJECT : django-easy-captcha
# TIME : 2018/11/25 16:47
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from importlib import import_module

from decaptcha.settings import generator


def get_generator():
    generator_ = load_string(generator)
    return generator_()


def load_string(module_str):
    m = module_str.split('.')
    module = import_module('.'.join(m[:-1]))
    ret = getattr(module, m[-1])
    return ret
