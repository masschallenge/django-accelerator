# Generated by Django 2.2.10 on 2021-11-12 18:09

from django.db import migrations
from simpleuser.models import User


def remove_finalist_role_from_staff(apps, schema_editor):
    ProgramRoleGrant = apps.get_model("accelerator", "ProgramRoleGrant")
    ProgramRole = apps.get_model("accelerator", "ProgramRole")
    Clearance = apps.get_model("accelerator", "Clearance")
    staff_ids = set(Clearance.objects.all().values_list(
        'user__pk', flat=True)).union(
        set(User.objects.filter(
            is_superuser=True).values_list('pk', flat=True)))
    program_role_ids = ProgramRole.objects.filter(
        user_role__name='Finalist').values_list('id', flat=True)
    ProgramRoleGrant.objects.filter(
        program_role__in=program_role_ids,
        person_id__in=staff_ids).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0074_update_url_to_community'),
    ]

    operations = [
        migrations.RunPython(remove_finalist_role_from_staff,
                             migrations.RunPython.noop)
    ]
