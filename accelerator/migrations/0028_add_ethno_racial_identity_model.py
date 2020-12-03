from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0027_add_birth_year_to_core_profile'),
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
