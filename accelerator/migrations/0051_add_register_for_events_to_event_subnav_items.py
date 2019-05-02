# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from accelerator.sitetree_navigation.sub_navigation import (
    create_events_subnav,
)


def create_subnav_trees_and_items(apps, schema_editor):
    create_events_subnav()


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0050_update_fluent_redirect_url'
        ),
    ]

    operations = [
        migrations.RunPython(
            create_subnav_trees_and_items,
            migrations.RunPython.noop),
    ]
