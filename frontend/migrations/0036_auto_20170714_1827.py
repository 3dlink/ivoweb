# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-14 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0035_auto_20170703_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/static/img/avatar-ivo.jpg', max_length=200, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='ed8fb254-18c9-4069-ac94-4a997cc05724', max_length=100, unique=True),
        ),
    ]
