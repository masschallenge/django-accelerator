from accelerator.models import (
    NavTree,
    NavTreeItem,
    UserRole,
    Program,
    ProgramFamily,
)


FLUENT_REDIRECT_URL = '/nav/fluent-redirect'
REGISTER_FOR_EVENTS_URL = '/events/'


def create_items(tree, item_props_list, parent=None):
    for item_props in item_props_list:
        item_kwargs = dict(item_props)
        item_kwargs.pop('user_roles', None)
        item_kwargs.pop('programs', None)
        item_kwargs.pop('program_families', None)
        if parent:
            item_kwargs['parent'] = parent
        NavTreeItem.objects.update_or_create(
            alias=item_kwargs['alias'],
            tree=tree,
            defaults=item_kwargs,
        )


def create_subnav(subnav_tree, subnav_items):
    tree, _ = NavTree.objects.update_or_create(
        alias=subnav_tree['alias'],
        defaults=subnav_tree)
    create_items(tree, subnav_items)
    add_user_roles_to_nav_items(subnav_items)


def _add_user_roles_to_item(item_props):
    allowed_user_roles = item_props.get('user_roles', [])
    if not allowed_user_roles:
        return

    user_roles = UserRole.objects.filter(name__in=allowed_user_roles)
    tree_item = NavTreeItem.objects.filter(alias=item_props["alias"]).first()
    tree_item.user_role.clear()
    for user_role in user_roles:
        tree_item.user_role.add(user_role)


def _add_allowed_programs_to_item(item_props):
    allowed_programs = item_props.get('programs', [])
    if not allowed_programs:
        return

    programs = Program.objects.filter(id__in=allowed_programs)
    tree_item = NavTreeItem.objects.filter(alias=item_props["alias"]).first()
    tree_item.program.clear()
    for program in programs:
        tree_item.program.add(program)


def _add_allowed_program_families_to_item(item_props):
    allowed_program_families = item_props.get('program_families', [])
    if not allowed_program_families:
        return

    program_families = ProgramFamily.objects.filter(
            id__in=allowed_program_families)
    tree_item = NavTreeItem.objects.filter(alias=item_props["alias"]).first()
    tree_item.program_family.clear()
    for program_family in program_families:
        tree_item.program_family.add(program_family)


def add_allowed_programs_to_nav_items(item_props_list):
    for item_props in item_props_list:
        _add_allowed_programs_to_item(item_props)


def add_allowed_program_families_to_nav_items(item_props_list):
    for item_props in item_props_list:
        _add_allowed_program_families_to_item(item_props)


def add_user_roles_to_nav_items(item_props_list):
    for item_props in item_props_list:
        _add_user_roles_to_item(item_props)


def add_user_roles_to_side_nav_items(item_props_list):
    add_user_roles_to_nav_items(item_props_list)


def delete_nav_tree(nav_tree_props):
    tree = NavTree.objects.filter(alias=nav_tree_props["alias"]).first()
    if tree:
        tree.delete()
