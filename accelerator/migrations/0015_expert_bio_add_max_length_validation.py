# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-25 15:00
from __future__ import unicode_literals

import django.core.validators
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0013_allocator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertprofile',
            name='bio',
            field=models.TextField(blank=True, default='', validators=[
                django.core.validators.MaxLengthValidator(7500)]),
        ),
    ]
