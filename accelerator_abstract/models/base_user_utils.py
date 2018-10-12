# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from accelerator_abstract.models import BaseUserRole


def is_expert(user):
    return _has_user_type(user, "EXPERT")


def is_entrepreneur(user):
    return _has_user_type(user, "ENTREPRENEUR")


def is_member(user):
    return _has_user_type(user, "MEMBER")


def _has_user_type(obj, user_type):
    return (obj and
            getattr(obj, "baseprofile", None) and
            obj.baseprofile.user_type == user_type)


def is_employee(user):
    return (user.is_superuser or
            user.programrolegrant_set.filter(
                program_role__user_role__name=BaseUserRole.STAFF
            ).exists())
