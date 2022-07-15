# Generated by Django 2.2.28 on 2022-04-20 13:05

import sorl.thumbnail.fields
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0101_add_industry_cluster_20220422_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='hubspot_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='program_image',
            field=sorl.thumbnail.fields.ImageField(
                blank=False,
                null=True,
                upload_to='program_images'),
        ),
    ]
