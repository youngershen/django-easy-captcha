# Generated by Django 2.1.3 on 2019-02-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decaptcha', '0002_auto_20181125_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captcharecord',
            name='timeout',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Timeout'),
        ),
    ]