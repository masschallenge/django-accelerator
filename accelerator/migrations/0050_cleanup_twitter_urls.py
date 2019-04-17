# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from accelerator.twitter_handle_cleanup import (
    clean_entrepreneur_profile_twitter_handles,
    clean_expert_profile_twitter_handles,
    clean_organization_twitter_handles
)


def clean_up_twitter_handles(apps, schema_editor):
    Organization = apps.get_model('accelerator', 'Organization')
    ExpertProfile = apps.get_model('accelerator', 'ExpertProfile')
    EntrepreneurProfile = apps.get_model(
        'accelerator',
        'EntrepreneurProfile')

    clean_entrepreneur_profile_twitter_handles(EntrepreneurProfile)
    clean_expert_profile_twitter_handles(ExpertProfile)
    clean_organization_twitter_handles(Organization)


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0049_update_office_hour_location_choices'
        ),
    ]

    operations = [
        migrations.RunPython(
            clean_up_twitter_handles,
            migrations.RunPython.noop),
    ]
