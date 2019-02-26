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

## Usage

### Settings

Here are the settings within django-easy-captcha, must add the following line in your django's settings.py file.

* DECAPTCHA_GENERATOR
    
        default : captcha.DefaultGenerator
        type    : string
        choices : captcha.DefaultGenerator, captcha.SimpleGenerator, captcha.SimpleChineseGenerator
        description : this is the image generator, you could choise above's and you also could
                      implements your own style image generator just follow the guide of 
                      [easy-captcha](https://github.com/youngershen/easy-captcha)
        
        

* DECAPTCHA_SIZE

        default: (100, 40)
        type   : tuple
        choises: as you wish the size of image.
        description: this paramters contorl the generated image size , you could set it as your desire.
        
* DECAPTCHA_TIMEOUT

        default: 10
        type   : integer
        choises: larger than 5
        descriptions: cause the challenge spawn and then store in the database , it has chance generated the
                      repeated challenge, so i set a timeout flag to control the gusses succeed rate.
                      
* DECAPTCHA_LENGTH

        default : 4
        type: integer
        chpises: larger than 4
        descriptions:          
        


* length = getattr(settings, 'DECAPTCHA_LENGTH', 4)
* challenge = getattr(settings, 'DECAPTCHA_CHALLENGE', 'decaptcha.challenges.random_char_challenge')
* url_prefix = getattr(settings, 'DECAPTCHA_URL_PREFIX', 'captcha')
* max_random_key = getattr(settings, DE'CAPTCHA_MAX_RANDOM_KEY', 18446744073709551616)  # 2 << 63


Bear Kid Homebrew Gaming Studio
熊孩子家酿游戏工作室