from __future__ import unicode_literals

import swapper
from factory import (
    Sequence,
    SubFactory,
)
from factory.django import DjangoModelFactory

from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.startup_role_factory import StartupRoleFactory

ProgramStartupStatus = swapper.load_model('accelerator',
                                          'ProgramStartupStatus')


class ProgramStartupStatusFactory(DjangoModelFactory):
    class Meta:
        model = ProgramStartupStatus

    program = SubFactory(ProgramFactory)
    startup_status = Sequence(lambda n: "program_startup_status{0}".format(n))
    description = Sequence(
        lambda n: "Description of Program Startup Status{0}".format(n))
    startup_role = SubFactory(StartupRoleFactory)
    startup_list_include = False
    startup_list_tab_title = Sequence(
        lambda n: "Tab Title for Program Startup Status {0}".format(n))
    startup_list_tab_description = Sequence(
        lambda n: "Tab Description for Program Startup Status {0}".format(n))
    startup_list_tab_id = Sequence(lambda n: "PSS_{0}".format(n))
    startup_list_tab_order = 1
    include_stealth_startup_names = False
    badge_image = None
    badge_display = "NONE"
    status_group = ""
    sort_order = 1
