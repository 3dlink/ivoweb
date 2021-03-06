# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-02 17:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0006_usuarioidioma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_destino', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_origen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multimedia', to=settings.AUTH_USER_MODEL),
        ),
    ]
