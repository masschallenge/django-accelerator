# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.conf import settings
import swapper
from django.db.models import (
    CASCADE,
    ForeignKey,
)
from .accelerator_model import AcceleratorModel


class BasePartnerJudgeApplicationAssignment(AcceleratorModel):
    judge = ForeignKey(settings.AUTH_USER_MODEL,
                       on_delete=CASCADE)
    application = ForeignKey(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, "Application"),
        on_delete=CASCADE)
    judging_round = ForeignKey(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, "JudgingRound"),
        on_delete=CASCADE)
    partner = ForeignKey(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, "Partner"),
        on_delete=CASCADE)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_partnerjudgeapplicationassignment'
        abstract = True
