# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-14 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0033_auto_20170609_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='a3b6178e-22b5-4654-9aae-85436c699a2a', max_length=100, unique=True),
        ),
    ]
