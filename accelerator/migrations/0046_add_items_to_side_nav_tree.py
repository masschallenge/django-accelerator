# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-19 10:21
from __future__ import unicode_literals

from django.db import migrations

from accelerator.models import (
    MC_SIDE_NAV_TREE_ALIAS,
)
from accelerator.sitetree_navigation import (
    SIDE_NAV_ITEM_PROPS_LIST,
    add_user_roles_to_side_nav_items,
    create_items,
)


def add_items_to_side_nav_tree(apps, schema_editor):
    from accelerator.models import NavTree
    side_nav_tree = NavTree.objects.filter(
        alias=MC_SIDE_NAV_TREE_ALIAS).first()
    if side_nav_tree:
        create_items(side_nav_tree, SIDE_NAV_ITEM_PROPS_LIST)
        add_user_roles_to_side_nav_items(SIDE_NAV_ITEM_PROPS_LIST)


def delete_items_from_side_nav_tree(apps, schema_editor):
    NavTree = apps.get_model('accelerator', 'NavTree')
    side_nav_tree = NavTree.objects.filter(
        alias=MC_SIDE_NAV_TREE_ALIAS).first()
    NavTreeItem = apps.get_model('accelerator', 'NavTreeItem')
    if side_nav_tree:
        NavTreeItem.objects.filter(tree=side_nav_tree).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0045_create_side_nav_tree'),
    ]

    operations = [
        migrations.RunPython(
            add_items_to_side_nav_tree,
            delete_items_from_side_nav_tree),
    ]