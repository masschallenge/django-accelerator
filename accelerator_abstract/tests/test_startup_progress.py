from django.test import TestCase

from accelerator.tests.factories import (
    BusinessPropositionFactory,
    StartupFactory
)
from accelerator.models import BusinessProposition
from accelerator_abstract.models.base_startup import (
    APPLICATION_READY,
    PROFILE_COMPLETE,
)
from accelerator_abstract.models import EXCLUDED_FIELDS


class TestStartupProgress(TestCase):
    def _business_proposition_data(self):
        fields = BusinessProposition._meta.get_fields(include_parents=False)
        characters = 'text input characters'
        data = {}
        for field in fields:
            if field.name not in EXCLUDED_FIELDS:
                data[field.name] = characters
        return data

    def test_application_ready_milestone_with_incomplete_data(self):
        startup = StartupFactory()
        BusinessPropositionFactory(startup=startup)
        progress = startup.profile_status()
        self.assertEqual(progress['milestone'], APPLICATION_READY)
        self.assertFalse(progress['bus-prop-complete'])
        self.assertFalse(progress['profile-complete'])
        self.assertGreater(1, progress['progress'])

    def test_business_prop_complete_startup_profile_incomplete(self):
        startup = StartupFactory()
        business_prop_data = self._business_proposition_data()
        BusinessPropositionFactory(startup=startup, **business_prop_data)
        progress = startup.profile_status()
        self.assertEqual(progress['milestone'], APPLICATION_READY)
        self.assertTrue(progress['bus-prop-complete'])
        self.assertFalse(progress['profile-complete'])
        self.assertGreater(1, progress['progress'])

    def test_profile_application_field_complete_business_prop_incomplete(self):
        startup = StartupFactory(video_elevator_pitch_url='https://video.com')
        BusinessPropositionFactory(startup=startup)
        progress = startup.profile_status()
        self.assertEqual(progress['milestone'], PROFILE_COMPLETE)
        self.assertFalse(progress['bus-prop-complete'])
        self.assertFalse(progress['profile-complete'])
        self.assertGreater(1, progress['progress'])

    def test_milestone_change_when_required_field_complete(self):
        business_proposition_data = self._business_proposition_data()
        startup = StartupFactory(video_elevator_pitch_url='https://video.com')
        BusinessPropositionFactory(startup=startup,
                                   **business_proposition_data)
        progress = startup.profile_status()
        self.assertEqual(progress['milestone'], PROFILE_COMPLETE)
        self.assertTrue(progress['bus-prop-complete'])
        self.assertFalse(progress['profile-complete'])
        self.assertGreater(1, progress['progress'])

    def test_business_prop_complete_startup_profile_complete(self):
        business_proposition_data = self._business_proposition_data()
        startup = StartupFactory(video_elevator_pitch_url='https://video.com',
                                 high_resolution_logo='logo.jpg')
        BusinessPropositionFactory(startup=startup,
                                   **business_proposition_data)
        progress = startup.profile_status()
        self.assertEqual(progress['milestone'], PROFILE_COMPLETE)
        self.assertTrue(progress['bus-prop-complete'])
        self.assertTrue(progress['profile-complete'])
        self.assertEqual(1, progress['progress'])
