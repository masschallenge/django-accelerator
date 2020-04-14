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

    name = CharField(max_length=255,
                     unique=True)
    sort_order = PositiveIntegerField()

    class Meta(AcceleratorModel.Meta):
        abstract = True
        db_table = '{}_userrole'.format(AcceleratorModel.Meta.app_label)


def has_user_role_base(
        user, user_role_name, program=None,
        inactive_programs=False, active_or_ended_programs=False):
    filter = user.programrolegrant_set.filter(
        program_role__user_role__name=user_role_name)
    if program:
        filter = filter.filter(program_role__program=program)
    if not inactive_programs:
        filter = filter.filter(program_role__program__program_status__in=[
            "active", "upcoming"])
    elif active_or_ended_programs:
        filter = filter.filter(program_role__program__program_status__in=[
            "active", "ended"])
    return filter.exists()


def is_finalist_user(user, program=None, inactive_programs=False):
    return has_user_role_base(
        user, BaseUserRole.FINALIST, program, inactive_programs)


def is_mentor(user, program=None, inactive_programs=False):
    return has_user_role_base(
        user, BaseUserRole.MENTOR, program, inactive_programs)


def is_judge(user, program=None, inactive_programs=False):
    return has_user_role_base(
        user, BaseUserRole.JUDGE, program, inactive_programs)


def has_user_roles(user, roles=None):
    return user.programrolegrant_set.filter(
        program_role__user_role__name__in=roles).exists()
