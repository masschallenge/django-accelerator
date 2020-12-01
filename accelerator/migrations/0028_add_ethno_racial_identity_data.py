import swapper
from django.db import migrations

from accelerator_abstract.models.base_ethno_racial_identity import (
    ETHNO_RACIAL_IDENTITY_CHOICES,
)


def add_ethno_racial_identity_data(*args, **kwargs):
    EthnoRacialIdentity = swapper.load_model(
        'accelerator', 'EthnoRacialIdentity'
    )
    for ethno_racial_identity in ETHNO_RACIAL_IDENTITY_CHOICES:
        EthnoRacialIdentity.objects.create(identity=ethno_racial_identity[0])


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0027_add_ethno_racial_identity_model'),
    ]

    operations = [
        migrations.RunPython(add_ethno_racial_identity_data,
                             migrations.RunPython.noop)
    ]
