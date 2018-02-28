# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from django.test import TestCase

from .factories.job_posting_factory import JobPostingFactory


class TestJobPosting(TestCase):
    def test_job_posting(self):
        posting = JobPostingFactory()
        self.assertTrue(posting.title in str(posting))
        self.assertTrue(posting.startup.organization.name in str(posting))
