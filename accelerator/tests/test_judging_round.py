from __future__ import unicode_literals

from django.test import TestCase
from accelerator.tests.factories import (
    JudgingRoundFactory,
    ProgramFactory,
)


class TestJudgingRound(TestCase):
    def test_str(self):
        judging_round = JudgingRoundFactory()
        assert judging_round.name in str(judging_round)

    def test_short_name(self):
        program_family_slug = 'Foo'
        judging_round = JudgingRoundFactory(
            program__program_family__url_slug=program_family_slug,
        )
        end_date_time = judging_round.end_date_time
        short_name = judging_round.short_name()
        assert str(end_date_time.date().year) in short_name
        assert '{:02}'.format(end_date_time.date().month) in short_name
        assert judging_round.name in short_name
        assert program_family_slug.upper() in short_name

    def test_short_name_for_cycle_based_round(self):
        program_family_slug = 'Foo'
        judging_round = JudgingRoundFactory(
            program__program_family__url_slug=program_family_slug,
            cycle_based_round=True,
        )
        short_name = judging_round.short_name()
        end_date_time = judging_round.end_date_time
        assert str(end_date_time.date().year) in short_name
        assert '{:02}'.format(end_date_time.date().month) in short_name
        assert judging_round.name in short_name
        assert program_family_slug.upper() in short_name

    def test_display_name_shows_requested_program(self):
        program_family_slug = 'Foo'
        judging_round = JudgingRoundFactory(
            program__program_family__url_slug=program_family_slug,
            cycle_based_round=True, )
        second_slug = "Bar"
        second_program = ProgramFactory(cycle=judging_round.program.cycle,
                                        program_family__url_slug=second_slug)
        display_name = judging_round.display_name(program=second_program)
        end_date_time = judging_round.end_date_time
        assert str(end_date_time.date().year) in display_name
        assert '{:02}'.format(end_date_time.date().month) in display_name
        assert judging_round.name in display_name
        assert second_slug.upper() in display_name
        assert program_family_slug.upper() not in display_name

    def test_program_family_abbr_returns_only_program_specified(self):
        program_family_slug = 'Foo'
        judging_round = JudgingRoundFactory(
            program__program_family__url_slug=program_family_slug,
            cycle_based_round=True, )
        second_slug = "Bar"
        second_program = ProgramFactory(cycle=judging_round.program.cycle,
                                        program_family__url_slug=second_slug)
        family_abbr = judging_round.program_family_abbrs(
            program=second_program)
        assert family_abbr == second_program.family_abbr()
