# Generated by Django 2.2.18 on 2021-03-03 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0036_add_user_deferrable_modal'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrolemenu',
            name='user_type',
            field=models.CharField(
                blank=True,
                choices=[('EXPERT', 'Expert'), ('ENTREPRENEUR', 'Entrepreneur')],
                max_length=12),
        ),
    ]
