# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-04 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0003_mensaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='imagen_1',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='mensajes'),
        ),
    ]
