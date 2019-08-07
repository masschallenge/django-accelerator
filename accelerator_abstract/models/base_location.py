from __future__ import unicode_literals

from django.db.models import (
    CharField,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseLocation(AcceleratorModel):
    name = CharField(max_length=100, blank=False)
    city = CharField(max_length=100, blank=True, default='')
    state = CharField(max_length=100, blank=True, default='')
    country = CharField(max_length=100, blank=True, default='')
    postcode = CharField(max_length=20, blank=True, default='')
    latitude = CharField(max_length=100, blank=True, default='')
    longitude = CharField(max_length=100, blank=True, default='')
    timezone = CharField(
        max_length=35,
        blank=False,
        default="UTC",
        help_text=("Timezone name from Olson Timezone database "
                   "(https://en.wikipedia.org/wiki/Tz_database)")
    )

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = "locations"
        db_table = '{}_location'.format(AcceleratorModel.Meta.app_label)
        abstract = True
