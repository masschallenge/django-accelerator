# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            'accelerator',
            '0060_add_mc_nodesubnavigation_permissions'
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='eventbrite_organization_id',
        )
    ]
