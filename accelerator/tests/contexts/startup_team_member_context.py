from datetime import (
    datetime,
    timedelta,
)

from accelerator.tests.factories import (
    EntrepreneurFactory,
    ProgramCycleFactory,
    ProgramFactory,
    StartupFactory,
    StartupStatusFactory,
    StartupTeamMemberFactory,
)
from pytz import utc

from accelerator_abstract.models import (
    ACTIVE_PROGRAM_STATUS,
    UPCOMING_PROGRAM_STATUS,
)


class StartupTeamMemberContext(object):
    def __init__(self,
                 cycle=None,
                 program=None,
                 startup=None,
                 startup_role=None,
                 user=None,
                 upcoming=False,
                 startup_administrator=False,
                 primary_contact=True,
                 founder=False,
                 program_status=ACTIVE_PROGRAM_STATUS):
        applications_open = False
        if upcoming:
            program_status = UPCOMING_PROGRAM_STATUS
            applications_open = True
        tomorrow = utc.localize(datetime.now() + timedelta(1))
        later = utc.localize(datetime.now() + timedelta(3))
        if cycle:
            self.cycle = cycle
        else:
            self.cycle = ProgramCycleFactory(
                advertised_final_deadline=tomorrow,
                application_final_deadline_date=later,
                applications_open=applications_open)
        self.program = program or ProgramFactory(cycle=self.cycle,
                                                 program_status=program_status,
                                                 start_date=tomorrow)
        self.user = user or EntrepreneurFactory()
        if primary_contact:
            self.startup = startup or StartupFactory(user=self.user)
            self.member = self.startup.primary_contact()
        else:
            self.startup = startup or StartupFactory()
            self.member = StartupTeamMemberFactory(
                startup=self.startup,
                startup_administrator=startup_administrator,
                founder=founder,
                user=self.user)
        self.startup_statuses = []
        self.program_startup_statuses = []

        if startup_role:
            self.create_startup_status(startup_role)

    def create_startup_status(self, startup_role):
        startup_status = StartupStatusFactory(
                program_startup_status__program=self.program,
                program_startup_status__startup_role=startup_role,
                startup=self.startup)
        self.startup_statuses.append(startup_status)
        self.program_startup_statuses.append(
            startup_status.program_startup_status)
