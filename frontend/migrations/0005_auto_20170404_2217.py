# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-04 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20170404_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='2c6ad818-06d2-48ad-87e9-7d1b20b42f04', max_length=100, unique=True),
        ),
    ]
