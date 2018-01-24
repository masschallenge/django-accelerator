from collections import Counter
from django.db import models

import logging

logger = logging.getLogger(__file__)

MULTIPLE_ANSWERS_FOR_QUESTION_MSG = (
    "Found multiple answers for ApplicationQuestion %d on "
    "Application %d for startup %s")


class ApplicationAnswerQuerySet(models.QuerySet):

    def filter_one_answer_for_each_question(self, application, questions):
        """
        for each 2-tuple of (Application, ApplicationQuestion), keep only
        the first ApplicationAnswer, exclude the rest of the ApplicationAnswer
        instances. When more than one such ApplicationAnswer exists for a
        given 2-tuple, log it since it does not suppose to happen.
        """
        answer_set = self
        answers_counter = Counter(
            answer_set.values_list('application_question_id', flat=True))
        multi_answer_question_ids = [question_id for question_id in
                                     answers_counter if
                                     answers_counter[question_id] > 1]
        for question_id in multi_answer_question_ids:
            question = questions.get(id=question_id)
            _log_multiple_answers(application, question)

            answer_set = answer_set.exclude(id__in=_non_first_answers(
                application, question).values_list('id', flat=True))

        return answer_set


def _non_first_answers(application, question):
    qs = application.applicationanswer_set.filter(
        application_question=question)
    return qs.exclude(id=qs.first().id)


def _log_multiple_answers(application, question):
    logger.warn(MULTIPLE_ANSWERS_FOR_QUESTION_MSG % (
        question.question_number,
        application.id,
        application.startup.name))
