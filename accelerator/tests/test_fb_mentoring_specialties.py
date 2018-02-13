# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase

from accelerator.tests.factories.mentoring_specialties_factory import (
    MentoringSpecialtiesFactory,
)


class TestMentoringSpecialties(TestCase):

    def test_create(self):
        specialties = MentoringSpecialtiesFactory()
        self.assertTrue("Mentoring Specialties" in specialties.name)
