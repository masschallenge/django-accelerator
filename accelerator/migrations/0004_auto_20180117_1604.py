# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0003_change_url_slug_validation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='is_visible',
            field=models.BooleanField(default=True, help_text='this is a test.'),
        ),
    ]
