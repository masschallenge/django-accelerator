from django.db import migrations


def remove_bucket_list_program_roles(apps, schema_editor):
    BucketState = apps.get_model('accelerator', 'BucketState')
    ProgramRole = apps.get_model('accelerator', 'ProgramRole')
    ProgramRoleGrant = apps.get_model('accelerator', 'ProgramRoleGrant')
    NodePublishedFor = apps.get_model('accelerator', 'NodePublishedFor')

    program_role_ids = BucketState.objects.values_list('program_role_id',
                                                       flat=True)
    NodePublishedFor.objects.filter(
        published_for_id__in=program_role_ids).delete()
    ProgramRoleGrant.objects.filter(
        program_role_id__in=program_role_ids).delete()
    BucketState.objects.all().delete()
    ProgramRole.objects.filter(pk__in=program_role_ids).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0112_migrate_partner_manager_subnav'),
    ]

    operations = [
        migrations.RunPython(remove_bucket_list_program_roles,
                             migrations.RunPython.noop)
    ]
