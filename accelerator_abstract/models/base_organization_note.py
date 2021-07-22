import swapper
from django.db import models

from accelerator_abstract.models.base_note import BaseNote


class BaseOrganizationNote(BaseNote):
    organization = models.ForeignKey(
        swapper.get_model_name(BaseNote.Meta.app_label, 'Organization'),
        related_name="organization_notes",
        on_delete=models.CASCADE)

    class Meta(BaseNote.Meta):
        abstract = True
        verbose_name = 'Organization note'

    def __str__(self):
        return 'Organization note for: {}'.format(self.organization.name)
