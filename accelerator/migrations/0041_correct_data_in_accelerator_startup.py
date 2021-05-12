# Generated by Django 2.2.16 on 2021-05-11 15:00

from django.db import migrations


MASSACHUSETTS = 'Massachusetts'
CALIFORNIA = 'California'
NEW_YORK = 'New York'
RHODE_ISLAND = 'Rhode Island'
MASSACHUSETTS_DATA_LIST = [
    'MASSACHUSETTS (MA)', 'Massachussetts ', 'MA', 'Ma.'
]


def update_accelerator_startup_data(apps, schema_editor):
    StartUp = apps.get_model('accelerator', 'Startup')
    StartUp.objects.filter(
        location_regional__in=MASSACHUSETTS_DATA_LIST
    ).update(location_regional=MASSACHUSETTS)

    StartUp.objects.filter(location_regional='CA').update(
        location_regional=CALIFORNIA)
    StartUp.objects.filter(location_regional='NY').update(
        location_regional=NEW_YORK)
    StartUp.objects.filter(location_regional='RI').update(
        location_regional=RHODE_ISLAND)


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0040_create_core_profile_table'),
    ]

    operations = [
        migrations.RunPython(update_accelerator_startup_data,
                             migrations.RunPython.noop)
    ]
