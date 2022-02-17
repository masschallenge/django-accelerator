# Generated by Django 2.2.10 on 2022-02-16 19:51

from django.db import migrations, models

GEOGRAPHIC_EXPERIENCE_CHOICES = (
    "United States-Northeast",
    "United States-Southeast",
    "United States-Southwest",
    "United States-Northwest",
    "United States-West",
    "United States-Midwest",
    "United States-Alaska and Hawaii",
    "Central America",
    "South America",
    "Europe",
    "Middle East",
    "Africa",
    "East Asia",
    "South Asia",
    "Central Asia",
    "Oceania",
)

GEOGRAPHIC_EXPERIENCE_HELP_TEXT = (
    'You may select up to 5 regions. To select multiple regions, '
    'please press and hold Control (CTRL) on PCs or Command (&#8984;) on Macs')


def add_geographic_experience_options(apps, schema_editor):
    GeographicExperience = apps.get_model('accelerator', 'GeographicExperience')
    GeographicExperience.objects.bulk_create(
        [GeographicExperience(name=name) for name in GEOGRAPHIC_EXPERIENCE_CHOICES])


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0084_add_privacy_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeographicExperience',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='coreprofile',
            name='geographic_experience',
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='geographic_experience',
            field=models.ManyToManyField(
                blank=True,
                help_text=GEOGRAPHIC_EXPERIENCE_HELP_TEXT,
                to='accelerator.GeographicExperience',
                verbose_name='Geographic Experience/Expertise'),
        ),
        migrations.RunPython(add_geographic_experience_options,
                             migrations.RunPython.noop)
    ]
