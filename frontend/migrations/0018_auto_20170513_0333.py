# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-13 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0017_auto_20170512_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pais',
            name='bandera',
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='ca0ddb78-58a4-43fb-8248-49af6e0fbe1b', max_length=100, unique=True),
        ),
    ]