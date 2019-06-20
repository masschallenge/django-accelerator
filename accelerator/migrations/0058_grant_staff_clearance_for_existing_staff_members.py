# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-06-12 19:38
from __future__ import unicode_literals

from django.db import migrations

STAFF = "Staff"  # don't import from models in migrations.


def grant_staff_clearances_for_role_grantees(apps, program_role):
    Clearance = apps.get_model('accelerator', 'Clearance')
    program_family = program_role.program.program_family
    user_ids = program_role.programrolegrant_set.values_list(
        "person_id", flat=True)
    for user_id in user_ids:
        Clearance.objects.get_or_create(
            user_id=user_id,
            program_family=program_family,
            defaults={"level": STAFF})


def grant_clearances_for_mc_staff_users(apps, schema_editor):
    ProgramRole = apps.get_model('accelerator', "ProgramRole")

    for program_role in ProgramRole.objects.filter(
            user_role__name=STAFF):
        grant_staff_clearances_for_role_grantees(apps, program_role)


def grant_demo_admin_clearance(apps, schema_editor):
    Clearance = apps.get_model('accelerator', 'Clearance')
    ProgramFamily = apps.get_model('accelerator', "ProgramFamily")
    User = apps.get_model('simpleuser', 'User')
    user = User.objects.filter(email="demoadmin@masschallenge.org").first()
    if user:
        [Clearance.objects.get_or_create(
            user=user,
            program_family=program_family,
            defaults={"level": STAFF})
         for program_family in ProgramFamily.objects.all()]


def revoke_staff_clearances(apps, schema_editor):
    Clearance = apps.get_model("accelerator", "Clearance")
    Clearance.objects.filter(level=STAFF).delete()


def grant_clearances(apps, schema_editor):
    grant_clearances_for_mc_staff_users(apps, schema_editor)
    grant_demo_admin_clearance(apps, schema_editor)


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0057_add_clearance_level_staff'),
    ]

    operations = [
        migrations.RunPython(
            grant_clearances,
            revoke_staff_clearances)
    ]
