from __future__ import unicode_literals

import swapper
from factory import SubFactory
from factory.django import DjangoModelFactory

from accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.tests.factories.startup_mentor_tracking_record_factory \
    import StartupMentorTrackingRecordFactory
from accelerator_abstract.models.base_startup_mentor_relationship import (
    CONFIRMED_RELATIONSHIP,
)

StartupMentorRelationship = swapper.load_model('accelerator',
                                               'StartupMentorRelationship')


class StartupMentorRelationshipFactory(DjangoModelFactory):
    class Meta:
        model = StartupMentorRelationship

    startup_mentor_tracking = SubFactory(StartupMentorTrackingRecordFactory)
    mentor = SubFactory(ExpertFactory)
    status = CONFIRMED_RELATIONSHIP
    primary = True
