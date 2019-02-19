# Generated by Django 2.1.3 on 2018-11-25 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaptchaRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge', models.CharField(max_length=255, verbose_name='Chanllenge')),
                ('hashkey', models.CharField(max_length=255, verbose_name='Hashkeys')),
                ('timeout', models.DateTimeField(auto_now_add=True, verbose_name='Timeout')),
            ],
        ),
    ]