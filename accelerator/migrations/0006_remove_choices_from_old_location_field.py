# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-10-07 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator',
         '0005_migrate_old_location_data_to_new_location_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprogramofficehour',
            name='old_location',
            field=models.CharField(max_length=50),
        ),
    ]
