# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-03 10:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('casting', '0003_auto_20170323_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_participar', models.TextField()),
                ('cuentanos', models.TextField()),
                ('archivo', models.FileField(blank=True, upload_to='audiciones')),
            ],
        ),
        migrations.AlterField(
            model_name='casting',
            name='imagen_principal',
            field=models.ImageField(blank=True, upload_to='casting'),
        ),
        migrations.AddField(
            model_name='audicion',
            name='id_casting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casting.Casting'),
        ),
        migrations.AddField(
            model_name='audicion',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
