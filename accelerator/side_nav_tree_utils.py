from accelerator_abstract.models import BaseUserRole
from accelerator.models import NavTree, NavTreeItem, UserRole

MC_SIDE_NAV_TREE_ALIAS = 'mc_side_nav_tree'

SIDE_NAV_TREE_ITEMS_LIST = [
    {
        'title': 'Home',
        'alias': 'home',
        'url': '/'
    },
    {
        'title': 'Events',
        'alias': 'events',
        'url': '/events'
    },
    {
        'title': 'Directories',
        'alias': 'directories',
        'url': '/directories'
    },
    {
        'title': 'Office Hours',
        'alias': 'officehours',
        'url': '/officehours'
    },
    {
        'title': 'Room Booking',
        'alias': 'roombooking',
        'url': '/roombooking'
    },
    {
        'title': 'Resources',
        'alias': 'resources',
        'url': '/resources'
    },
    {
        'title': 'My startups',
        'alias': 'mystartups',
        'url': '/mystartups'
    },
    {
        'title': 'Judging',
        'alias': 'judging',
        'url': '/judging'
    },
]

def create_items():
    side_nav_tree = NavTree.objects.filter(
        alias=MC_SIDE_NAV_TREE_ALIAS).first()

    tree_item_objects = []
    for item in SIDE_NAV_TREE_ITEMS_LIST:
        tree_item_objects.append(
            NavTreeItem(
                title=item['title'],
                alias=item['alias'],
                url=item['url'],
                tree=side_nav_tree
            )
        )
    NavTreeItem.objects.bulk_create(tree_item_objects)

def add_user_roles_to_item(alias, user_roles):
    item = NavTreeItem.objects.get(alias=alias)
    for user_role in user_roles:
        item.user_role.add(user_role)

def add_user_roles_to_items():
    ALUM_ROLE = UserRole.objects.get(name=BaseUserRole.ALUM)
    ALUM_IN_RESIDENCE_ROLE = UserRole.objects.get(name=BaseUserRole.AIR)
    FINALIST_ROLE = UserRole.objects.get(name=BaseUserRole.FINALIST)
    JUDGE_ROLE = UserRole.objects.get(name=BaseUserRole.JUDGE)
    MENTOR_ROLE = UserRole.objects.get(name=BaseUserRole.MENTOR)
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
