# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-26 13:08
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


def add_mc_nodesubnavigation_permissions(apps, schema_editor):
    perms = Permission.objects.filter(
        content_type__app_label='accelerator',
        content_type__model='nodesubnavassociation')
    for perm in perms:
        ct, _ = ContentType.objects.get_or_create(
            app_label="mc",
            model=perm.content_type.model)
        new_perm, _ = Permission.objects.get_or_create(
            name=perm.name,
            content_type=ct,
            codename=perm.codename)
        for user in perm.user_set.all():
            user.user_permissions.add(new_perm)


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0058_grant_staff_clearance_for_existing_staff_members'),
    ]

    operations = [
        migrations.RunPython(add_mc_nodesubnavigation_permissions,
                             migrations.RunPython.noop)
    ]
