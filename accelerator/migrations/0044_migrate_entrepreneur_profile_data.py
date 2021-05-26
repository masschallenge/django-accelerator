# Generated by Django 2.2.10 on 2021-05-26 09:37

from django.db import migrations


def migrate_entrepreneur_profile_data(apps, schema_editor):
    EntrepreneurProfile = apps.get_model('accelerator', 'EntrepreneurProfile')
    EntrepreneurProfile1 = apps.get_model('accelerator', 'EntrepreneurProfile1')
    for profile in EntrepreneurProfile.objects.all():
        profile_dict = profile.__dict__.copy()
        profile_dict.pop("_state")
        EntrepreneurProfile1.objects.create(**profile_dict)


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0043_add_entrepreneurprofile1'),
    ]

    operations = [
        migrations.RunPython(migrate_entrepreneur_profile_data,
                             migrations.RunPython.noop),
    ]
