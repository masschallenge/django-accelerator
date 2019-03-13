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
                 user_role=None,
                 program_family=None,
                 program=None,
                 display_single_item=False,
                 program_role_user_role=UserRole.STAFF):

        self.display_single_item = display_single_item
        self.tree = tree or NavTreeFactory()

        self.tree_item = NavTreeItemFactory(
            tree=self.tree,
            display_single_item=display_single_item)

        self.tree_items = [self.tree_item]

        self.user_role = user_role or UserRoleFactory()
        self.program_family = program_family or ProgramFamilyFactory()

        self.program = program or ProgramFactory(
            program_family=self.program_family)

        self.user = ExpertFactory(
            profile__home_program_family=self.program_family)
        self.program_role = ProgramRoleFactory(
            program=self.program, user_role__name=program_role_user_role)
        self.program_role_grant = ProgramRoleGrantFactory(
            person=self.user,
            program_role=self.program_role)

    def update_item_title(self, tree_item, title):
        tree_item.title = title
        tree_item.save()

    def add_tree_item(self, user_role=None):
        item = NavTreeItemFactory(
            tree=self.tree,
            display_single_item=self.display_single_item)

        if user_role:
            item.user_role.add(user_role)
            item.save()

        self.tree_items.append(item)
        return item

    def add_user_role_to_tree_item(self, tree_item=None, user_role=None):

        if tree_item is None:
            tree_item = self.tree_item

        if user_role is None:
            user_role = self.user_role

        tree_item.user_role.add(user_role)

    def add_program_to_tree_item(self, tree_item=None, program=None):

        if tree_item is None:
            tree_item = self.tree_item

        if program is None:
            program = self.program

        tree_item.program.add(program)
        return program

    def add_program_family_to_tree_item(self, tree_item=None, family=None):

        if tree_item is None:
            tree_item = self.tree_item

        if family is None:
            family = self.program_family

        tree_item.program_family.add(family)

    def add_role_permissions(self, program=None, user_role=None):

        if program is None:
            program = ProgramFactory()

        if user_role is None:
            user_role = UserRoleFactory()

        program_role = ProgramRoleFactory(
            program=program, user_role=user_role)
        self.program_role_grant = ProgramRoleGrantFactory(
            person=self.user,
            program_role=program_role)
