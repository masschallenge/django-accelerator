# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-19 09:55
from __future__ import unicode_literals

from django.db import migrations

from accelerator.models import MC_SIDE_NAV_TREE_ALIAS


def create_side_nav_tree(apps, schema_editor):
    NavTree = apps.get_model('accelerator', 'NavTree')
    navtree_kwargs = {
        'title': "MC Side Nav Tree",
        'alias': MC_SIDE_NAV_TREE_ALIAS
    }
    NavTree.objects.update_or_create(**navtree_kwargs)


def delete_side_nav_tree(apps, schema_editor):
    NavTree = apps.get_model('accelerator', 'NavTree')
    NavTree.objects.filter(alias=MC_SIDE_NAV_TREE_ALIAS).delete()


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0044_add_sitetree_sidenav_toggle'
        ),
    ]

    operations = [
        migrations.RunPython(
            create_side_nav_tree,
            delete_side_nav_tree),
    ]