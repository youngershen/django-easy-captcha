# PROJECT : django-easy-captcha
# TIME : 19-3-4 上午10:53
# AUTHOR : Younger Shen
# EMAIL : younger.x.shen@gmail.com
# CELL : 13811754531
# WECHAT : 13811754531
# WEB : https://youngershen.com

from django.utils.translation import ugettext as _
from django.core.management.base import BaseCommand
from decaptcha.models import CaptchaRecord as Record


class Command(BaseCommand):
    help = 'Delete all expired captch records'

    def handle(self, *args, **options):
        Record.delete_expired_records()
        self.stdout.write(self.style.SUCCESS(_('Successfully delete expires records.')))
