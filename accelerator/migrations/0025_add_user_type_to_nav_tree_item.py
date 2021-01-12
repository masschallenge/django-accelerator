# Generated by Django 2.2.10 on 2020-09-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0024_program_show_all_masschallenge_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='navtreeitem',
            name='user_type',
            field=models.CharField(
                blank=True, choices=[
                    ('EXPERT', 'Expert'),
                    ('ENTREPRENEUR', 'Entrepreneur')
                    ], max_length=12),
        ),
    ]