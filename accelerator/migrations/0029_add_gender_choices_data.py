# Generated by Django 2.2.10 on 2020-12-01 19:01

from django.db import migrations

GENDER_MALE_CHOICE = "Male"
GENDER_FEMALE_CHOICE = "Female"
GENDER_CISGENDER_CHOICE = "Cisgender"
GENDER_TRANSGENDER_CHOICE = "Transgender"
GENDER_NON_BINARY_CHOICE = "Non-Binary"
GENDER_PREFER_TO_SELF_DESCRIBE_CHOICE = "I Prefer To Self-describe"
GENDER_PREFER_NOT_TO_SAY_CHOICE = "I Prefer Not To Say"

GENDER_CHOICES = (
    GENDER_MALE_CHOICE,
    GENDER_FEMALE_CHOICE,
    GENDER_CISGENDER_CHOICE,
    GENDER_TRANSGENDER_CHOICE,
    GENDER_NON_BINARY_CHOICE,
    GENDER_PREFER_TO_SELF_DESCRIBE_CHOICE,
    GENDER_PREFER_NOT_TO_SAY_CHOICE
)


def add_gender_choices(apps, schema_editor):
    GenderChoices = apps.get_model('accelerator', 'GenderChoices')
    db_gender_choices = GenderChoices.objects.all().values_list(
        'name', flat=True)
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
