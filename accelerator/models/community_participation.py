from django.db import models

from accelerator_abstract.models.accelerator_model import AcceleratorModel

PARTICIPATION_ROLE = 'PARTICIPATION_ROLE'
ADVISING_STARTUP_BUSINESS_AREA = 'ADVISING_STARTUP_BUSINESS_AREA'
ADVISING_STARTUP_SUPPORT_BELIEVE = 'ADVISING_STARTUP_SUPPORT_BELIEVE'

PARTICIPATION_CHOICES = (
    (PARTICIPATION_ROLE, PARTICIPATION_ROLE),
    (ADVISING_STARTUP_BUSINESS_AREA, ADVISING_STARTUP_BUSINESS_AREA),
    (ADVISING_STARTUP_SUPPORT_BELIEVE, ADVISING_STARTUP_SUPPORT_BELIEVE)
)


class CommunityParticipation(AcceleratorModel):
    name = models.TextField()
    description = models.TextField()
    sort_order = models.IntegerField()
    type = models.CharField(max_length=50,
                            default=PARTICIPATION_ROLE,
                            choices=PARTICIPATION_CHOICES)

    def __repr__(self):
        return 'Community Participation: {}'.format(self.name)
