from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseStartupTeamMember(AcceleratorModel):
    startup = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Startup"),
        on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=60, blank=True)
    startup_administrator = models.BooleanField(
        help_text='You have to have at least one administrator')
    is_contact = models.BooleanField(
        default=False,
        help_text='A secondary contact for the startup')
    primary_contact = models.BooleanField(
        default=False,
        help_text='You may only have one primary contact')
    technical_contact = models.BooleanField(default=False)
    marketing_contact = models.BooleanField(default=False)
    financial_contact = models.BooleanField(default=False)
    legal_contact = models.BooleanField(default=False)
    product_contact = models.BooleanField(default=False)
    design_contact = models.BooleanField(default=False)
    display_on_public_profile = models.BooleanField(default=True)
    founder = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_startupteammember'
        abstract = True
        unique_together = ('startup', 'user')
        verbose_name_plural = 'Startup Team Members'

    def __str__(self):
        return "%s of %s" % (str(self.user), str(self.startup))
