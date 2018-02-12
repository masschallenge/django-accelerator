# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone

from accelerator.tests.factories import JudgingRoundFactory


class TestJudgingRound(TestCase):
    def test_str(self):
        judging_round = JudgingRoundFactory()
        assert judging_round.name in str(judging_round)

    def test_short_name(self):
        now = timezone.now()
        program_family_slug = 'Foo'
        judging_round = JudgingRoundFactory(
            program__program_family__url_slug=program_family_slug,
            end_date_time=now
        )
        short_name = judging_round.short_name()
        assert str(now.date().year) in short_name
        assert '{:02}'.format(now.date().month) in short_name
        assert judging_round.name in short_name
        assert program_family_slug.upper() in short_name

    def test_short_name_for_cycle_based_round(self):
        now = timezone.now()
        program_family_slug = 'Foo'
        judging_round = JudgingRoundFactory(
            program__program_family__url_slug=program_family_slug,
            end_date_time=now,
            cycle_based_round=True,
        )
        short_name = judging_round.short_name()
        assert str(now.date().year) in short_name
        assert '{:02}'.format(now.date().month) in short_name
        assert judging_round.name in short_name
        assert program_family_slug.upper() in short_name
