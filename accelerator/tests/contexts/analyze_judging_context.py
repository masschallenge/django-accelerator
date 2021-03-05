from accelerator.tests.factories import (
    CriterionFactory,
    CriterionOptionSpecFactory,
)
from accelerator.tests.contexts.judge_feedback_context import (
    JudgeFeedbackContext,
)
from accelerator.models import JUDGING_FEEDBACK_STATUS_COMPLETE

import swapper


JudgeApplicationFeedback = swapper.load_model(
    'accelerator', 'JudgeApplicationFeedback')


class AnalyzeJudgingContext(JudgeFeedbackContext):
    def __init__(self,
                 type="reads",
                 name="reads",
                 read_count=1,
                 options=[""],
                 is_active=True,
                 judge_capacity=10,
                 add_application=True):
        super().__init__(is_active=is_active,
                         judge_capacity=judge_capacity)
        self.read_count = read_count
        self.options = options
        self.feedback.feedback_status = JUDGING_FEEDBACK_STATUS_COMPLETE
        self.feedback.save()
        if add_application:
            self.add_application()
        self.criterion = CriterionFactory(type=type,
                                          name=name,
                                          judging_round=self.judging_round)
        self.option_specs = [CriterionOptionSpecFactory(
            criterion=self.criterion,
            count=read_count,
            option=option) for option in options]

    def needed_reads(self):
        return self.total_reads_required() - self.feedback_count()

    def total_reads_required(self):
        return self.read_count * len(self.applications)

    def feedback_count(self):
        counts = [JudgeApplicationFeedback.objects.filter(
            application=app,
            feedback_status=JUDGING_FEEDBACK_STATUS_COMPLETE).count()
            for app in self.applications]
        return sum([min(self.read_count, count)
                    for count in counts])
