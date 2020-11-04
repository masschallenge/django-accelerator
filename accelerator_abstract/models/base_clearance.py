# MIT License
# Copyright (c) 2018 MassChallenge, Inc.

from __future__ import unicode_literals

import logging
import swapper
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel

logger = logging.getLogger(__file__)


CLEARANCE_LEVEL_EXEC_MD = "Exec/MD"
CLEARANCE_LEVEL_GLOBAL_MANAGER = "Global Manager"
CLEARANCE_LEVEL_POM = "Program Operations Manager"
CLEARANCE_LEVEL_STAFF = "Staff"

CLEARANCE_LEVELS = [
    CLEARANCE_LEVEL_EXEC_MD,
    CLEARANCE_LEVEL_GLOBAL_MANAGER,
    CLEARANCE_LEVEL_POM,
    CLEARANCE_LEVEL_STAFF,
]

CLEARANCE_LEVEL_CHOICES = [(x, x) for x in CLEARANCE_LEVELS]
CLEARANCE_FORMAT_STR = "Clearance {level} at {program_family} for {user}"
CLEARANCE_LOGGER_FAILURE_BASE_MSG = (
    "clearance_check failure: Failed attempted to access data protected by "
    "a clearance level.\nAttempting user: {user}.\nAttempted Program Family: "
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

CLEARANCE_LEVEL_ORDER = {level: i for i, level in enumerate(CLEARANCE_LEVELS)}


class ClearanceManager(models.Manager):
    def get_queryset(self):
        case_statement = build_case_statement(CLEARANCE_LEVEL_ORDER,
                                              attr_field="level",
                                              default_value=BOTTOM_CLEARANCE)
        return super(ClearanceManager, self).get_queryset().annotate(
            order=case_statement).order_by("program_family", "-order", "user")

    def clearances_for_user(self, user, level=CLEARANCE_LEVELS[-1]):
        level_rank = _level_rank(user, level, program_family=None)
        return self.get_queryset().filter(user=user, order__lte=level_rank)

    def check_clearance(self, user, level, program_family=None):
        queryset = self.get_queryset()
        level_rank = _level_rank(user, level, program_family)
        filter_kwargs = {'user': user, 'order__lte': level_rank}
        if program_family:
            filter_kwargs['program_family'] = program_family
        return queryset.filter(**filter_kwargs).exists()


def _level_rank(user, level, program_family=None):
    level_rank = CLEARANCE_LEVEL_ORDER.get(level)
    if level_rank is None:
        logger.warning(CLEARANCE_LOGGER_FAILED_BAD_CLEARANCE_MSG.format(
            user=user,
            program_family=program_family or "none",
            level=level))
        return NO_SUCH_CLEARANCE
    return level_rank


@python_2_unicode_compatible
class BaseClearance(AcceleratorModel):
    objects = ClearanceManager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=False,
                             blank=False,
                             related_name="clearances",
                             on_delete=models.CASCADE)
    level = models.CharField(choices=CLEARANCE_LEVEL_CHOICES,
                             null=False,
                             blank=False,
                             max_length=64)
    program_family = models.ForeignKey(swapper.get_model_name(
        AcceleratorModel.Meta.app_label, "ProgramFamily"),
        null=False,
        blank=False,
        related_name="user_clearances",
        on_delete=models.CASCADE)

    class Meta(AcceleratorModel.Meta):
        unique_together = ("user", "program_family")
        abstract = True
        db_table = "accelerator_clearance".format(
            AcceleratorModel.Meta.app_label)

    def __str__(self):
        return CLEARANCE_FORMAT_STR.format(level=self.level,
                                           program_family=self.program_family,
                                           user=self.user)


# Copied from accelerate/mcproject/mc/utils.py
def build_case_statement(cases_dict,
                         attr_field,
                         default_value=None,
                         output_field=models.IntegerField()):
    cases = [models.When(**{attr_field: key, 'then': models.Value(value)})
             for key, value in cases_dict.items()]
    case_statement = models.Case(default=models.Value(default_value),
                                 output_field=output_field)
    case_statement.cases = cases
    return case_statement
