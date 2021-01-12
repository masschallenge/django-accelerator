import swapper
from django.db import migrations


ethno_racial_identity_list = [
    'Black', 'East and/or Southeast Asian',
    'Hispanic, Latinx, and/or Spanish', 'Indigenous',
    'Native Hawaiian, Pacific Islander, or Polynesian',
    'Middle Eastern and/or North African', 'North and/or Central Asian',
    'South Asian', 'White or Caucasian', 'I prefer not to say'
]


def add_ethno_racial_identity_data(*args, **kwargs):
    EthnoRacialIdentity = swapper.load_model(
        'accelerator', 'EthnoRacialIdentity'
    )
    for ethno_racial_identity in ethno_racial_identity_list:
        EthnoRacialIdentity.objects.create(identity=ethno_racial_identity)


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0032_add_ethno_racial_identity_model'),
    ]

    operations = [
        migrations.RunPython(add_ethno_racial_identity_data,
                             migrations.RunPython.noop)
    ]
