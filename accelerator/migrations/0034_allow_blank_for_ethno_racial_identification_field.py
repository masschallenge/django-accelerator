from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0033_add_ethno_racial_identity_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genderchoices',
            options={'managed': True,
                     'ordering': ['name'],
                     'verbose_name': 'Gender Choice',
                     'verbose_name_plural': 'Gender Choices'
                     },
        ),
        migrations.AlterField(
            model_name='entrepreneurprofile',
            name='ethno_racial_identification',
            field=models.ManyToManyField(
                blank=True,
                to=settings.ACCELERATOR_ETHNORACIALIDENTITY_MODEL
            ),
        ),
        migrations.AlterField(
            model_name='expertprofile',
            name='ethno_racial_identification',
            field=models.ManyToManyField(
                blank=True,
                to=settings.ACCELERATOR_ETHNORACIALIDENTITY_MODEL
            ),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='ethno_racial_identification',
            field=models.ManyToManyField(
                blank=True,
                to=settings.ACCELERATOR_ETHNORACIALIDENTITY_MODEL
            ),
        ),
    ]
