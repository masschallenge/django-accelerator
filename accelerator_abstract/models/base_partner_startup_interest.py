from swapper import get_model_name

from django.db.models import (
    CASCADE,
    ForeignKey,
)

from .accelerator_model import AcceleratorModel


class BasePartnerStartupInterest(AcceleratorModel):
    partner = ForeignKey(
        get_model_name(AcceleratorModel.Meta.app_label,
                       "Partner"),
        on_delete=CASCADE)
    judging_round = ForeignKey(
        get_model_name(AcceleratorModel.Meta.app_label,
                       "JudgingRound"),
        on_delete=CASCADE)
    startup = ForeignKey(
        get_model_name(AcceleratorModel.Meta.app_label,
                       "Startup"),
        on_delete=CASCADE)

    class Meta(AcceleratorModel.Meta):
        abstract = True
        db_table = 'accelerator_partnerstartupinterest'
