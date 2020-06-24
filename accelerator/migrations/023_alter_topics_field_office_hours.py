from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0022_add_meeting_info_on_office_hour_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprogramofficehour',
            name='topics',
            field=models.TextField(blank=True),
        ),
    ]