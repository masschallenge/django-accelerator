# Generated by Django 2.2.28 on 2022-06-20 15:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0106_migrate_startup_top_nav'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='associated_industry',
            field=models.CharField(default='', max_length=20),
        )
    ]
