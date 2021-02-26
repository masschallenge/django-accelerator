import swapper

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel
from accelerator_abstract.models.base_base_profile import USER_TYPES

DURATION_HELP_TEXT = ('Default deferment duration. Format: '
                      'days hours:minutes:seconds e.g 1 00:00:00')


class BaseDeferrableModal(AcceleratorModel):
    name = models.CharField(max_length=255,
                            default='',
                            help_text='Deferrable modal name')
    type = models.CharField(max_length=35,
                            default='',
                            help_text='Deferrable modal type')
    header = models.CharField(max_length=255,
                              default='',
                              help_text='Deferrable modal header text')
    submit_button = models.CharField(
        max_length=255,
        default='',
        help_text='Submit button text')
    defer_button = models.CharField(
        max_length=255,
        default='',
        help_text='Deferment button text')
    content = models.TextField(
        default='',
        help_text='Deferrable modal content. Use HTML for links.')
    duration = models.DurationField(
        blank=True,
        null=True,
        help_text=DURATION_HELP_TEXT)
    user_type = models.CharField(
        max_length=35,
        choices=USER_TYPES,
        blank=True,
        null=True, )
    user_role = models.ManyToManyField(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'UserRole'),
        blank=True, )
    program = models.ManyToManyField(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'Program'),
        blank=True, )
    program_family = models.ManyToManyField(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'ProgramFamily'),
        blank=True, )
    active_program = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        abstract = True
        verbose_name = 'Deferrable Modal'

    def __str__(self):
        return 'Deferrable Modal: {}'.format(self.name)
