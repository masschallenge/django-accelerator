# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-14 09:25
from __future__ import unicode_literals

import django.db.models.deletion
import swapper
from django.conf import settings
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
                ('description', models.TextField()),

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
            name='UserLegalCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created_at',
                 models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('legal_check',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='user_set',
                                   to=swapper.get_model_name(
                                       'accelerator', 'LegalCheck'))),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='legalcheck_set',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Legal Check',
                'db_table': 'accelerator_userlegalcheck',
                'abstract': False,
                'managed': True,
                'swappable': swapper.swappable_setting('accelerator',
                                                       'UserLegalCheck'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='userlegalcheck',
            unique_together=set([('user', 'legal_check')]),
        ),
    ]

