# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.db import models
@python_2_unicode_compatible
class BaseProgramPartner(AcceleratorModel):
    program = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"))
    partner = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "Partner"))
    partner_type = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "ProgramPartnerType"))
    description = models.TextField(
        max_length=2000,
        blank=True,
        help_text='This is the description of the Partner '
        'SPECIFICALLY IN THE CONTEXT OF THE PROGRAM. '
        '(Distinct from the generic description of the Partner.) '
        'For example, description of In-Kind sponsorship deals specific '
        'to a Program would go here.')

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_programpartner'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = 'Program Partner'
        ordering = ['program__name', 'partner_type__sort_order', 'partner', ]

    def __str__(self):
        return "%s Partner %s from %s" % (self.partner_type.partner_type,
                                           self.partner.name,
                                           self.program.name)
