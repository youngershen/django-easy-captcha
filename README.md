# Django Easy Captcha

![Travis](https://img.shields.io/travis/youngershen/django-easy-captcha.svg)
![codecov](https://codecov.io/gh/youngershen/django-easy-captcha/branch/master/graph/badge.svg)
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

3. add **path('captcha/', include('decaptcha.urls'))** to your urls.py

4. run **python manage.py migrate** to sync the database.

### Management Commands

* **decpatcha_purge** 

        python manage.py decaptcha_purge
        
        this command has no parameter, and it is just for deleting the expired captcha records in database.
        

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

* /captcha/new
    
        method: POST
        parameters: None
        response: JSON
        sample  : {'key': k, 'url': url}
        description: this method generated the key and captcha image url to json response, 
                     could useful in ajax situlation.
                      
* /captcha/image

        method: GET
        parameters: /captcha/image/892d9c60e0347bc3eb7d7028f4c3c1eef6181af3
        response: image/png
        description: this method get image from server, you should user
                     the hashkey you got in **new** method as parameters.
                     
* /captcha/match
        
        method: POST
        parameters : 
            challenge : string, not null. 
            hashkey   : string, not null.

        responsse: JSON
        description: this method for validate the user input challenge,
                     **challenge** is the user input code, 
                     **hashkey** is the hashkey you got when generate the captcha.
        
* /captcha/get
    
        method: GET
        parameters : None
        response: image/png
        description: this method direct get the image captcha 
                     the hashkey save to the cookies, but you
                     do not need care about the hashkey, for 
                     detail just read the source code.


## Advance Topics

### Custom Challenge Generator

to make a custom challenge generator is very easy, just check the code in decaptcha/challenge.py, subclass the Base
class then simplement the class method **get**, this method just return the string you want.

when you custom your own challenge generator, you also should change the **DECAPTCHA_CHALLENGE** in settings.py

### Custom Captcha image Generator

if you want to make your own captcha image generator, you should read the docs [here](https://github.com/youngershen/easy-captcha#custom-captcha-generator), and follow
the guide.