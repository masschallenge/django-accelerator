# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-19 10:21
from __future__ import unicode_literals

from django.db import migrations

from accelerator_abstract.models.base_nav_tree import MC_SIDE_NAV_TREE_ALIAS
from accelerator.models import NavTree
from accelerator.side_nav_tree_utils import (
    SIDE_NAV_TREE_ITEMS_LIST,
    add_user_roles_to_side_nav_items,
    create_items,
)


def add_items_to_side_nav_tree(apps, schema_editor):
    side_nav_tree = NavTree.objects.filter(
        alias=MC_SIDE_NAV_TREE_ALIAS).first()
    create_items(side_nav_tree, SIDE_NAV_TREE_ITEMS_LIST)
    add_user_roles_to_side_nav_items(SIDE_NAV_TREE_ITEMS_LIST)


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0044_create_side_nav_tree'),
    ]

    operations = [
        migrations.RunPython(add_items_to_side_nav_tree),
    ]
