# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0053_add_eventbrite_organization_id_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='eventbrite_organization_id',
            new_name='eventbrite_organizer_id'
        )
    ]
