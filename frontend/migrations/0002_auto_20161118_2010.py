# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-18 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='aa0adc5a-3cf0-4ee2-a4f5-9c74a859408c', max_length=100, unique=True),
        ),
    ]
