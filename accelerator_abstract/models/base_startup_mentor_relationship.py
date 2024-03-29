from __future__ import unicode_literals

import swapper
from django.conf import settings
from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

CONFIRMED_RELATIONSHIP = "Confirmed"
DESIRED_RELATIONSHIP = "Desired"
DISCUSSING_RELATIONSHIP = "In Discussions With"
RELATIONSHIP_CHOICES = ((CONFIRMED_RELATIONSHIP, CONFIRMED_RELATIONSHIP),
                        (DISCUSSING_RELATIONSHIP, DISCUSSING_RELATIONSHIP),
                        (DESIRED_RELATIONSHIP, DESIRED_RELATIONSHIP))


class BaseStartupMentorRelationship(AcceleratorModel):
    startup_mentor_tracking = models.ForeignKey(
        swapper.get_model_name(AcceleratorModel.Meta.app_label,
                               "StartupMentorTrackingRecord"),
        on_delete=models.CASCADE)
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    status = models.CharField(
        max_length=32,
        choices=RELATIONSHIP_CHOICES,
        default=DESIRED_RELATIONSHIP)
    primary = models.BooleanField(default=False)

    class Meta(AcceleratorModel.Meta):
        db_table = 'accelerator_startupmentorrelationship'
        abstract = True
        verbose_name_plural = 'Startup Mentor Relationships'

    def __str__(self):
        name = "Relationship of %s to %s" % (
            self.startup_mentor_tracking.startup.name,
            self.mentor.get_profile().full_name()
        )
        return name
