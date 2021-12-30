from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.accelerator_model import (
    AcceleratorModel,
    CHOICE_OPTION_HELP_TEXT
)

CHOICE_LAYOUT_HORIZONTAL = "horizontal"
CHOICE_LAYOUT_VERTICAL = "vertical"
CHOICE_LAYOUT_DROPDOWN = "dropdown"

CHOICE_LAYOUTS = ((CHOICE_LAYOUT_HORIZONTAL, 'Horizontal'),
                  (CHOICE_LAYOUT_VERTICAL, 'Vertical'),
                  (CHOICE_LAYOUT_DROPDOWN, 'Dropdown'))

QUESTION_TYPE_MULTILINE = "multiline"
QUESTION_TYPE_MULTICHOICE = "multichoice"
QUESTION_TYPE_NUMBER = "number"

QUESTION_TYPES = ((QUESTION_TYPE_MULTILINE, 'MultilineText'),
                  (QUESTION_TYPE_MULTICHOICE, 'MultipleChoice'),
                  (QUESTION_TYPE_NUMBER, 'Number'))


class BaseQuestion(AcceleratorModel):
    name = models.CharField(max_length=200)
    question_type = models.CharField(
        max_length=64,
        choices=QUESTION_TYPES,
    )
    choice_options = models.CharField(
        max_length=4000,
        blank=True,
        help_text=CHOICE_OPTION_HELP_TEXT
    )
    choice_layout = models.CharField(
        max_length=64,
        choices=CHOICE_LAYOUTS,
        blank=True,
    )

    class Meta(AcceleratorModel.Meta):
        abstract = True
        db_table = 'accelerator_question'
