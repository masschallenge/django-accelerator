# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0058_grant_staff_clearance_for_existing_staff_members'
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='eventbrite_organization_id',
        )
    ]
