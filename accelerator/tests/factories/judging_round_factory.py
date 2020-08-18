# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.apps import AcceleratorConfig
from accelerator.models import (
    CAPTURE_AVAILABILITY_DISABLED,
    FEEDBACK_DISPLAY_DISABLED,
    IN_PERSON_JUDGING_ROUND_TYPE,
    RECRUIT_NONE,
)
from accelerator.tests.factories.application_type_factory import (
    ApplicationTypeFactory
)
from accelerator.tests.factories.judging_form_factory import (
    JudgingFormFactory
)
from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.startup_label_factory import (
    StartupLabelFactory
)
from accelerator.tests.factories.user_label_factory import UserLabelFactory
from accelerator.tests.utils import months_from_now
from accelerator_abstract.models.base_judging_round import (
    DEFAULT_BUFFER_BEFORE_EVENT,
    SCENARIO_DETECTION,
)

JudgingRound = swapper.load_model(AcceleratorConfig.name, 'JudgingRound')


class JudgingRoundFactory(DjangoModelFactory):
    class Meta:
        model = JudgingRound

    program = SubFactory(ProgramFactory)
    cycle_based_round = False
    name = Sequence(lambda n: "Judging Round {0}".format(n))
    start_date_time = months_from_now(1)
    end_date_time = months_from_now(2)
    is_active = False
    round_type = IN_PERSON_JUDGING_ROUND_TYPE
    allow_dynamic_allocation = False
    application_type = SubFactory(ApplicationTypeFactory)
    buffer_before_event = DEFAULT_BUFFER_BEFORE_EVENT
    judging_form = SubFactory(JudgingFormFactory)
    recruit_judges = RECRUIT_NONE
    recruiting_prompt = ""
    positive_recruiting_prompt = ""
    negative_recruiting_prompt = ""
    capture_capacity = False
    capacity_prompt = ""
    capacity_options = "10|20|30|40|50|60|70|80"
    capture_availability = CAPTURE_AVAILABILITY_DISABLED
    feedback_display = FEEDBACK_DISPLAY_DISABLED
    feedback_merge_with = None
    feedback_display_message = ""
    feedback_display_items = ""
    judge_instructions = ""
    presentation_mins = 20
    buffer_mins = 10
    break_mins = 10
    num_breaks = 1
    startup_label = SubFactory(StartupLabelFactory)
    desired_judge_label = SubFactory(UserLabelFactory)
    confirmed_judge_label = SubFactory(UserLabelFactory)
    collision_detection_mode = SCENARIO_DETECTION
