# Generated by Django 2.2.10 on 2022-04-05 13:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accelerator',
         '0096_remove_nullable_option_on_startup_boolean_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='current_status_hiring',
            field=models.BooleanField(
                default=False,
                verbose_name='Current status hiring'),
        ),
        migrations.AddField(
            model_name='organization',
            name='current_status_seeking_investors',
            field=models.BooleanField(
                default=False,
                verbose_name='Current status seeeking investors'),
        ),
        migrations.AddField(
            model_name='organization',
            name='funding_disclosure_consent',
            field=models.BooleanField(
                default=False,
                verbose_name='Funding disclosure consent'),
        ),
        migrations.CreateModel(
            name='StartupUpdate',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True, null=True)),
                ('current_status_hiring', models.BooleanField(
                    default=False,
                    verbose_name='Current status hiring')),
                ('current_status_seeking_investors', models.BooleanField(
                    default=False,
                    verbose_name='Current status seeeking investors')),
                ('funding_disclosure_consent', models.BooleanField(
                    default=False,
                    verbose_name='Funding disclosure consent')),
                ('current_status_name_change', models.BooleanField(
                    default=False,
                    verbose_name='Current status name change')),
                ('current_status_new_name', models.TextField(
                    verbose_name='Current status name')),
                ('company_disposition', models.CharField(
                    choices=[
                        ('active', 'active'),
                        ('closed-ipo', 'closed-ipo'),
                        ('closed-acquisition', 'closed-acquisition'),
                        ('closed-inactive', 'closed-inactive'),
                        ('departed-staff', 'departed-staff')],
                    max_length=100,
                    verbose_name='Company disposition')),
                ('active_annualized_revenue', models.DecimalField(
                    decimal_places=2,
                    max_digits=13,
                    verbose_name='Active annualized revenue')),
                ('active_headcount', models.IntegerField(
                    verbose_name='Active headcount')),
                ('active_total_funding', models.DecimalField(
                    decimal_places=2, max_digits=13,
                    verbose_name='Active total funding')),
                ('active_funding_source_founders', models.BooleanField(
                    default=False,
                    verbose_name='Active funding source founders')),
                ('active_funding_source_friends', models.BooleanField(
                    default=False,
                    verbose_name='Active funding source friends')),
                ('active_funding_source_angel', models.BooleanField(
                    default=False,
                    verbose_name='Active funding source angel')),
                ('active_funding_source_venture', models.BooleanField(
                    default=False,
                    verbose_name='Active funding source venture')),
                ('active_funding_source_private_equity', models.BooleanField(
                    default=False,
                    verbose_name='Active funding source private equity')),
                ('active_funding_source_gifts_grants', models.BooleanField(
                    default=False,
                    verbose_name='Active funding source gift grants')),
                ('active_funding_source_other', models.BooleanField(
                    default=False,
                    verbose_name='Active funding source other')),
                ('active_most_recent_investment_date', models.DateField(
                    verbose_name='Active most recent investment date')),
                ('active_valuation', models.DecimalField(
                    decimal_places=2,
                    max_digits=13,
                    verbose_name='Active valuation')),
                ('ipo_valuation', models.DecimalField(
                    decimal_places=2,
                    max_digits=13,
                    verbose_name='IPO valuation')),
                ('ipo_date', models.DateField(verbose_name='IPO date')),
                ('acquired_valuation', models.DecimalField(
                    decimal_places=2,
                    max_digits=13,
                    verbose_name='Acquired valuation')),
                ('acquired_date', models.DateField(
                    verbose_name='Acquired date')),
                ('startup', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.ACCELERATOR_STARTUP_MODEL)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
    ]
