# Generated by Django 2.2.10 on 2021-04-30 16:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0038_make_gender_field_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberprofile',
            name='bio',
            field=models.TextField(
                blank=True,
                default='',
                validators=[django.core.validators.MaxLengthValidator(7500)]),
        ),
        migrations.AlterField(
            model_name='entrepreneurprofile',
            name='bio',
            field=models.TextField(
                blank=True,
                default='',
                validators=[django.core.validators.MaxLengthValidator(7500)]),
        ),
    ]
