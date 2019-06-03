# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import Permission


def revoke_delete_user_perms_from_all_users(apps, schema_editor):
    perm = Permission.objects.filter(name="Can delete user").first()
    if perm and perm.user_set.exists():
        perm.user_set.clear()


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0055_update_startup_dashboard_subnav_items'
        ),
    ]

    operations = [
        migrations.RunPython(
            revoke_delete_user_perms_from_all_users,
            migrations.RunPython.noop),
    ]
