# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-19 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0041_make_user_role_field_many_to_many'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judginground',
            name='end_date_time',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='judginground',
            name='start_date_time',
            field=models.DateTimeField(default=None),
        ),
    ]
