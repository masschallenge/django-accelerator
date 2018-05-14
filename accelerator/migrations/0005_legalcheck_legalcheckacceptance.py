# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-14 09:25
from __future__ import unicode_literals

import django.db.models.deletion
import swapper
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0004_fix_acstream_contenttypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created_at',
                 models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(default='',
                                          max_length=128,
                                          unique=True)),
                ('title', models.CharField(default='', max_length=512)),
                ('url', models.URLField(max_length=100)),
            ],
            options={
                'verbose_name': 'Legal Check',
                'db_table': 'accelerator_legalcheck',
                'abstract': False,
                'managed': True,
                'swappable': swapper.swappable_setting('accelerator',
                                                       'LegalCheck'),
            },
        ),
        migrations.CreateModel(
            name='LegalCheckAcceptance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created_at',
                 models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('legal_check',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='profile_set',
                                   to=swapper.get_model_name(
                                       'accelerator', 'LegalCheck'))),
                ('profile',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='legalcheck_set',
                                   to=swapper.get_model_name(
                                       'accelerator', 'BaseProfile'))),
            ],
            options={
                'verbose_name': 'Legal Check Acceptance',
                'db_table': 'accelerator_legalcheckacceptance',
                'abstract': False,
                'managed': True,
                'swappable': swapper.swappable_setting('accelerator',
                                                       'LegalCheckAcceptance'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='legalcheckacceptance',
            unique_together=set([('profile', 'legal_check')]),
        ),
    ]
