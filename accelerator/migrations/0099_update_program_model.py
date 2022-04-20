# Generated by Django 2.2.28 on 2022-04-20 13:05

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0098_update_startup_update_20220408_0441'),
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
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
