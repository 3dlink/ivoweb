# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-12 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casting', '0005_audicion_ganador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audicion',
            name='archivo',
            field=models.FileField(upload_to='audiciones'),
        ),
    ]
