# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-24 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0022_auto_20170519_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cita',
            field=models.TextField(blank=True, db_column='Cita', null=True, verbose_name='Cita'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='a01d39b9-5826-457b-9203-b1ebd0814c5b', max_length=100, unique=True),
        ),
    ]
