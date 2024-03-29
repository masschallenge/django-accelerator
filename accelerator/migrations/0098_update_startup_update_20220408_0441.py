# Generated by Django 2.2.10 on 2022-04-08 08:41
from django.db import migrations, models
from accelerator_abstract.models.base_startup_update import (
    DISCLOSURE_CONSENT
)
HEAD_COUNT = 'Headcount (Full Time, Part-Time, and Volunteers)'


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0097_create_startup_update_20220405_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startupupdate',
            name='acquired_date',
            field=models.DateField(
                blank=True,
                null=True,
                verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='acquired_valuation',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=13,
                null=True,
                verbose_name='Valuation'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_annualized_revenue',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=13,
                null=True,
                verbose_name='Anualized revenue (in US dollars)'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_funding_source_angel',
            field=models.BooleanField(
                default=False,
                verbose_name='Angel'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_funding_source_founders',
            field=models.BooleanField(
                default=False,
                verbose_name='Founder'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_funding_source_friends',
            field=models.BooleanField(
                default=False,
                verbose_name='Friends and Family'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_funding_source_gifts_grants',
            field=models.BooleanField(
                default=False, verbose_name='Gifts'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_funding_source_private_equity',
            field=models.BooleanField(
                default=False,
                verbose_name='Private Equity'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_funding_source_venture',
            field=models.BooleanField(
                default=False,
                verbose_name='Institutional VC'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_headcount',
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name=HEAD_COUNT),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_most_recent_investment_date',
            field=models.DateField(
                blank=True,
                null=True,
                verbose_name='Date of most recent investment'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_total_funding',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=13,
                null=True,
                verbose_name='Total Funding Raised (in US dollars)'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='active_valuation',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=13,
                null=True,
                verbose_name='Valuation (in US dollars)'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='current_status_hiring',
            field=models.BooleanField(
                default=False,
                verbose_name='This company is currently hiring'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='current_status_name_change',
            field=models.BooleanField(
                default=False,
                verbose_name='This company has changed its name'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='current_status_new_name',
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name='Current status name'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='current_status_seeking_investors',
            field=models.BooleanField(
                default=False,
                verbose_name='This company is currently seeking investors'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='funding_disclosure_consent',
            field=models.BooleanField(
                default=False,
                verbose_name=DISCLOSURE_CONSENT),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='ipo_date',
            field=models.DateField(
                blank=True,
                null=True,
                verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='startupupdate',
            name='ipo_valuation',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=13,
                null=True,
                verbose_name='Valuation'),
        ),
    ]
