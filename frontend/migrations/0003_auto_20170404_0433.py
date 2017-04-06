# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-04 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20170403_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='portada',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='portada'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='16c8bd26-a86d-4054-883e-6c6e1d908042', max_length=100, unique=True),
        ),
    ]