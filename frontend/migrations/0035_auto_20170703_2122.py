# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-03 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0034_auto_20170614_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='2a51a8d0-9862-435a-a94a-edf7200a569f', max_length=100, unique=True),
        ),
    ]
