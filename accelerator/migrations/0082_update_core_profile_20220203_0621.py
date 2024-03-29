# Generated by Django 2.2.10 on 2022-01-31 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

PROFESSIONAL_DEGREE = ('Professional degree '
                       '(for example: MD, DDS, DVM, LLB, JD)')


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0081_add_community_participation_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='coreprofile',
            name='education_level',
            field=models.CharField(
                blank=True,
                null=True,
                choices=[('No formal schooling', 'No formal schooling'),
                         ('Completed high school', 'Completed high school'),
                         ('Associates degree (for example: AA, AS)',
                          'Associates degree (for example: AA, AS)'),
                         ('Bachelor’s degree (for example: BA. BS)',
                          'Bachelor’s degree (for example: BA. BS)'),
                         (PROFESSIONAL_DEGREE, PROFESSIONAL_DEGREE),
                         ('Advanced degree (Masters or Doctoral)',
                          'Advanced degree (Masters or Doctoral)')],
                max_length=200, verbose_name='Education Level'),
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='entrepreneur_interest',
            field=models.BooleanField(default=False,
                                      verbose_name='Enterpreneur Interest'),
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='expert_interest',
            field=models.BooleanField(default=False,
                                      verbose_name='Expert Interest'),
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='geographic_experience',
            field=models.CharField(
                blank=True,
                null=True,
                choices=[('United States-Northeast',
                          'United States-Northeast'),
                         ('United States-Southeast',
                          'United States-Southeast'),
                         ('United States-Southwest',
                          'United States-Southwest'),
                         ('United States-Northwest',
                          'United States-Northwest'),
                         ('United States-West', 'United States-West'),
                         ('United States-Midwest', 'United States-Midwest'),
                         ('United States-Alaska and Hawaii',
                          'United States-Alaska and Hawaii'),
                         ('Central America', 'Central America'),
                         ('South America', 'South America'),
                         ('Europe', 'Europe'),
                         ('Middle East', 'Middle East'),
                         ('Africa', 'Africa'),
                         ('East Asia', 'East Asia'),
                         ('South Asia', 'South Asia'),
                         ('Central Asia', 'Central Asia'),
                         ('Oceania', 'Oceania')],
                max_length=100,
                verbose_name='Geographic Experience/Expertise'),
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='preferred_name',
            field=models.CharField(blank=True,
                                   null=True,
                                   max_length=32,
                                   verbose_name='Prefered Name'),
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='pronouns',
            field=models.CharField(
                blank=True,
                null=True,
                choices=[('she, her, hers', 'She, Her, Hers'),
                         ('he, him, his', 'He, Him, His'),
                         ('they, them, theirs', 'They, Them, Theirs'),
                         ('Just my name please!', 'Just my name please!'),
                         ('other', 'Other')],
                max_length=32, verbose_name="Pronouns"),
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='shared_demographic_data',
            field=models.BooleanField(
                default=False,
                verbose_name='Permission To Shared Demographic Data'),
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='user_location',
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.ACCELERATOR_LOCATION_MODEL),
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='worldwide_participation_interest',
            field=models.BooleanField(
                default=False,
                verbose_name='World Wide Participation Interest'),
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='here_about_us',
            field=models.CharField(
                blank=True,
                null=True,
                choices=[('Advertising', 'Advertising'),
                         ('Email from MassChallenge',
                          'Email from MassChallenge'),
                         ('Search engine (Google, Yahoo, etc.)',
                          'Search engine (Google, Yahoo, etc.)'),
                         ('Recommended by friend or colleague',
                          'Recommended by friend or colleague'),
                         ('Recommended by a community organization',
                          'Recommended by a community organization'),
                         ('Social media', 'Social media'),
                         ('Blog or publication', 'Blog or publication'),
                         ('Other', 'Other')],
                max_length=100,
                verbose_name='Where did you here about us'),
        ),
    ]
