# Generated by Django 2.2.28 on 2022-06-20 17:10

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0107_modify_description_20220620_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='associated_industry',
            field=models.CharField(default='',
                                   max_length=20),
        ),
    ]
