from django.conf import settings

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseNote(AcceleratorModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    note_content = models.TextField(default='',
                                    help_text='Note contents')

    class Meta(AcceleratorModel.Meta):
        abstract = True
