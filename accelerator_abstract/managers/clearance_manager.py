# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.db import models
from accelerator_abstract.utils import build_case_statement
import logging

logger = logging.getLogger(__file__)


CLEARANCE_LOGGER_FAILURE_BASE_MSG = (
    "clearance_check failure: Failed attempted to access data protected by"
    "a clearance level.\nAttempting user: {user}.\nAttempted Program Family:"
    "{program_family}.\nRequired Level:{level}.\n"
)

CLEARANCE_LEVEL_DOES_NOT_EXIST_MSG = (
    "Permission Level with name \"{}\" does not exist.")


CLEARANCE_LOGGER_FAILED_INSUFFICIENT_CLEARANCE_MSG = (
    CLEARANCE_LOGGER_FAILURE_BASE_MSG + "Reason: Insufficient privileges."
)
CLEARANCE_LOGGER_SUCCESS_MSG = (
    "clearance_check success: {user} attempted to access "
    "{program_family} related data that requires a clearance of "
    "{level}, and was granted access.")

CLEARANCE_LOGGER_FAILED_BAD_CLEARANCE_MSG = (
    CLEARANCE_LOGGER_FAILURE_BASE_MSG + "Reason: Bad clearance level name."
)

NO_CLEARANCE_ERROR_MSG = ("User {user} does not have permission level "
                          "\"{level}\" for {program_family}.")

BOTTOM_CLEARANCE = 9999999
NO_SUCH_CLEARANCE = -1
CLEARANCE_LEVEL_EXEC_MD = "Exec/MD"
CLEARANCE_LEVEL_GLOBAL_MANAGER = "Global Manager"
CLEARANCE_LEVEL_POM = "Program Operations Manager"
CLEARANCE_LEVELS = [
    CLEARANCE_LEVEL_EXEC_MD,
    CLEARANCE_LEVEL_GLOBAL_MANAGER,
    CLEARANCE_LEVEL_POM,
]

CLEARANCE_LEVEL_ORDER = {level: i for i, level in enumerate(CLEARANCE_LEVELS)}


class ClearanceManager(models.Manager):
    def get_queryset(self):
        case_statement = build_case_statement(CLEARANCE_LEVEL_ORDER,
                                              attr_field="level",
                                              default_value=BOTTOM_CLEARANCE)
        return super(ClearanceManager, self).get_queryset().annotate(
            order=case_statement).order_by("program_family", "-order", "user")

    def clearances_for_user(self, user, level=CLEARANCE_LEVELS[-1]):
        level_order = _level_order(user, level, program_family=None)
        return self.get_queryset().filter(
            user=user, order__lte=level_order)

    def check_clearance(self, user, level, program_family=None):
        queryset = self.get_queryset()
        level_order = _level_order(user, level, program_family)
        filter_kwargs = {'user': user,
                         'order__lte': level_order}
        if program_family:
            filter_kwargs['program_family'] = program_family
        return queryset.filter(**filter_kwargs).exists()


def _level_order(user, level, program_family=None):
    level_order = CLEARANCE_LEVEL_ORDER.get(level)
    if level_order is None:
        logger.warn(CLEARANCE_LOGGER_FAILED_BAD_CLEARANCE_MSG.format(
            user=user,
            program_family=program_family or "none",
            level=level))
        return NO_SUCH_CLEARANCE
    return level_order
