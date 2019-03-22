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
        'active_program': True,
        'user_roles': [FINALIST, MENTOR]
    },
    {
        'title': 'Directories',
        'alias': 'directories',
        'url': '/directories',
        'active_program': True,
        'user_roles': [FINALIST, MENTOR],
    },
    {
        'title': 'Office Hours',
        'alias': 'officehours',
        'url': '/officehours',
        'active_program': True,
        'user_roles': [FINALIST, MENTOR],
    },
    {
        'title': 'Room Booking',
        'alias': 'roombooking',
        'url': '/roombooking',
        'active_program': True,
        'user_roles': [AIR, FINALIST, MENTOR],
    },
    {
        'title': 'Resources',
        'alias': 'resources',
        'url': '/resources',
        'active_program': True,
        'user_roles': [ALUM, FINALIST, MENTOR],
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
        'user_roles': [ALUM, FINALIST, JUDGE],
    },
]


def create_items(tree, item_props_list):
    tree_item_objects = []
    for item in item_props_list:
        item_kwargs = dict(item)
        item_kwargs.pop('user_roles', None)
        tree_item_objects.append(
            NavTreeItem(
                tree=tree,
                **item_kwargs
            )
        )
    NavTreeItem.objects.bulk_create(tree_item_objects)


def add_user_roles_to_item(item_props):
    allowed_user_roles = item_props.get('user_roles', [])
    user_roles = UserRole.objects.filter(name__in=allowed_user_roles)
    tree_item = NavTreeItem.objects.filter(alias=item_props["alias"]).first()
    for user_role in user_roles:
        tree_item.user_role.add(user_role)


def add_user_roles_to_side_nav_items(item_props_list):
    for item_props in item_props_list:
        add_user_roles_to_item(item_props)
