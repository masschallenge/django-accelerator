# Generated by Django 2.2.10 on 2021-06-02 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0055_delete_expert_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExpertProfile1',
            new_name='ExpertProfile',
        ),
        migrations.AlterModelTable(
            name='expertprofile',
            table='accelerator_expertprofile',
        ),
    ]
