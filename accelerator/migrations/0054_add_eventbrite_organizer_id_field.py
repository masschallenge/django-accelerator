# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0053_add_eventbrite_organization_id_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='eventbrite_organizer_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        )
    ]
