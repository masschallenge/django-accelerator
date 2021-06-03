from accelerator.models import UserRole
from accelerator.tests.contexts.context_utils import get_user_role_by_name
from accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.program_role_factory import ProgramRoleFactory
from accelerator.tests.factories.program_role_grant_factory import (
    ProgramRoleGrantFactory
)


class MentorUserContext:
    def __init__(self,
                 program=None,
                 program_role=None,
                 program_role_landing_page="",
                 user=None):
        self.user = user
        self.program = program
        if not program:
            self.user = user or ExpertFactory()
            if program_role:
                self.program = program_role.program
            else:
                program_family = self.user.get_profile().home_program_family
                self.program = ProgramFactory(program_family=program_family)
        elif not user:
            program_family = program.program_family
            self.user = ExpertFactory(
                profile__home_program_family=program_family)
        user_role = get_user_role_by_name(UserRole.MENTOR)
        self.program_role = program_role or ProgramRoleFactory(
            program=self.program,
            landing_page=program_role_landing_page,
            user_role=user_role)
        self.program_role_grant = ProgramRoleGrantFactory(
            person=self.user,
            program_role=self.program_role)
