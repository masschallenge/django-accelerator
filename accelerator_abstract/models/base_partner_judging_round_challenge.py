from swapper import get_model_name

from django.db.models import (
    CASCADE,
    ForeignKey,
    TextField,
)

from .accelerator_model import AcceleratorModel

class BasePartnerJudgingRoundChallenge(AcceleratorModel):
    partner = ForeignKey(
        get_model_name(AcceleratorModel.Meta.app_label,
                       "Partner"),
        on_delete=CASCADE)
    judging_round = ForeignKey(
        get_model_name(AcceleratorModel.Meta.app_label,
                       "JudgingRound"),
        on_delete=CASCADE)
    text = TextField(blank=True,
                     null=True)
                                

    class Meta(AcceleratorModel.Meta):
        abstract = True
        verbose_name_plural = 'Partner Judging Round Challenges'
        db_table = 'accelerator_partnerjudgingroundchallenge'
