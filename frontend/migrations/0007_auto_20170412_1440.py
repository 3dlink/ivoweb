# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-12 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='busto',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cadera',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cintura',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='estatura',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tipo_usuario',
            field=models.CharField(choices=[('I', 'INDUSTRIA'), ('A', 'ARTISTAS'), ('F', 'FANS'), ('P', 'PROVEEDOR')], db_column='Tipousuario', default='A', max_length=1, verbose_name='Tipo de usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='561d8f28-9414-46c0-84a3-14ec050eeb58', max_length=100, unique=True),
        ),
    ]