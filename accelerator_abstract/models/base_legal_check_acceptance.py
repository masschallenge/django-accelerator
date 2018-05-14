# MIT License
# Copyright (c) 2017 MassChallenge, Inc.
# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from accelerator_abstract.models.accelerator_model import AcceleratorModel


@python_2_unicode_compatible
class BaseLegalCheckAcceptance(AcceleratorModel):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='legalcheck_set')
    legal_check = models.ForeignKey(
        to=swapper.get_model_name(AcceleratorModel.Meta.app_label,
                                  'LegalCheck'),
        related_name='user_set')
    accepted = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_legalcheckacceptance'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name = 'Legal Check Acceptance'
        unique_together = ('user', 'legal_check')

    def __str__(self):
        return '{} {}accepted by {}'.format(self.legal_check,
                                            '' if self.accepted else "not ",
                                            self.user.full_name())
