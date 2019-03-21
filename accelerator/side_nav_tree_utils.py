from accelerator_abstract.models import BaseUserRole
from accelerator.models import (
    NavTree,
    NavTreeItem,
    UserRole
)

MC_SIDE_NAV_TREE_ALIAS = 'mc_side_nav_tree'

SIDE_NAV_TREE_ITEMS_LIST = [
    {
        'title': 'Home',
        'alias': 'home',
        'url': '/',
    },
    {
        'title': 'Events',
        'alias': 'events',
        'url': '/events',
        'active_program': True
    },
    {
        'title': 'Directories',
        'alias': 'directories',
        'url': '/directories',
    },
    {
        'title': 'Office Hours',
        'alias': 'officehours',
        'url': '/officehours',
        'active_program': True,
    },
    {
        'title': 'Room Booking',
        'alias': 'roombooking',
        'url': '/roombooking',
        'active_program': True,
    },
    {
        'title': 'Resources',
        'alias': 'resources',
        'url': '/resources',
        'active_program': True,
    },
    {
        'title': 'My startups',
        'alias': 'mystartups',
        'url': '/mystartups',
    },
    {
        'title': 'Judging',
        'alias': 'judging',
        'url': '/judging',
        'active_program': True,
    },
]


def create_items():
    side_nav_tree = NavTree.objects.filter(
        alias=MC_SIDE_NAV_TREE_ALIAS).first()

    tree_item_objects = []
    for item in SIDE_NAV_TREE_ITEMS_LIST:
        tree_item_objects.append(
            NavTreeItem(
                tree=side_nav_tree,
                **item
            )
        )
    NavTreeItem.objects.bulk_create(tree_item_objects)


def add_user_roles_to_item(alias, user_roles):
    item = NavTreeItem.objects.get(alias=alias)
    for user_role in user_roles:
        if user_role:
            item.user_role.add(user_role)


def add_user_roles_to_items():
    ALUM_ROLE = UserRole.objects.filter(
        name=BaseUserRole.ALUM).first()
    ALUM_IN_RESIDENCE_ROLE = UserRole.objects.filter(
        name=BaseUserRole.AIR).first()
    FINALIST_ROLE = UserRole.objects.filter(
        name=BaseUserRole.FINALIST).first()
    JUDGE_ROLE = UserRole.objects.filter(
        name=BaseUserRole.JUDGE).first()
    MENTOR_ROLE = UserRole.objects.filter(
        name=BaseUserRole.MENTOR).first()
    add_user_roles_to_item(
        'directories', [FINALIST_ROLE, MENTOR_ROLE])
    add_user_roles_to_item(
        'events', [FINALIST_ROLE, MENTOR_ROLE])
    add_user_roles_to_item(
        'officehours', [FINALIST_ROLE, MENTOR_ROLE])
    add_user_roles_to_item(
        'resources', [ALUM_ROLE, FINALIST_ROLE, MENTOR_ROLE])
    add_user_roles_to_item(
        'roombooking', [ALUM_IN_RESIDENCE_ROLE, FINALIST_ROLE, MENTOR_ROLE])
    add_user_roles_to_item(
        'judging', [ALUM_ROLE, FINALIST_ROLE, JUDGE_ROLE])
