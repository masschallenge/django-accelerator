# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendationTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'accelerator_recommendationtag',
                'abstract': False,
                'managed': True,
            },
        ),
    ]
