from accelerator.tests.contexts.mentor_user_context import MentorUserContext
from accelerator.tests.factories.named_group_factory import NamedGroupFactory


class MentorProgramGroupContext(object):
    def __init__(self):
        mentor_context1 = MentorUserContext()
        mentor_context2 = MentorUserContext()
        self.mentors = [mentor_context1.user, mentor_context2.user]
        self.programs = [mentor_context1.program, mentor_context2.program]
        self.program_group = NamedGroupFactory()
        _set_mentor_program_group(self.programs[0], self.program_group)
        _set_mentor_program_group(self.programs[1], self.program_group)


def _set_mentor_program_group(program, program_group):
    program.mentor_program_group = program_group
    program.save()
