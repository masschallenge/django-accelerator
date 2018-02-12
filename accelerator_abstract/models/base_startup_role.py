# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db.models import CharField

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseStartupRole(AcceleratorModel):
    # Known Startup Roles
    FINALIST = "Finalist"
    ENTRANT = "Entrant"
    FAST_TRACK = "Fast Track"
    AIR = "Alum In Residence"
    MC_STAFF = "MC Staff"

    FINALIST_STARTUP_ROLES = [FINALIST,
                              AIR,
                              MC_STAFF]

    name = CharField(max_length=255)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_startuprole'.format(AcceleratorModel.Meta.app_label)
        abstract = True
