# Generated by Django 2.2.28 on 2022-07-06 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0110_add_verbose_names_on_partner_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coreprofile',
            name='judge_interest',
        ),
        migrations.RemoveField(
            model_name='coreprofile',
            name='mentor_interest',
        ),
        migrations.RemoveField(
            model_name='coreprofile',
            name='speaker_interest',
        ),
    ]
