# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficios', '0002_mapa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='priorizar',
            old_name='porcentaje',
            new_name='valor',
        ),
    ]
