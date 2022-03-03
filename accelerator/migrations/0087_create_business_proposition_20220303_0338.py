# Generated by Django 2.2.10 on 2022-03-03 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
INVESTOR = 'Current or anticipated advisors or investors'


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0086_alter_founder_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coreprofile',
            name='preferred_name',
            field=models.CharField(
                blank=True,
                max_length=32,
                null=True,
                verbose_name='Nickname / Preferred Name'),
        ),
        migrations.CreateModel(
            name='BusinessProposition',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    null=True)),
                ('updated_at', models.DateTimeField(auto_now=True,
                                                    null=True)),
                ('pain_point', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name="Customer Pain Point")),
                ('solution', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Solution')),
                ('impact', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='One-Year / Five-Year Impact (?)')),
                ('market', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Potential Market / Addressable Size')),
                ('value_proposition', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Value Proposition / Marketing Message')),
                ('sales', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Sales and Distribution / Channels')),
                ('competitors', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Current and Future Competitors')),
                ('product_complements', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Product Complements / Value Chain Partners')),
                ('primary_advantages', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Primary Advantages vs Competitors')),
                ('drivers', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Key Drivers of Business Economics')),
                ('intellectual_property', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Intellectual Property')),
                ('regulation', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Regulatory Requirements')),
                ('team_summary', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Team (Backgrounds, advantages)')),
                ('investors', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name=INVESTOR)),
                ('validation', models.TextField(
                    blank=True,
                    null=True,
                    verbose_name='Traction and Market Validation')),
                ('startup', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.ACCELERATOR_STARTUP_MODEL)),
            ],
            options={
                'abstract': False,
                'managed': True,
                'swappable': 'ACCELERATOR_BUSINESSPROPOSITION_MODEL',
            },
        ),
    ]
