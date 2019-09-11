# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-15 13:27
from __future__ import unicode_literals

from django.db import migrations
from accelerator.sitetree_navigation.sub_navigation import (
    create_startup_dashboard_subnav,
)


def update_startup_profile_item(apps, schema_editor):
    NavTreeItem = apps.get_model('accelerator', 'NavTreeItem')
    NavTreeItem.objects.filter(
        alias="startup_profile").delete()
    create_startup_dashboard_subnav()


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0074_update_social_and_website_field_labels'),
    ]

    operations = [
        migrations.RunPython(
            update_startup_profile_item,
            migrations.RunPython.noop)
    ]