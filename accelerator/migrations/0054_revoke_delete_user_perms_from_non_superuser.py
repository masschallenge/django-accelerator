# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import Permission


def revoke_delete_user_perms_from_non_superusers(apps, schema_editor):
    perm = Permission.objects.filter(name="Can delete user").first()
    if perm and perm.user_set.exists():
        perm.user_set.clear()


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0053_add_eventbrite_organization_id_field'
        ),
    ]

    operations = [
        migrations.RunPython(
            revoke_delete_user_perms_from_non_superusers,
            migrations.RunPython.noop),
    ]
