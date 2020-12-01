from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

BLACK = 'Black'
EAST_SOUTHEAST_ASIAN = 'East and/or Southeast Asian'
HISPANIC_LATINX_SPANISH = 'Hispanic, Latinx, and/or Spanish'
INDIGENOUS = 'Indigenous'
HAWAIIAN_PACIFIC_POLYNESIAN = 'Native Hawaiian, Pacific Islander, or Polynesian'
MIDDLE_EASTERN_NORTH_AFRICAN = 'Middle Eastern and/or North African'
NORTH_CENTRAL_ASIAN = 'North and/or Central Asian'
SOUTH_ASIAN = 'South Asian'
WHITE_CAUCASIAN = 'White or Caucasian'
PREFER_NOT_TO_STATE = 'I prefer not to say'

ETHNO_RACIAL_IDENTITY_CHOICES = [
    (BLACK, 'e.g., African American, Haitian, Nigerian, Somali'),
    (EAST_SOUTHEAST_ASIAN, 'e.g., Chinese, Filipino, Korean, Indonesian'),
    (HISPANIC_LATINX_SPANISH, 'e.g., Brazilian, Colombian, Mexican, Nicaraguan'),
    (INDIGENOUS, 'e.g., Aboriginal, Inuit, Maasai, Native American'),
    (HAWAIIAN_PACIFIC_POLYNESIAN, 'Native Hawaiian, Pacific Islander, or Polynesian'),
    (MIDDLE_EASTERN_NORTH_AFRICAN, 'e.g., Egyptian, Emirati, Iranian, Moroccan'),
    (NORTH_CENTRAL_ASIAN, 'e.g., Kazakh, Siberian, Tajik, Uzbek'),
    (SOUTH_ASIAN, 'e.g., Bangladeshi, Indian, Pakistani, Sri Lankan'),
    (WHITE_CAUCASIAN, 'White or Caucasian'),
    (PREFER_NOT_TO_STATE, 'I prefer not to say'),
]


class BaseEthnoRacialIdentity(AcceleratorModel):
    identity = models.CharField(max_length=100,
                                blank=True,
                                null=True,
                                choices=ETHNO_RACIAL_IDENTITY_CHOICES)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_ethnoracialidentity'
        abstract = True
