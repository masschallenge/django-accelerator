# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import swapper

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from django.conf import settings
from django.db import models


@python_2_unicode_compatible
class BasePartnerTeamMember(AcceleratorModel):
    partner = models.ForeignKey(swapper.get_model_name(AcceleratorModel.Meta.app_label, "Partner"))
    team_member = models.ForeignKey(settings.AUTH_USER_MODEL)
    partner_administrator = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        db_table = '{}_partnerteammember'.format(
            AcceleratorModel.Meta.app_label)
        abstract = True
        verbose_name_plural = 'Partner Team Members'
        ordering = ['team_member__last_name', 'team_member__first_name', ]
        unique_together = ('partner', 'team_member')

    def __str__(self):
        return "Member %s from %s" % (self.team_member,
                                       self.partner.name)
