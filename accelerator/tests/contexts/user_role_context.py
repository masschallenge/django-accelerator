from builtins import object

from accelerator.tests.factories import (
    ExpertFactory,
    ProgramFactory,
    ProgramRoleFactory,
    ProgramRoleGrantFactory,
    UserLabelFactory,
    UserRoleFactory,
)
from accelerator.tests.contexts.context_utils import user_role_for_name
from accelerator.models import UserRole


class UserRoleContext(object):

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
        self.user_role = user_role_for_name(user_role_name)
        user_label = user_label or UserLabelFactory()
        self.program_role = ProgramRoleFactory(user_role=self.user_role,
                                               program=self.program,
                                               landing_page=landing_page,
                                               user_label=user_label)
        self.program_role_grant = ProgramRoleGrantFactory(
            person=self.user,
            program_role=self.program_role)
