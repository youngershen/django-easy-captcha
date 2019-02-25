# Django Easy Captcha

![Travis](https://img.shields.io/travis/youngershen/django-easy-captcha.svg)
![codecov](https://codecov.io/gh/youngershen/django-easy-captcha/branch/develop/graph/badge.svg)
![PyPI - License](https://img.shields.io/pypi/l/django-easy-captcha.svg)
![PyPI](https://img.shields.io/pypi/v/django-easy-captcha.svg)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/django-easy-captcha.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-easy-captcha.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/youngershen/django-easy-captcha.svg)

## About

django-easy-captcha is a simple django app to provide captcha services. 
it is inspired by [django-simple-captcha](https://github.com/mbi/django-simple-captcha), 
and extends the [easy-captcha](https://github.com/youngershen/easy-captcha) to django.

the reason for recreate another wheel is that the  [django-simple-captcha](https://github.com/mbi/django-simple-captcha)
's image generator bind too tight to django, so i make a alternative package to separate the generator program and
django program.

it is another choise for developers(mostly you maybe make your own library) or just fine for me.

## Settings

Here are the settings within django-easy-captcha, must add the following line in your django's settings.py file.

* DECAPTCHA_GENERATOR
    
        default : captcha.DefaultGenerator
        type    : string
        choices : captcha.DefaultGenerator, captcha.SimpleGenerator, captcha.SimpleChineseGenerator
        description : 
        
        

* size = getattr(settings, 'CAPTCHA_SIZE', (100, 40))
* timeout = getattr(settings, 'CAPTCHA_TIMEOUT', 10)  # minutes
* length = getattr(settings, 'CAPTCHA_LENGTH', 4)
* challenge = getattr(settings, 'CAPTCHA_CHALLENGE', 'decaptcha.challenges.random_char_challenge')
* url_prefix = getattr(settings, 'CAPTCHA_URL_PREFIX', 'captcha')
* max_random_key = getattr(settings, 'CAPTCHA_MAX_RANDOM_KEY', 18446744073709551616)  # 2 << 63