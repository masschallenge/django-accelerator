# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accelerator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='user',
            field=models.ForeignKey(related_name='acc_startups',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='startup',
            field=models.ForeignKey(to='accelerator.Startup'),
        ),
        migrations.AddField(
            model_name='industry',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children',
                                             blank=True,
                                             to='accelerator.Industry',
                                             null=True),
        ),
    ]
