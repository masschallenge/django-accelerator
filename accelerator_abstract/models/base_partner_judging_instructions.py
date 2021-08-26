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
        max_length=1000,
        blank=False,
        help_text='Partner Judging instructions for judging rounds')

    class Meta(AcceleratorModel.Meta):
        abstract = True
        verbose_name_plural = "instructions from a partner"
        unique_together = ('partner', 'judging_round')

    def __str__(self):
        return "%s added instruction %s for %s " % (
            self.partner, self.instructions, self.judging_round)
