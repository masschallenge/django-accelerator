from accelerator.tests.factories import (
    CriterionFactory,
    CriterionOptionSpecFactory,
)
from accelerator.models import (
    FEEDBACK_DISPLAY_ENABLED,
    ONLINE_JUDGING_ROUND_TYPE,
    SUBMITTED_APP_STATUS,
)
from accelerator.tests.factories import (
    ApplicationFactory,
    ProgramCycleFactory,
)
from accelerator.tests.contexts import JudgingRoundContext


class CriterionOptionSpecContext:
    def __init__(self,
                 type="reads",
                 name="reads",
                 judging_round=None,
                 option="InterestinOption"):
        self.judging_round = judging_round
        self.cycle = ProgramCycleFactory()
        self.application = ApplicationFactory(
            application_status=SUBMITTED_APP_STATUS,
            application_type=self.cycle.default_application_type,
            cycle=self.cycle)
        self.application_type = self.application.application_type

        jr_kwargs = {
            'program__cycle': self.cycle,
            'round_type': ONLINE_JUDGING_ROUND_TYPE,
            'feedback_display': FEEDBACK_DISPLAY_ENABLED,
            'cycle_based_round': False,
            'application_type': self.application_type,
            'is_active': True,
        }

        if judging_round is None:
            self.judging_round = JudgingRoundContext(**jr_kwargs).judging_round

        self.criterion = CriterionFactory(
            type=type, name=name, judging_round=self.judging_round)
        self.criterion_option_spec = CriterionOptionSpecFactory(
            criterion=self.criterion,
            option=option
        )
