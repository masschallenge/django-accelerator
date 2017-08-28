# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0002_avoid_direct_use_of_simpleuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='url_slug',
            field=models.CharField(default='',
                                   unique=True,
                                   max_length=64,
                                   blank=True,
                                   validators=[django.core.validators.RegexValidator('.*\\D.*', 'Slug must contain a non-numeral.'),
                                               django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')]),
        ),
    ]
