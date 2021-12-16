from swapper import get_model_name

from django.db.models import (
    BooleanField,
    CASCADE,
    ForeignKey,
)

from .accelerator_model import AcceleratorModel


class BasePartnerApplicationInterest(AcceleratorModel):
    partner = ForeignKey(
        get_model_name(AcceleratorModel.Meta.app_label,
                       "Partner"),
        on_delete=CASCADE)
    judging_round = ForeignKey(
        get_model_name(AcceleratorModel.Meta.app_label,
                       "JudgingRound"),
        on_delete=CASCADE)
    application = ForeignKey(
        get_model_name(AcceleratorModel.Meta.app_label,
                       "Application"),
        on_delete=CASCADE)
    advance_to_next_round = BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        abstract = True
        db_table = 'accelerator_partnerapplicationinterest'
        unique_together = (('partner', 'judging_round',
                            'application'),)

    def __repr__(self):
        return "PartnerApplicationInterest {} - {} - {}".format(
            self.partner.organization.name,
            self.application.startup.organization.name,
            self.judging_round.name
            )
