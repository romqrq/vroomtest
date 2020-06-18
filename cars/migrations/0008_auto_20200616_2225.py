# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-16 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20200616_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_class',
            field=models.CharField(choices=[('Custom Classic', 'Custom Classic'), ('Luxury', 'Luxury'), ('Supersport', 'Supersport')], max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.CharField(choices=[('Dublin', 'Dublin'), ('Cork', 'Cork'), ('Galway', 'Galway')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='country',
            field=models.CharField(choices=[('Ireland', 'Ireland')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='county',
            field=models.CharField(choices=[('Dublin', 'Dublin'), ('Cork', 'Cork'), ('Galway', 'Galway')], max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Full Electric', 'Full Electric'), ('Hybrid', 'Hybrid'), ('Petrol', 'Petrol')], max_length=40),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=10),
        ),
    ]