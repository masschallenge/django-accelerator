from __future__ import unicode_literals

import swapper
from django.db import models
from sorl.thumbnail import ImageField

from accelerator_abstract.models.accelerator_model import AcceleratorModel

PARTNER_BADGE_DISPLAY_VALUES = (
    ('NONE', 'None'),
    ('PARTNER_LIST', 'Only on partner list'),
    ('PARTNER_PROFILE', 'Only on partner profile'),
    ('PARTNER_LIST_AND_PROFILE', 'Partner list and profile'))


class BaseProgramPartnerType(AcceleratorModel):
    program = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, "Program"),
        on_delete=models.CASCADE)
    partner_type = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    feature_in_footer = models.BooleanField(default=False)
    sort_order = models.IntegerField(
        blank=True,
        null=True)
    badge_image = ImageField(
        upload_to='badge_images',
        blank=True)
    badge_display = models.CharField(choices=PARTNER_BADGE_DISPLAY_VALUES,
                                     max_length=30, default="NONE")

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_programpartnertype'
        abstract = True
        verbose_name_plural = 'Program Partner Types'
        ordering = ['program', 'sort_order', ]

    def __str__(self):
        return "Partner type %s for %s" % (self.partner_type,
                                           self.program.name)
