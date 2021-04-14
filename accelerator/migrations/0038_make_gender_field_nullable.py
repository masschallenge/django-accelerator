# Generated by Django 2.2.18 on 2021-04-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0037_add_user_type_to_userrolemenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneurprofile',
            name='gender',
            field=models.CharField(
                blank=True,
                choices=[
                    ('f', 'Female'),
                    ('m', 'Male'),
                    ('p', 'Prefer Not To State'),
                    ('o', 'Other'),
                    ('', 'Unknown'),
                ],
                default='',
                max_length=1,
                null=True),
        ),
        migrations.AlterField(
            model_name='expertprofile',
            name='gender',
            field=models.CharField(
                blank=True,
                choices=[
                    ('f', 'Female'),
                    ('m', 'Male'),
                    ('p', 'Prefer Not To State'),
                    ('o', 'Other'),
                    ('', 'Unknown'),
                ],
                default='',
                max_length=1,
                null=True),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='gender',
            field=models.CharField(
                blank=True,
                choices=[
                    ('f', 'Female'),
                    ('m', 'Male'),
                    ('p', 'Prefer Not To State'),
                    ('o', 'Other'),
                    ('', 'Unknown'),
                ],
                default='',
                max_length=1,
                null=True),
        ),
    ]
