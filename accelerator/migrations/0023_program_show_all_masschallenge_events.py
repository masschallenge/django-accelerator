# Generated by Django 2.2.10 on 2020-06-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0022_add_meeting_info_on_office_hour_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='show_all_masschallenge_events',
            field=models.BooleanField(default=False),
        ),
    ]
