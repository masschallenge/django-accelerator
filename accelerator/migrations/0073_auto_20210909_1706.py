# Generated by Django 2.2.10 on 2021-09-09 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0072_partnerjudgeapplicationassignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerApplicationInterest',
            fields=[('id',
                     models.AutoField(auto_created=True,
                                      primary_key=True,
                                      serialize=False,
                                      verbose_name='ID')),
                    ('created_at', models.DateTimeField(auto_now_add=True,
                                                        null=True)),
                    ('updated_at', models.DateTimeField(auto_now=True,
                                                        null=True)),
                    ('advance_to_next_round', models.BooleanField(
                        default=False)),
                    ('application', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.ACCELERATOR_APPLICATION_MODEL)),
                    ('judging_round', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.ACCELERATOR_JUDGINGROUND_MODEL)),
                    ('partner', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.ACCELERATOR_PARTNER_MODEL)),
                    ],
            options={
                'db_table': 'accelerator_partnerapplicationinterest',
                'abstract': False,
                'managed': True,
                'swappable': 'ACCELERATOR_PARTNERAPPLICATIONINTEREST_MODEL',
            },
        ),
        migrations.DeleteModel(
            name='PartnerStartupInterest',
        ),
    ]
