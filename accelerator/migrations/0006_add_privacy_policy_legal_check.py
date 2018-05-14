# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-14 09:09
from __future__ import unicode_literals

from django.db import migrations


def add_privacy_policy_legal_check(apps, schema_editor):
    LegalCheck = apps.get_model('accelerator', 'LegalCheck')
    LegalCheck.objects.create(
        name='accepted_privacy_policy',
        title='The MassChallenge Privacy Policy',
        url='https://masschallenge.org/privacy-policy'
    )


def remove_privacy_policy_legal_check(apps, schema_editor):
    LegalCheck = apps.get_model('accelerator', 'LegalCheck')
    LegalCheck.objects.filter(name='accepted_privacy_policy').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0005_legalcheck_legalcheckacceptance'),
    ]

    operations = [
        migrations.RunPython(add_privacy_policy_legal_check,
                             remove_privacy_policy_legal_check),

    ]
