# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-09 01:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0004_auto_20170608_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casting',
            name='genero',
        ),
    ]
