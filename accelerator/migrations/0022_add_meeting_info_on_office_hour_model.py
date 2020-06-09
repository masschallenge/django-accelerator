from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0021_add_nullable_startup_and_program_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorprogramofficehour',
            name='meeting_info',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]
