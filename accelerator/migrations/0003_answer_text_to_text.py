# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-02 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0002_mc_to_impact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgefeedbackcomponent',
            name='answer_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='judgefeedbackcomponent',
            name='original_answer_text',
            field=models.TextField(blank=True),
        ),
    ]
