# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-09-04 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0077_add_program_overview_link_field_to_a_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='street_address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
