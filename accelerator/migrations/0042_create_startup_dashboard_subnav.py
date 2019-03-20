# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-25 12:56
from __future__ import unicode_literals

from django.db import migrations


def create_startup_dashboard_subnav(apps, schema_editor):
    NavTree = apps.get_model('accelerator', 'NavTree')
    UserRole = apps.get_model('accelerator', 'UserRole')
    NavTreeItem = apps.get_model('accelerator', 'NavTreeItem')
    tree = NavTree.objects.create(
        title='Startup Dashboard SubNav',
        alias='startup_dashboard_subnav')
    NavTreeItem.objects.create(
        title='Dashboard',
        url='startup_dashboard startup.id',
        urlaspattern=True,
        tree=tree
    )
    profile = NavTreeItem.objects.create(
        title='Profile',
        url='/',
        tree=tree
    )
    NavTreeItem.objects.create(
        title='View Profile',
        url='startup_preview startup.id',
        urlaspattern=True,
        parent=profile,
        tree=tree
    )
    NavTreeItem.objects.create(
        title='Edit Profile',
        url='edit_startup startup.id',
        urlaspattern=True,
        parent=profile,
        tree=tree
    )
    NavTreeItem.objects.create(
        title='Team',
        url='startup_team_view startup.id',
        urlaspattern=True,
        tree=tree
    )
    mentors_and_goals = NavTreeItem.objects.create(
        title='Mentors & Goals',
        url=(
            'startup_mentor_tracking_view startup_id'
            ' family_slug program_slug'
        ),
        urlaspattern=True,
        tree=tree
    )

    finalist_user_role = UserRole.objects.filter(name='Finalist').first()
    mentors_and_goals.user_role.add(finalist_user_role)


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0041_make_user_role_field_many_to_many'
        ),
    ]

    operations = [
        migrations.RunPython(create_startup_dashboard_subnav),
    ]
