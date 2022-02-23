from __future__ import unicode_literals

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseLegalCheck(AcceleratorModel):
    name = models.CharField(max_length=128,
                            default='',
                            null=False,
                            blank=False,
                            unique=True,
                            help_text='Internal name for this check.')
    description = models.TextField(
        help_text='Text displayed next to checkbox. Use HTML for links.')
    is_enabled_for_experts = models.BooleanField(
        default=True,
        help_text='This legal check is for Experts (Judges and Mentors)')
    is_enabled_for_entrepreneurs = models.BooleanField(
        default=True,
        help_text='This legal check is for Entrepreneurs (people with '
                  'Startups applying to MassChallenge)')
    is_enabled_for_unified_profile = models.BooleanField(
        default=False,
        help_text='This legal check is only available for users with '
                  'unified profiles. (Neither Experts nor Entrepreneurs)',
    )

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_legalcheck'
        abstract = True
        verbose_name = "Legal Check"

    def __str__(self):
        return 'Legal Check: {}'.format(self.name)
