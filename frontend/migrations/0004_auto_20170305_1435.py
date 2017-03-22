# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-05 14:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20170228_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioArteGenero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdOn', models.DateTimeField(auto_now_add=True, verbose_name='created On')),
                ('modifiedOn', models.DateTimeField(auto_now=True, verbose_name='modified On')),
                ('id_genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.GeneroArtistico')),
            ],
            options={
                'verbose_name': 'RelacionGeneroARTE',
                'verbose_name_plural': 'RelacionGenerosARTES',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(default='6023cb57-dc0d-46ee-954e-fa51a1ff10e7', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='usuarioartegenero',
            name='id_usuario',
            field=models.ForeignKey(db_column='Idusuario', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]