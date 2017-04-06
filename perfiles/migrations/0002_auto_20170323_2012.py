# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-23 20:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educacion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiencia', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='multimedia', to=settings.AUTH_USER_MODEL),
        ),
    ]