# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-19 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0037_auto_20170714_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=200)),
                ('respuesta', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='c1c87ce9-b302-4098-b248-993d329be28e', max_length=100, unique=True),
        ),
    ]
