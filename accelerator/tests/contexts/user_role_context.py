from accelerator.tests.factories import (
    ExpertFactory,
    ProgramFactory,
    ProgramRoleFactory,
    ProgramRoleGrantFactory,
    UserLabelFactory,
)
from accelerator.tests.contexts.context_utils import get_user_role_by_name


class UserRoleContext:

    def __init__(self, user_role_name,
                 program=None,
                 user=None,
                 landing_page=None,
                 user_label=None):
        if user and not program:
            self.program = user.get_profile().current_program
        else:
            self.program = program or ProgramFactory()
        self.user = (user or
                     ExpertFactory(profile__current_program=self.program))
        self.user_role = get_user_role_by_name(user_role_name)
        user_label = user_label or UserLabelFactory()
        self.program_role = ProgramRoleFactory(user_role=self.user_role,
                                               program=self.program,
                                               landing_page=landing_page,
                                               user_label=user_label)
        self.program_role_grant = ProgramRoleGrantFactory(
            person=self.user,
            program_role=self.program_role)
