# Generated by Django 2.2.27 on 2022-04-01 14:06
from django.db import (
    migrations,
    models,
)

ACKNOWLEDGEMENT_HELP_TEXT = (
    'I understand that my Startup Profile is a pre-requisite for '
    'applying to any MassChallenge Program')


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0095_update_nav_tree_access_restrictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='acknowledgement',
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text=ACKNOWLEDGEMENT_HELP_TEXT,
            ),
        ),
        migrations.AlterField(
            model_name='startup',
            name='bipoc_founder',
            field=models.BooleanField(
                blank=True,
                default=False,
                verbose_name='BIPOC Founder'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='female_or_transgender_founder',
            field=models.BooleanField(
                blank=True,
                default=False,
                verbose_name='Female or Transgender Founder'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='first_time_founder',
            field=models.BooleanField(
                blank=True,
                default=False,
                verbose_name='First-time Founder'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='is_startup',
            field=models.BooleanField(
                blank=True,
                default=False),
        ),
        migrations.AlterField(
            model_name='startup',
            name='is_visible',
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text=('Startup Profiles will be published to'
                           ' external websites through the the API.')),
        ),
    ]
