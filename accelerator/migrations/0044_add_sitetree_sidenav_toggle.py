# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-03-20 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0043_remove_exclude_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programfamily',
            name='side_navigation',
        ),
        migrations.AddField(
            model_name='programfamily',
            name='use_site_tree_side_nav',
            field=models.BooleanField(default=False, help_text='Show the new-style side navigation'),
        ),
    ]
