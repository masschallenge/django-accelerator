# Generated by Django 2.2.10 on 2021-06-08 14:54

from django.db import migrations
from polymorphic.utils import reset_polymorphic_ctype


def update_polymorphic_ctype(apps, schema_editor):
    CoreProfile = apps.get_model('accelerator', 'CoreProfile')
    ExpertProfile = apps.get_model('accelerator', 'ExpertProfile')
    EntrepreneurProfile = apps.get_model('accelerator', 'EntrepreneurProfile')
    MemberProfile = apps.get_model('accelerator', 'MemberProfile')
    reset_polymorphic_ctype(
        CoreProfile, EntrepreneurProfile, ExpertProfile, MemberProfile)


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0061_rename_member_profile'),
    ]

    operations = [
        migrations.RunPython(update_polymorphic_ctype,
                             migrations.RunPython.noop),
    ]
