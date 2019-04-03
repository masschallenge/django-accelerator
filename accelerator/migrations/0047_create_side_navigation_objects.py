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
)


def create_subnav_trees_and_items(apps, schema_editor):
    create_directory_subnav()
    create_events_subnav()
    create_home_subnav()
    create_judging_subnav()
    create_resources_subnav()
    create_startup_dashboard_subnav()


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0046_add_items_to_side_nav_tree'
        ),
    ]

    operations = [
        migrations.RunPython(create_subnav_trees_and_items),
    ]
