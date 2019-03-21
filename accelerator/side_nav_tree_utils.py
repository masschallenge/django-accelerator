from accelerator_abstract.models import BaseUserRole
from accelerator.models import (
    NavTreeItem,
    UserRole
)

AIR = BaseUserRole.AIR
ALUM = BaseUserRole.ALUM
FINALIST = BaseUserRole.FINALIST
JUDGE = BaseUserRole.JUDGE
MENTOR = BaseUserRole.MENTOR

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


def create_items(tree, items_list):
    tree_item_objects = []
    for item in items_list:
        tree_item_objects.append(
            NavTreeItem(
                tree=tree,
                **item
            )
        )
    NavTreeItem.objects.bulk_create(tree_item_objects)


def add_user_roles_to_item(alias, user_roles):
    item = NavTreeItem.objects.get(alias=alias)
    for user_role in user_roles:
        if user_role:
            item.user_role.add(user_role)


def get_user_roles():
    user_roles = [
        AIR,
        ALUM,
        FINALIST,
        JUDGE,
        MENTOR,
    ]
    user_roles_dict = dict(
        (user_role.name, user_role) for user_role in
        UserRole.objects.filter(name__in=user_roles))

    return user_roles_dict


def add_user_roles_to_side_nav_items():
    user_roles = get_user_roles()
    ALUM_IN_RESIDENCE_ROLE = user_roles.get(AIR)
    ALUM_ROLE = user_roles.get(ALUM)
    FINALIST_ROLE = user_roles.get(FINALIST)
    JUDGE_ROLE = user_roles.get(JUDGE)
    MENTOR_ROLE = user_roles.get(MENTOR)

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
