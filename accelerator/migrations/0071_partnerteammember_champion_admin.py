# Generated by Django 2.2.10 on 2021-08-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0070_judginground_champion_partner_label')
    ]

    operations = [
        migrations.AddField(
            model_name='partnerteammember',
            name='champion_admin',
            field=models.BooleanField(default=False),
        ),
    ]
