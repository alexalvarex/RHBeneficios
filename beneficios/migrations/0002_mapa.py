# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-20 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beneficios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comunidadFinal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Final', to='beneficios.Comunidad')),
                ('comunidadInicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Inicio', to='beneficios.Comunidad')),
            ],
        ),
    ]
