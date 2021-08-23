import swapper
from django.conf import settings
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
        max_length=500,
        blank=False,
        help_text='Partner Judging instructions to guide teams in 500 characters or less.')

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_partnerjudginginstructions'
        abstract = True
        verbose_name_plural = "instructions from a partner to guide teams in evaluating startups"
        unique_together = ('partner', 'judging_round')

    def __str__(self):
        return "%s added an instruction to %s judging round" % (self.partner, self.judging_round)
