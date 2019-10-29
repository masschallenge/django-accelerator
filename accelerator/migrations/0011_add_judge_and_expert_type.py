# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-10-29 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0010_make_old_location_field_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertprofile',
            name='judge_type',
            field=models.CharField(blank=True, help_text='Allowed Values: 1 - Round 1 Judge, 2 - Round 2 Judge, 3 - Pre-final Judge, 4 - Final Judge, 0 - Once Accepted, now rejected, X - Not Accepted as a Judge (May still be a mentor)', max_length=64, verbose_name='Judge Type'),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='mentor_type',
            field=models.CharField(blank=True, help_text='Allowed Values: F - Functional Expert, P - Partner, T - Technical, E - Entrepreneur, N - Once accepted, now rejected, X - Not Accepted as a Mentor (may still be a judge)', max_length=64, verbose_name='Mentor Type'),
        ),
    ]
