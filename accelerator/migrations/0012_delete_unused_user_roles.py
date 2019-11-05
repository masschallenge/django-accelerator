# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-11-04 21:03
from __future__ import unicode_literals

from django.db import migrations


def delete_unused_user_roles(apps, schema_editor):
    unused_roles = ("Senior Judge", "Active Judge")
    UserRole = apps.get_model('accelerator', 'UserRole')
    UserRole.objects.filter(name__in=unused_roles).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0011_add_judge_and_expert_type'),
    ]

    operations = [
        migrations.RunPython(delete_unused_user_roles,
                             migrations.RunPython.noop)
    ]
