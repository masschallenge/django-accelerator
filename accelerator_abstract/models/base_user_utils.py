from __future__ import unicode_literals
from accelerator_abstract.models import (
    CLEARANCE_LEVEL_STAFF,
)


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


def has_staff_clearance(user):
    return user.clearances.check_clearance(user, CLEARANCE_LEVEL_STAFF)


def is_employee(user):
    if user.is_anonymous:
        return False
    if user.is_superuser:
        return True

    return has_staff_clearance(user)
