# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0004_update_organization_url_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup',
            name='additional_industry_categories',
        ),
        migrations.AddField(
            model_name='startup',
            name='additional_industries',
            field=models.ManyToManyField(blank=True, db_table='accelerator_startup_related_industry', help_text='You may select up to 5 related industries.', related_name='secondary_startups', to='accelerator.Industry', verbose_name='Additional Industries'),
        ),
    ]
