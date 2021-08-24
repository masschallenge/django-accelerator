# Generated by Django 2.2.24 on 2021-08-24 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0065_organization_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerJudgingInstructions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('instructions', models.TextField(help_text='Partner Judging instructions to guide teams in 500 characters or less.', max_length=500)),
                ('judging_round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.ACCELERATOR_JUDGINGROUND_MODEL)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.ACCELERATOR_PARTNER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'instructions from a partner to guide teams in evaluating startups',
                'db_table': 'accelerator_partnerjudginginstructions',
                'abstract': False,
                'managed': True,
                'swappable': 'ACCELERATOR_PARTNERJUDGINGINSTRUCTION_MODEL',
                'unique_together': {('partner', 'judging_round')},
            },
        ),
    ]