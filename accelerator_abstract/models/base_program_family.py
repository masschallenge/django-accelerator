from __future__ import unicode_literals
import swapper
from django.db.models import (
    BooleanField,
    SET_NULL,
    CharField,
    EmailField,
    ForeignKey,
    TextField,
)

from accelerator_abstract.models.accelerator_model import AcceleratorModel


class BaseProgramFamily(AcceleratorModel):
    """An association of related programs."""

    name = CharField(max_length=128)
    short_description = TextField(
        blank=True,
        help_text="You may use HTML, including links",
    )
    url_slug = CharField(
        max_length=30,
        default="",
    )
    email_domain = CharField(
        max_length=30,
        default="",
        help_text="Base domain for role-based email"
    )
    phone_number = CharField(
        max_length=30,
        default="",
        help_text="Phone number for this program (local form)"
    )
    home_community = ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label, 'Community'),
        verbose_name='home community', blank=True, null=True,
        on_delete=SET_NULL)
    office_hour_bcc = EmailField(
        max_length=100,
        blank=True,
        null=True,
        help_text="An email address to bcc whenever office hours"
                  " are created, deleted, or modified in this program family"
    )
    is_open_for_startups = BooleanField(
        default=False,
        help_text="Whether this ProgramFamily should be available to"
                  " entrepreneurs"
    )
    is_open_for_experts = BooleanField(
        default=False,
        help_text="Whether this ProgramFamily should be available to"
                  " experts"
    )

    class Meta(AcceleratorModel.Meta):
        verbose_name_plural = "program families"
        db_table = 'accelerator_programfamily'
        abstract = True
