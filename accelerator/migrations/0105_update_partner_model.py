# Generated by Django 2.2.28 on 2022-06-02 17:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0104_update_startupupdate_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='additional_industries',
            field=models.ManyToManyField(
                blank=True,
                db_table='accelerator_partner_related_industry',
                help_text='You may select up to 5 related industries.',
                null=True,
                related_name='secondary_partners',
                to=settings.MPTT_SWAPPABLE_INDUSTRY_MODEL,
                verbose_name='Additional Industries'),
        ),
        migrations.AddField(
            model_name='partner',
            name='date_founded',
            field=models.CharField(
                blank=True,
                help_text='Month and Year when your partner was founded.',
                max_length=100,
                null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='facebook_url',
            field=models.URLField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name='Facebook profile URL'),
        ),
        migrations.AddField(
            model_name='partner',
            name='full_elevator_pitch',
            field=models.TextField(
                blank=True,
                help_text='Your enterprise in 140 characters or less.',
                max_length=500,
                null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='is_visible',
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text='Partner Profiles will be published to external'
                          'websites through the the API.'),
        ),
        migrations.AddField(
            model_name='partner',
            name='linked_in_url',
            field=models.URLField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name='LinkedIn profile URL'),
        ),
        migrations.AddField(
            model_name='partner',
            name='location_city',
            field=models.CharField(
                blank=True,
                default='',
                help_text='Please specify the city where your main office'
                          '(headquarters) is located. (e.g. Boston)',
                max_length=100,
                null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='location_national',
            field=models.CharField(
                blank=True,
                default='',
                help_text='Please specify the country where your main office'
                          '(headquarters) is located',
                max_length=100,
                null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='location_regional',
            field=models.CharField(
                blank=True,
                default='',
                help_text='Please specify the state, region or province where'
                          'your main office (headquarters) is located'
                          '(if applicable).',
                max_length=100,
                null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='location_street_address',
            field=models.CharField(
                blank=True,
                default='',
                help_text='Please specify the street address for your'
                          'main office (headquarters).',
                max_length=100,
                null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='primary_industry',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='partners',
                to=settings.MPTT_SWAPPABLE_INDUSTRY_MODEL,
                verbose_name='Primary Industry categorization'),
        ),
        migrations.AddField(
            model_name='partner',
            name='short_pitch',
            field=models.TextField(
                blank=True,
                help_text='Your enterprise in 140 characters or less.',
                max_length=140,
                null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='video_elevator_pitch_url',
            field=embed_video.fields.EmbedVideoField(
                blank=True,
                help_text='Upload your 1-3 minute video pitch to'
                          'Vimeo or Youtube. Paste the shared link here.',
                max_length=100,
                null=True),
        ),
    ]
