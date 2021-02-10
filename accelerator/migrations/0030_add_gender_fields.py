from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrepreneurprofile',
            name='gender_self_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='entrepreneurprofile',
            name='gender_identity',
            field=models.ManyToManyField(
                blank=True,
                to=settings.ACCELERATOR_GENDERCHOICES_MODEL),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='gender_self_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='gender_identity',
            field=models.ManyToManyField(
                blank=True,
                to=settings.ACCELERATOR_GENDERCHOICES_MODEL),
        ),
        migrations.AddField(
            model_name='memberprofile',
            name='gender_self_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='memberprofile',
            name='gender_identity',
            field=models.ManyToManyField(
                blank=True,
                to=settings.ACCELERATOR_GENDERCHOICES_MODEL),
        ),
    ]
