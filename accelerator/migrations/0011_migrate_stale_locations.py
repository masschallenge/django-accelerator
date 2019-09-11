# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-26 09:03
from __future__ import unicode_literals

from django.db import migrations

TLV_LOCATION_OLD = "MassChallenge Israel - Tel Aviv"
TLV_LOCATION_NEW = "Other - see description"

REMOTE_LOCATION_OLD = "Remote"
REMOTE_LOCATION_NEW = "Remote - see description"


def forward(apps, schema_editor):
    MentorProgramOfficeHour = apps.get_model('accelerator',
                                             'MentorProgramOfficeHour')
    MentorProgramOfficeHour.objects.filter(
        location=TLV_LOCATION_OLD).update(location=TLV_LOCATION_NEW)
    MentorProgramOfficeHour.objects.filter(
        location=REMOTE_LOCATION_OLD).update(location=REMOTE_LOCATION_NEW)


def backward(apps, schema_editor):
    MentorProgramOfficeHour = apps.get_model('accelerator',
                                             'MentorProgramOfficeHour')
    MentorProgramOfficeHour.objects.filter(
        location=TLV_LOCATION_NEW).update(location=TLV_LOCATION_OLD)
    MentorProgramOfficeHour.objects.filter(
        location=REMOTE_LOCATION_NEW).update(location=REMOTE_LOCATION_OLD)


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0010_add_mentor_program_office_hour_locations'),
    ]

    operations = [
        migrations.RunPython(forward, backward)
    ]