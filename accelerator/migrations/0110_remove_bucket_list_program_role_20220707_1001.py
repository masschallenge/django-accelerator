from django.db import migrations


def remove_bucket_list_program_roles(apps, schema_editor):
    BucketState = apps.get_model('accelerator', 'BucketState')
    ProgramRole = apps.get_model('accelerator', 'ProgramRole')
    program_role_ids = BucketState.objects.values_list('program_role_id', flat=True)
    ProgramRole.objects.filter(pk__in=program_role_ids).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0109_remove_interest_fields_20220705_0425'),
    ]

    operations = [
        migrations.RunPython(remove_bucket_list_program_roles,
                             migrations.RunPython.noop)
    ]
