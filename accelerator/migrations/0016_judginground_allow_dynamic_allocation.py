# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-14 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0015_expert_bio_add_max_length_validation'),
    ]

    operations = [
        migrations.AddField(
            model_name='judginground',
            name='allow_dynamic_allocation',
            field=models.BooleanField(default=False),
        ),
    ]