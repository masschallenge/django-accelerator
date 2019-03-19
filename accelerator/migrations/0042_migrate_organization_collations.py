from django.db import migrations


def get_conversion_function(collation, character_set='utf8'):
    def alter_collation_from_migration(apps, schema_editor):
        with schema_editor.connection.cursor() as cursor:
            cursor.execute(
                'ALTER TABLE accelerator_organization'
                'CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci')
    return alter_collation_from_migration


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0041_make_user_role_field_many_to_many'),
    ]
    operations = [
        migrations.RunPython(get_conversion_function('utf8mb4_general_ci')),
    ]
