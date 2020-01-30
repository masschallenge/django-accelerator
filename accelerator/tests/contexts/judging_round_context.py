from accelerator.tests.factories import (
    JudgingFormFactory,
    JudgingFormElementFactory,
    JudgingRoundFactory,
)
from accelerator_abstract.models import FORM_ELEM_OVERALL_RECOMMENDATION

class JudgingRoundContext:
    def __init__(self, **kwargs):
        if kwargs.get("is_active") is True:
            should_be_active = True
            kwargs["is_active"] = False
        else:
            should_be_active = False
        self.judging_round = JudgingRoundFactory(**kwargs)
        if should_be_active:
            self.activate_judging_round()


    def activate_judging_round(self):
        self.judging_form = self.prepare_judging_form()
        self.judging_round.judging_form = self.judging_form
        self.judging_round.is_active=True
        self.judging_round.save()
        

    def prepare_judging_form(self):
        judging_form = JudgingFormFactory()
        JudgingFormElementFactory(
            element_name=FORM_ELEM_OVERALL_RECOMMENDATION,
            form_type=judging_form)
        return judging_form


            
