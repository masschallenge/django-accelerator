import swapper
from django.db import models

from .accelerator_model import AcceleratorModel


class BasePartnerJudgingInstructions(AcceleratorModel):
    partner = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "Partner"),
        on_delete=models.CASCADE)
    judging_round = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "JudgingRound"),
        on_delete=models.CASCADE)
    instructions = models.TextField(
        blank=False,
        help_text='Partner Judging instructions for judging rounds')

    class Meta(AcceleratorModel.Meta):
        abstract = True
        verbose_name_plural = "instructions from a partner"
        unique_together = ('partner', 'judging_round')
