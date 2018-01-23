# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import embed_video.fields
import mptt.fields
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('abbr', models.CharField(unique=True, max_length=3)),
                ('usd_exchange', models.FloatField()),
            ],
            options={
                'swappable': 'ACCELERATOR_CURRENCY_MODEL',
                'db_table': 'accelerator_currency',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=50, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to=settings.MPTT_SWAPPABLE_INDUSTRY_MODEL, null=True)),
            ],
            options={
                'swappable': 'MPTT_SWAPPABLE_INDUSTRY_MODEL',
                'db_table': 'accelerator_industry',
                'managed': True,
                'verbose_name_plural': 'Industries',
            },
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('postdate', models.DateTimeField()),
                ('type', models.CharField(max_length=20, choices=[('NONE', 'None'), ('INTERNSHIP', 'An internship'), ('PART_TIME_PERMANENT', 'A part-time permanent position'), ('FULL_TIME_PERMANENT', 'A full-time permanent position'), ('PART_TIME_CONTRACT', 'A part-time contract position'), ('FULL_TIME_CONTRACT', 'A full-time contract position')])),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('applicationemail', models.EmailField(max_length=100, null=True, verbose_name='Email address', blank=True)),
                ('more_info_url', models.URLField(max_length=100, null=True, blank=True)),
            ],
            options={
                'swappable': 'ACCELERATOR_JOBPOSTING_MODEL',
                'db_table': 'accelerator_jobposting',
                'managed': True,
                'verbose_name_plural': 'Job postings for startups',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('website_url', models.URLField(max_length=100, blank=True)),
                ('twitter_handle', models.CharField(help_text='Omit the "@". We\'ll add it.', max_length=40, blank=True)),
                ('public_inquiry_email', models.EmailField(max_length=100, verbose_name='Email address', blank=True)),
                ('url_slug', models.CharField(default='', unique=True, max_length=64, blank=True, validators=[django.core.validators.RegexValidator(regex='^[\\w-]+$', message='Letters, numbers, and dashes only.')])),
            ],
            options={
                'managed': True,
                'ordering': ['name'],
                'abstract': False,
                'verbose_name_plural': 'Organizations',
                'db_table': 'accelerator_organization',
                'swappable': 'ACCELERATOR_ORGANIZATION_MODEL',
            },
        ),
        migrations.CreateModel(
            name='RecommendationTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('text', models.TextField()),
            ],
            options={
                'swappable': 'ACCELERATOR_RECOMMENDATIONTAG_MODEL',
                'db_table': 'accelerator_recommendationtag',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_visible', models.BooleanField(default=True, help_text='Startup Profiles will be published to external websites through the the API.')),
                ('short_pitch', models.CharField(help_text='Your startup in 140 characters or less.', max_length=140)),
                ('full_elevator_pitch', models.TextField(help_text='Your startup in 500 characters or less.', max_length=500)),
                ('linked_in_url', models.URLField(max_length=100, blank=True)),
                ('facebook_url', models.URLField(max_length=100, blank=True)),
                ('high_resolution_logo', sorl.thumbnail.fields.ImageField(upload_to='startup_pics', verbose_name='High Resolution Logo', blank=True)),
                ('video_elevator_pitch_url', embed_video.fields.EmbedVideoField(help_text="The Startup Profile video is great way to show off your startup to the judges and the broader MassChallenge community (if you're not in stealth mode). Brevity is recommended and videos should not be longer than 1-3 minutes. Please submit YouTube or Vimeo URLs.", max_length=100, blank=True)),
                ('created_datetime', models.DateTimeField(null=True, blank=True)),
                ('last_updated_datetime', models.DateTimeField(null=True, blank=True)),
                ('community', models.CharField(blank=True, max_length=64, choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')])),
                ('profile_background_color', models.CharField(default='217181', max_length=7, blank=True, validators=[django.core.validators.RegexValidator('^([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|)$', 'Color must be 3 or 6-digit hexecimal number, such as FF0000 for red.')])),
                ('profile_text_color', models.CharField(default='FFFFFF', max_length=7, blank=True, validators=[django.core.validators.RegexValidator('^([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|)$', 'Color must be 3 or 6-digit hexecimal number, such as FF0000 for red.')])),
                ('location_national', models.CharField(default='', help_text='Please specify the country where your main office (headquarters) is located', max_length=100, blank=True)),
                ('location_regional', models.CharField(default='', help_text='Please specify the state, region or province where your main office (headquarters) is located (if applicable).', max_length=100, blank=True)),
                ('location_city', models.CharField(default='', help_text='Please specify the city where your main office (headquarters) is located. (e.g. Boston)', max_length=100, blank=True)),
                ('location_postcode', models.CharField(default='', help_text='Please specify the postal code for your main office (headquarters). (ZIP code, Postcode, codigo postal, etc.)', max_length=100, blank=True)),
                ('date_founded', models.CharField(help_text='Month and Year when your startup was founded.', max_length=100, blank=True)),
                ('landing_page', models.CharField(max_length=255, null=True, blank=True)),
                ('additional_industries', models.ManyToManyField(related_name='secondary_startups', to=settings.MPTT_SWAPPABLE_INDUSTRY_MODEL, db_table=b'accelerator_startup_related_industry', blank=True, help_text='You may select up to 5 related industries.', verbose_name='Additional Industries')),
                ('currency', models.ForeignKey(blank=True, to=settings.ACCELERATOR_CURRENCY_MODEL, null=True)),
                ('organization', models.ForeignKey(related_name='startups', blank=True, to=settings.ACCELERATOR_ORGANIZATION_MODEL, null=True)),
                ('primary_industry', models.ForeignKey(related_name='startups', verbose_name='Primary Industry categorization', to=settings.MPTT_SWAPPABLE_INDUSTRY_MODEL)),
                ('recommendation_tags', models.ManyToManyField(to=settings.ACCELERATOR_RECOMMENDATIONTAG_MODEL, blank=True)),
                ('user', models.ForeignKey(related_name='acc_startups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['organization__name'],
                'swappable': 'ACCELERATOR_STARTUP_MODEL',
                'db_table': 'accelerator_startup',
                'managed': True,
                'verbose_name_plural': 'Startups',
            },
        ),
        migrations.AddField(
            model_name='jobposting',
            name='startup',
            field=models.ForeignKey(to=settings.ACCELERATOR_STARTUP_MODEL),
        ),
    ]
