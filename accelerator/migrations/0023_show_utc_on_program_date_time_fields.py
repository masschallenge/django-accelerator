# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-26 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0022_add_judginground_collision_detection_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='overview_deadline_date',
            field=models.DateTimeField(
                blank=True,
                help_text='Time is in UTC',
                null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='overview_start_date',
            field=models.DateTimeField(
                blank=True,
                help_text='Time is in UTC',
                null=True),
        ),
    ]
