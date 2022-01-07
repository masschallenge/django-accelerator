from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


def is_expert_validator(value):
    """Validate the provided value

    id must identify a User who has an ExpertProfile
    """
    ExpertProfile = swapper.load_model(AcceleratorModel.Meta.app_label,
                                       "ExpertProfile")
    if not ExpertProfile.objects.filter(user_id__exact=value).exists():
        raise ValidationError("User must be an expert")


class BaseExpertInterest(AcceleratorModel):
    """Relates a specific user, program family, and expert interest type

    Indicates that this user has this type of interest in serving for this
    program family
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="expert_interests",
        validators=[is_expert_validator, ],
        on_delete=models.CASCADE
    )
    program_family = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'ProgramFamily'),
        related_name="interested_experts",
        on_delete=models.CASCADE
    )
    interest_type = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               'ExpertInterestType'),
        related_name="interested_experts",
        on_delete=models.CASCADE
    )
    topics = models.TextField(
        blank=True,
        help_text="Please provide a list of topics of interest to yo"
    )

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_expertinterest'
        abstract = True
        verbose_name_plural = "Expert Interests"

    def __str__(self):
        msg = "{} interest by {} in the {} program family"
        return msg.format(
            self.interest_type,
            self.user,
            self.program_family
        )
