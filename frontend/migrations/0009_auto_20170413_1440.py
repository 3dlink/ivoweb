# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-13 14:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_auto_20170413_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteresesUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_interes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Intereses')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='03126915-f979-47d7-87dc-39964620bfbc', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='interesesusuario',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intereses', to=settings.AUTH_USER_MODEL),
        ),
    ]
