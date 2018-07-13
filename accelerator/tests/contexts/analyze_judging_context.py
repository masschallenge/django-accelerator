from accelerator.tests.factories import (
    CriterionFactory,
    CriterionOptionSpecFactory,
)
from accelerator.tests.contexts.judge_feedback_context import (
    JudgeFeedbackContext,
)
from accelerator.models import (
    JUDGING_FEEDBACK_STATUS_COMPLETE,
    JudgeApplicationFeedback,
)


class AnalyzeJudgingContext(JudgeFeedbackContext):
    def __init__(self, type, name, read_count, options):
        super().__init__()
        self.read_count = read_count
        self.options = options
        self.feedback.feedback_status = JUDGING_FEEDBACK_STATUS_COMPLETE
        self.feedback.save()
        self.add_application()  # Add unread app
        self.criterion = CriterionFactory(type=type,
                                          name=name,
                                          judging_round=self.judging_round)
        self.option_specs = [CriterionOptionSpecFactory(
            criterion=self.criterion,
            count=read_count,
            option=option) for option in options]

    def needed_reads(self):
        return (self.read_count * len(self.applications) -
                self.feedback_count())

    def feedback_count(self):
        counts = [JudgeApplicationFeedback.objects.filter(
            application=app,
            feedback_status=JUDGING_FEEDBACK_STATUS_COMPLETE).count()
                  for app in self.applications]
        return sum([min(self.read_count, count)
                    for count in counts])
