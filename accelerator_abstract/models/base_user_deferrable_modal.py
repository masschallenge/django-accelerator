import swapper

from django.conf import settings
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseUserDeferrableModal(AcceleratorModel):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    deferrable_modal = models.ForeignKey(
        to=swapper.get_model_name(
            AcceleratorModel.Meta.app_label, 'DeferrableModal'),
        on_delete=models.CASCADE)
    is_deferred = models.BooleanField(default=False)
    deferred_to = models.DateTimeField(null=True, blank=True)

    class Meta(AcceleratorModel.Meta):
        abstract = True
        verbose_name = 'User Deferrable Modal'

    def __str__(self):
        return 'User Deferrable Modal: {}'.format(self.pk)
