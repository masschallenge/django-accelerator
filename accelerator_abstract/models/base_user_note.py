from django.conf import settings

from django.db import models

from accelerator_abstract.models.base_note import BaseNote


class BaseUserNote(BaseNote):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name="user_notes",
                             on_delete=models.CASCADE)

    class Meta(BaseNote.Meta):
        abstract = True
        verbose_name = 'User note'

    def __str__(self):
        return 'User note for: {}'.format(self.user.email)
