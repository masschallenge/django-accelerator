from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0024_program_show_all_masschallenge_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='navtreeitem',
            name='active_user_roles',
            field=models.BooleanField(
                help_text='Whether to show on active user roles only',
                default=False),
        ),
    ]
