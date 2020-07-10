# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-10 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_track_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='county',
            field=models.CharField(choices=[('Dublin', 'Dublin'), ('Cork', 'Cork'), ('Galway', 'Galway')], default='', max_length=30),
        ),
    ]
