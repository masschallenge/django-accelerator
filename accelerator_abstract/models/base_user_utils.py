# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.contrib.auth import get_user_model
from django.db.models import Q
from judging_round import (
    JudgingRound,
    RECRUIT_ANYONE,
    RECRUIT_APPROVED_ONLY,
)
from user_role import UserRole
from program_role import ProgramRole
from program import ACTIVE_PROGRAM_STATUS


def _has_user_type(obj, user_type):
    return (obj and
            getattr(obj, "baseprofile", None) and
            obj.baseprofile.user_type == user_type)


def is_expert(user):
    return _has_user_type(user, "EXPERT")


def is_entrepreneur(user):
    return _has_user_type(user, "ENTREPRENEUR")


def is_member(user):
    return _has_user_type(user, "MEMBER")


def current_mentor_roles():
    return ProgramRole.objects.filter(
        program__program_status=ACTIVE_PROGRAM_STATUS,
        user_role__name=UserRole.MENTOR)


def current_mentor_filter():
    return Q(programrolegrant__program_role__in=current_mentor_roles())


def current_office_hour_holder_roles():
    return ProgramRole.objects.filter(
        program__program_status=ACTIVE_PROGRAM_STATUS,
        user_role__name=UserRole.OFFICE_HOUR_HOLDER)


def current_office_hours_filter():
    return Q(
        programrolegrant__program_role__in=current_office_hour_holder_roles())


def get_office_hour_holder_users():
    """return all users who could be office-hour holders

    This means any person who _is_ a mentor or _is_ a partner
    team member
    """
    mentor_q = current_mentor_filter()
    partner_team_member_q = ~Q(partnerteammember__exact=None)
    current_air_roles = ProgramRole.objects.filter(
        program__program_status=ACTIVE_PROGRAM_STATUS,
        user_role__name=UserRole.AIR)
    air_q = Q(programrolegrant__program_role__in=current_air_roles)
    office_hours_q = current_office_hours_filter()

    qs = get_user_model().objects.filter(
        mentor_q |
        partner_team_member_q |
        air_q |
        office_hours_q)
    return qs.distinct().order_by('last_name', 'first_name')


def recruiting_rounds(user):
    recruiting_approved = Q(recruit_judges=RECRUIT_APPROVED_ONLY)
    approved = Q(desired_judge_label__in=user.userlabel_set.all())
    recruiting_any = Q(recruit_judges=RECRUIT_ANYONE)
    return JudgingRound.objects.filter(
        (recruiting_approved & approved) |
        recruiting_any).order_by('start_date_time', 'name')


def active_judging_rounds(user):
    active = Q(is_active=True)
    confirmed = Q(confirmed_judge_label__in=user.userlabel_set.all())
    return JudgingRound.objects.filter(
        active & confirmed).order_by('start_date_time', 'name')


def users_by_program_roles(program_roles):
    return get_user_model().objects.filter(
        programrolegrant__program_role__in=program_roles)


def users_by_user_roles(user_roles):
    return get_user_model().objects.filter(
        programrolegrant__program_role__user_role__in=user_roles)


def finalist_users(program=None):
    user_set = users_by_program_roles(program.finalist_roles())
    return user_set.order_by('last_name', 'first_name')


def partner_name(expert):
    if expert.partnerteammember_set.count() > 0:
        return ", ".join(member.partner.name
                         for member in expert.partnerteammember_set.all())
    if expert.startupteammember_set.count() > 0:
        return ", ".join(member.startup.name
                         for member in expert.startupteammember_set.all())
    if is_expert(expert):
        return expert.get_profile().company
    return ""


def startup_name(finalist):
    return ", ".join("%s (%s)" % (member.startup.name, member.startup.id)
                     for member in finalist.startupteammember_set.all())
