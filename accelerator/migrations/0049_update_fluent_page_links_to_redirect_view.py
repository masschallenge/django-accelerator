# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from accelerator.sitetree_navigation.sub_navigation import (
    create_events_subnav,
    create_home_subnav,
    create_resources_subnav,
)


def update_subnav_trees_and_items(apps, schema_editor):
    create_events_subnav()
    create_home_subnav()
    create_resources_subnav()


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0048_create_fluent_page_association_with_subnav'
        ),
    ]

    operations = [
        migrations.RunPython(update_subnav_trees_and_items),
    ]
