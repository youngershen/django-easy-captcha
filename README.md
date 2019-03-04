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

### Install

1. run **pip install django-easy-captcha** or download the source code and run **python setup.py install**

2. append the **decaptcha** to **INSTALLED_APPS**.

3. run **python manage.py migrate** to sync the database.

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
        choises: bigger than 5
        descriptions: cause the challenge spawn and then store in the database , it has chance generated the
                      repeated challenge, so i set a timeout flag to control the gusses succeed rate.
                      
* DECAPTCHA_LENGTH

        default: 4
        type   : integer
        choices: bigger than 4
        descriptions: the length of the captcha challenge length, better bigger than 4.          
        
* DECAPTCHA_CHALLENGE

        default: decaptcha.challenges.RandomSimpleChars
        type   : string
        choices: decaptcha.challenges.RandomSimpleChars, decaptcha.challenges.RandomChars
        descriptions: the challenge generator defines how the systemd get challenge code,
                      the package provide 2 kind of generator, and you could custom your 
                      own generator too, just follow [this](#)
                     

* DECAPTCHA_COOKIE_NAME
    
        default: decaptcha
        type   : string
        choices: any string
        description: this string defines the cookie name of captcha hashkey, in match
        method you can put the hashkey in get parameter or get it from cookie

 
### URLs

## Advance Topics

### Custom Challenge Generator

### Cusom Captcha Generator

