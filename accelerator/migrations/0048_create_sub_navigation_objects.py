# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from accelerator.sitetree_navigation.sub_navigation import (
    create_directory_subnav,
    create_events_subnav,
    create_home_subnav,
    create_judging_subnav,
    create_resources_subnav,
    create_startup_dashboard_subnav,
    delete_directory_subnav,
    delete_events_subnav,
    delete_home_subnav,
    delete_judging_subnav,
    delete_resources_subnav,
    delete_startup_dashboard_subnav
)


def create_subnav_trees_and_items(apps, schema_editor):
    create_directory_subnav()
    create_events_subnav()
    create_home_subnav()
    create_judging_subnav()
    create_resources_subnav()
    create_startup_dashboard_subnav()


def delete_subnav_trees_and_items(apps, schema_editor):
    delete_directory_subnav()
    delete_events_subnav()
    delete_home_subnav()
    delete_judging_subnav()
    delete_resources_subnav()
    delete_startup_dashboard_subnav()


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0047_create_fluent_page_association_with_subnav'
        ),
    ]

    operations = [
        migrations.RunPython(
            create_subnav_trees_and_items,
            delete_subnav_trees_and_items),
    ]