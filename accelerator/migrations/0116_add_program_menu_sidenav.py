# Generated by Django 2.2.28 on 2022-07-28 02:37
import swapper
from django.db import migrations


def add_program_menu(apps, schema_editor):
    NavTreeItem = apps.get_model('accelerator', 'NavTreeItem')
    NavTree = swapper.load_model('accelerator', 'NavTree')
    nav_tree, _ = NavTree.objects.get_or_create(alias='mc_side_nav_tree')
    last_item = nav_tree.navtreeitem_set.all().last()
    sort_order = last_item.sort_order if last_item else nav_tree.id*10
    sort_order += 1
    NavTreeItem.objects.filter(
        alias='program_interest',
        url='/profile/programs/').delete()
    NavTreeItem.objects.get_or_create(
            title='Programs',
            alias='program_interest_manager',
            url='/programs',
            tree_id=nav_tree.id,
            sort_order=sort_order)


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0115_add_ecosystem_model'),
    ]

    operations = [
        migrations.RunPython(add_program_menu,
                             migrations.RunPython.noop)
    ]
