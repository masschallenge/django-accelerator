from django.conf import settings
from django.db import models

CHOICE_OPTION_HELP_TEXT = (
    "Provide a list of options separated by a “|” (ie. Yes|No)"
)


class AcceleratorModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta(object):
        abstract = True
        app_label = 'accelerator'
        managed = settings.ACCELERATOR_MODELS_ARE_MANAGED

    def __str__(self):
        return self.name if hasattr(self, 'name') else str(self.id)
