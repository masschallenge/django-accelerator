# Generated by Django 2.2.10 on 2021-11-10 13:17

from django.db import migrations


def remove_finalist_role_from_staff(apps, schema_editor):
    User = apps.get_model("accelerator", "User")
    ProgramRoleGrant = apps.get_model("accelerator", "ProgramRoleGrant")
    staff_ids = User.objects.filter(
        programrolegrant__program_role__user_role__name='Finalist',
        is_staff=True).values_list('id', flat=True)

    staff_finalist_role = ProgramRoleGrant.objects.filter(
                program_role__user_role__name='Finalist',
                person_id__in=staff_ids).values_list(
                    'id', flat=True)

    for role in staff_finalist_role:
        role.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0073_auto_20210909_1706'),
    ]

    operations = [
        migrations.RunPython(remove_finalist_role_from_staff,
                             migrations.RunPython.noop)
    ]
