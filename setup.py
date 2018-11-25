# PROJECT : kungfucms
# TIME : 2018/11/25 10:05
# AUTHOR : Younger Shen
# EMAIL : youngershen64@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531

from setuptools import setup, find_packages

setup(
    name='django-easy-captcha',

    version='0.1',

    description='a very easy to use captcha image generator for django.',

    url='https://github.com/youngershen/django-easy-captcha',

    # Author details
    author='Younger Shen',
    author_email='youngershen64@hotmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 1 - Planning',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django'
    ],

    # What does your project relate to?
    keywords='django, captcha, image',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    install_requires=[
        'easy-captcha',
        'django'
    ],

    python_requires='>=3.6',
)
