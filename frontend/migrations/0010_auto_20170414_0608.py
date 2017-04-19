# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-14 06:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_auto_20170413_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255, verbose_name='Sector Industria')),
            ],
        ),
        migrations.CreateModel(
            name='sectorIndustria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Industria')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='549b1678-d7cf-4c1b-9632-35a1c1e826b7', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='sectorindustria',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sectorindustria', to=settings.AUTH_USER_MODEL),
        ),
    ]
