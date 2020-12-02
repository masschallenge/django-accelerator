# Generated by Django 2.2.10 on 2020-12-01 19:01

from django.db import migrations
from accelerator_abstract.models.base_gender_choices import GENDER_CHOICES


def add_gender_choices(apps, schema_editor):
    GenderChoices = apps.get_model('accelerator', 'GenderChoices')
    db_gender_choices = GenderChoices.objects.all().values_list('name', flat=True)
    missing_gender_choices = set(GENDER_CHOICES).difference(db_gender_choices)
    if missing_gender_choices:
        GenderChoices.objects.bulk_create(
            [GenderChoices(name=choice) for choice in missing_gender_choices])


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0028_add_gender_fields'),
    ]

    operations = [
        migrations.RunPython(add_gender_choices,
                             migrations.RunPython.noop)
    ]
