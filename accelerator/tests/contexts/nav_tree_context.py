from accelerator.tests.factories import (
    ExpertFactory,
    NavTreeFactory,
    NavTreeItemFactory,
    ProgramFamilyFactory,
    ProgramFactory,
    ProgramRoleFactory,
    ProgramRoleGrantFactory,
    UserRoleFactory,
)

from accelerator.models import UserRole


class NavTreeContext(object):
    def __init__(self,
                 tree=None,
                 program_family=None,
                 program=None,
                 user_role=UserRole.STAFF,
                 tree_user_role=UserRole.STAFF):

        self.tree = tree
        if not tree:
            self.tree = NavTreeFactory()

        self.user_role = UserRoleFactory(name=tree_user_role)

        self.tree_item = NavTreeItemFactory(
            tree=self.tree,
            user_role=self.user_role)

        self.program_family = program_family
        if program_family is None:
            self.program_family = ProgramFamilyFactory()

        self.program = program
        if program is None:
            self.program = ProgramFactory(
                program_family=self.program_family)

        self.user = ExpertFactory(
            profile__home_program_family=self.program_family)
        self.program_role = ProgramRoleFactory(
            program=self.program, user_role__name=user_role)
        self.program_role_grant = ProgramRoleGrantFactory(
            person=self.user,
            program_role=self.program_role)

    def add_program_to_tree_item(self, tree_item=None, program=None):

        if tree_item is None:
            tree_item = self.tree_item

        if program is None:
            program = self.program

        tree_item.program.add(program)

    def add_program_family_to_tree_item(self, tree_item=None, family=None):

        if tree_item is None:
            tree_item = self.tree_item

        if family is None:
            family = self.program_family

        tree_item.program_family.add(family)

    def add_excluded_program_to_tree_item(self, tree_item=None, program=None):

        if tree_item is None:
            tree_item = self.tree_item

        if program is None:
            program = self.program

        tree_item.program_exclude.add(program)

    def add_excluded_family_to_tree_item(self, tree_item=None, family=None):

        if tree_item is None:
            tree_item = self.tree_item

        if family is None:
            family = self.program_family

        tree_item.program_family_exclude.add(family)
