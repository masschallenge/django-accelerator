# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-03 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0025_reorder_gender_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='acknowledgement',
            field=models.BooleanField(
                default=False,
                help_text=('I understand that my Startup Profile '
                           'is a pre-requisite for applying to '
                           'any MassChallenge Program')),
        ),
    ]
