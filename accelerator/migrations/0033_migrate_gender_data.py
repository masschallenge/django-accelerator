# Generated by Django 2.2.10 on 2021-01-22 12:13
from django.db import migrations

# gender identity
GENDER_MALE = "Male"
GENDER_FEMALE = "Female"
GENDER_PREFER_TO_SELF_DESCRIBE = "I Prefer To Self-describe"
GENDER_PREFER_NOT_TO_SAY = "I Prefer Not To Say"

# gender
MALE_CHOICE = "m"
FEMALE_CHOICE = "f"
OTHER_CHOICE = "o"
PREFER_NOT_TO_STATE_CHOICE = "p"

gender_map = {
    MALE_CHOICE: GENDER_MALE,
    FEMALE_CHOICE: GENDER_FEMALE,
    OTHER_CHOICE: GENDER_PREFER_TO_SELF_DESCRIBE,
    PREFER_NOT_TO_STATE_CHOICE: GENDER_PREFER_NOT_TO_SAY,
}


def get_gender_choice_obj_dict(apps):
    GenderChoices = apps.get_model("accelerator", "GenderChoices")
    return {
        gender_choice.name: gender_choice
        for gender_choice in GenderChoices.objects.all()
    }


def add_gender_identity_data(model, gender_choices):
    ThroughModel = model.gender_identity.through
    for gender, gender_identity in gender_map.items():
        gender_choice = gender_choices[gender_identity]
        profiles = model.objects.filter(gender=gender)
        ThroughModel.objects.bulk_create([
            ThroughModel(**{
                f"{model.__name__.lower()}": profile,
                "genderchoices": gender_choices[gender_identity]
            })
            for profile in profiles if not profile.gender_identity.filter(
                pk=gender_choice.pk).exists()
        ], ignore_conflicts=True)


def migrate_gender_data_to_gender_identity(apps, schema_editor):
    gender_choices = get_gender_choice_obj_dict(apps)
    MemberProfile = apps.get_model("accelerator", "MemberProfile")
    ExpertProfile = apps.get_model("accelerator", "ExpertProfile")
    EntrepreneurProfile = apps.get_model("accelerator", "EntrepreneurProfile")
    for model in [EntrepreneurProfile, ExpertProfile, MemberProfile]:
        add_gender_identity_data(model, gender_choices)


class Migration(migrations.Migration):
    dependencies = [
        ("accelerator", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            migrate_gender_data_to_gender_identity,
        )
    ]
