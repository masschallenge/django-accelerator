# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-10 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0002_add_mc_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprogramofficehour',
            name='location',
            field=models.CharField(choices=[('MassChallenge Boston', 'MassChallenge Boston'), ('MassChallenge Israel - Jerusalem', 'MassChallenge Israel - Jerusalem'), ('MassChallenge Israel - Tel Aviv', 'MassChallenge Israel - Tel Aviv'), ('MassChallenge Mexico', 'MassChallenge Mexico'), ('MassChallenge Rhode Island', 'MassChallenge Rhode Island'), ('MassChallenge Switzerland', 'MassChallenge Switzerland'), ('MassChallenge Texas', 'MassChallenge Texas'), ('Newton Innovation Center (NIC)', 'Newton Innovation Center (NIC)'), ('PULSE@MassChallenge', 'PULSE@MassChallenge'), ('Remote', 'Remote')], max_length=50),
        ),
    ]
