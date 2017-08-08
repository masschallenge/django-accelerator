# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 17:55
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import mptt.fields
import re
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('abbr', models.CharField(max_length=3, unique=True)),
                ('usd_exchange', models.FloatField()),
            ],
            options={
                'db_table': 'accelerator_currency',
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.CharField(blank=True, max_length=50)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='accelerator.Industry')),
            ],
            options={
                'verbose_name_plural': 'Industries',
                'db_table': 'accelerator_industry',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('postdate', models.DateTimeField()),
                ('type', models.CharField(choices=[('NONE', 'None'), ('INTERNSHIP', 'An internship'), ('PART_TIME_PERMANENT', 'A part-time permanent position'), ('FULL_TIME_PERMANENT', 'A full-time permanent position'), ('PART_TIME_CONTRACT', 'A part-time contract position'), ('FULL_TIME_CONTRACT', 'A full-time contract position')], max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('applicationemail', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email address')),
                ('more_info_url', models.URLField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Job postings for startups',
                'db_table': 'accelerator_jobposting',
                'abstract': False,
                'managed': True,
            },
        ),
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
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('is_visible', models.BooleanField(default=True, help_text='Startup Profiles will be published to external websites through the the API.')),
                ('short_pitch', models.CharField(help_text='Your startup in 140 characters or less.', max_length=140)),
                ('full_elevator_pitch', models.TextField(help_text='Your startup in 500 characters or less.', max_length=500)),
                ('website_url', models.CharField(blank=True, max_length=100)),
                ('linked_in_url', models.URLField(blank=True, max_length=100)),
                ('facebook_url', models.URLField(blank=True, max_length=100)),
                ('high_resolution_logo', sorl.thumbnail.fields.ImageField(blank=True, upload_to='startup_pics', verbose_name='High Resolution Logo')),
                ('twitter_handle', models.CharField(blank=True, help_text='Omit the "@". We\'ll add it.', max_length=40)),
                ('public_inquiry_email', models.EmailField(blank=True, help_text='This email will be published to external websites through the API.', max_length=100, verbose_name='Email address')),
                ('video_elevator_pitch_url', embed_video.fields.EmbedVideoField(blank=True, help_text='The Startup Profile video is great way to show off your startup to the judges and the broader community. Brevity is recommended and videos should not be longer than 1-3 minutes. Please submit YouTube or Vimeo URLs.', max_length=100)),
                ('created_datetime', models.DateTimeField(blank=True, null=True)),
                ('last_updated_datetime', models.DateTimeField(blank=True, null=True)),
                ('community', models.CharField(blank=True, choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')], max_length=64)),
                ('url_slug', models.CharField(blank=True, default='', max_length=64, unique=True, validators=[django.core.validators.RegexValidator('.*\\D.*', 'Slug must contain a non-numeral.'), django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('profile_background_color', models.CharField(blank=True, default='217181', max_length=7, validators=[django.core.validators.RegexValidator('^([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|)$', 'Color must be 3 or 6-digit hexecimal number, such as FF0000 for red.')])),
                ('profile_text_color', models.CharField(blank=True, default='FFFFFF', max_length=7, validators=[django.core.validators.RegexValidator('^([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|)$', 'Color must be 3 or 6-digit hexecimal number, such as FF0000 for red.')])),
                ('location_national', models.CharField(blank=True, default='', help_text='Please specify the country where your main office (headquarters) is located', max_length=100)),
                ('location_regional', models.CharField(blank=True, default='', help_text='Please specify the state, region or province where your main office (headquarters) is located (if applicable).', max_length=100)),
                ('location_city', models.CharField(blank=True, default='', help_text='Please specify the city where your main office (headquarters) is located. (e.g. Boston)', max_length=100)),
                ('location_postcode', models.CharField(blank=True, default='', help_text='Please specify the postal code for your main office (headquarters). (ZIP code, Postcode, codigo postal, etc.)', max_length=100)),
                ('date_founded', models.CharField(blank=True, help_text='Month and Year when your startup was founded.', max_length=100)),
                ('landing_page', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_industry_categories', models.ManyToManyField(blank=True, db_table='accelerator_startup_related_industry', help_text='You may select up to 5 related industries.', related_name='secondary_startups', to='accelerator.Industry', verbose_name='Related Industries')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accelerator.Currency')),
                ('primary_industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='startups', to='accelerator.Industry', verbose_name='Primary Industry categorization')),
                ('recommendation_tags', models.ManyToManyField(blank=True, to='accelerator.RecommendationTag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Startups',
                'db_table': 'accelerator_startup',
                'ordering': ['name'],
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='jobposting',
            name='startup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accelerator.Startup'),
        ),
    ]
