from django.conf import settings

from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseUserNote(AcceleratorModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="user_notes",
                             on_delete=models.CASCADE)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name="manager_notes",
                                on_delete=models.CASCADE)
    note_content = models.TextField(default='',
                                    help_text='Note contents')

    class Meta(AcceleratorModel.Meta):
        abstract = True
        verbose_name = 'Staff Notes'

    def __str__(self):
        return 'User note for: {}'.format(self.user.email)
