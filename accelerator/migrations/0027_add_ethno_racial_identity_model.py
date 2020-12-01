from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0026_remove_character_limit_to_application_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='EthnoRacialIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    null=True)),
                ('updated_at', models.DateTimeField(auto_now=True,
                                                    null=True)),
                ('identity', models.CharField(
                    blank=True,
                    choices=[
                        ('Black',
                         'e.g., African American, Haitian, Nigerian, Somali'),
                        ('East and/or Southeast Asian',
                         'e.g., Chinese, Filipino, Korean, Indonesian'),
                        ('Hispanic, Latinx, and/or Spanish',
                         'e.g., Brazilian, Colombian, Mexican, Nicaraguan'),
                        ('Indigenous',
                         'e.g., Aboriginal, Inuit, Maasai, Native American'),
                        ('Native Hawaiian, Pacific Islander, or Polynesian',
                         'Native Hawaiian, Pacific Islander, or Polynesian'),
                        ('Middle Eastern and/or North African',
                         'e.g., Egyptian, Emirati, Iranian, Moroccan'),
                        ('North and/or Central Asian',
                         'e.g., Kazakh, Siberian, Tajik, Uzbek'),
                        ('South Asian',
                         'e.g., Bangladeshi, Indian, Pakistani, Sri Lankan'),
                        ('White or Caucasian',
                         'White or Caucasian'),
                        ('I prefer not to say',
                         'I prefer not to say')],
                    max_length=100,
                    null=True)
                 ),
            ],
            options={
                'db_table': 'accelerator_ethnoracialidentity',
                'abstract': False,
                'managed': True,
                'swappable': 'ACCELERATOR_ETHNORACIALIDENTITY_MODEL',
            },
        ),
        migrations.AddField(
            model_name='entrepreneurprofile',
            name='ethno_racial_identification',
            field=models.ManyToManyField(
                to=settings.ACCELERATOR_ETHNORACIALIDENTITY_MODEL
            ),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='ethno_racial_identification',
            field=models.ManyToManyField(
                to=settings.ACCELERATOR_ETHNORACIALIDENTITY_MODEL
            ),
        ),
        migrations.AddField(
            model_name='memberprofile',
            name='ethno_racial_identification',
            field=models.ManyToManyField(
                to=settings.ACCELERATOR_ETHNORACIALIDENTITY_MODEL
            ),
        ),
        migrations.AddField(
            model_name='entrepreneurprofile',
            name='authorization_to_share_ethno_racial_identity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='expertprofile',
            name='authorization_to_share_ethno_racial_identity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='memberprofile',
            name='authorization_to_share_ethno_racial_identity',
            field=models.BooleanField(default=False),
        ),
    ]
