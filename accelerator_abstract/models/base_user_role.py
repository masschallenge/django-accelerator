# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db.models import (
    CharField,
    PositiveIntegerField,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseUserRole(AcceleratorModel):
    # Known User Roles
    ACTIVE_JUDGE = "Active Judge"
    ALUM = "Alum"
    ALUM_MENTOR = "Alum Mentor"
    AIR = "Alumni in Residence"
    MENTOR = "Mentor"
    DESIRED_JUDGE = "Desired Judge"
    DESIRED_MENTOR = "Desired Mentor"
    FINALIST = "Finalist"
    JUDGE = "Judge"
    OFFICE_HOUR_HOLDER = "Office Hour Holder"
    PARTNER = "Partner"
    PARTNER_ADMIN = "Partner Admin"
    PROCTOR = "Proctor"
    SENIOR_JUDGE = "Senior Judge"
    STAFF = "Staff"
    TEAM = "Team"

    OFFICE_HOUR_ROLES = set([AIR,
                             PARTNER,
                             PARTNER_ADMIN,
                             OFFICE_HOUR_HOLDER,
                             MENTOR])

    FINALIST_USER_ROLES = [FINALIST,
                           AIR,
                           STAFF]

    name = CharField(max_length=255)
    url_slug = CharField(max_length=30)
    sort_order = PositiveIntegerField()

    class Meta(AcceleratorModel.Meta):
        abstract = True
        db_table = '{}_userrole'.format(AcceleratorModel.Meta.app_label)
