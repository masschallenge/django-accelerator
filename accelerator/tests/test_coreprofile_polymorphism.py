from unittest import TestCase

from accelerator.models import (
    CoreProfile,
    EntrepreneurProfile,
    ExpertProfile,
)
from accelerator.tests.factories import (
    ExpertFactory,
    EntrepreneurFactory,
)


class TestCoreProfilePolymorphism(TestCase):

    def test_get_all_profile_types(self):
        expert = ExpertFactory()
        expertprofile = expert.get_profile()
        entrepreneur = EntrepreneurFactory()
        entrepreneurprofile = entrepreneur.get_profile()
        expected = sorted([expertprofile.pk, entrepreneurprofile.pk])
        results = CoreProfile.objects.all().values_list('id', flat=True)
        self.assertEqual(sorted(results), expected)

    def test_get_only_expert_profile_type(self):
        expert = ExpertFactory()
        expertprofile = expert.get_profile()
        EntrepreneurFactory()
        expert = CoreProfile.objects.instance_of(
            ExpertProfile).last()
        self.assertEqual(expert.pk, expertprofile.pk)

    def test_get_only_entrepreneur_profile_type(self):
        entrepreneur = EntrepreneurFactory()
        entrepreneurprofile = entrepreneur.get_profile()
        ExpertFactory()
        entrepreneur = CoreProfile.objects.instance_of(
            EntrepreneurProfile).last()
        self.assertEqual(entrepreneur.pk, entrepreneurprofile.pk)
