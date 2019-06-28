# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-26 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator',
            '0058_grant_staff_clearance_for_existing_staff_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrepreneurprofile',
            name='recommendation_tags',
        ),
        migrations.RemoveField(
            model_name='expertprofile',
            name='recommendation_tags',
        ),
        migrations.RemoveField(
            model_name='memberprofile',
            name='recommendation_tags',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='recommendation_tags',
        ),
        migrations.RemoveField(
            model_name='startupteammember',
            name='recommendation_tags',
        ),
        migrations.DeleteModel(
            name='RecommendationTag',
        ),
    ]