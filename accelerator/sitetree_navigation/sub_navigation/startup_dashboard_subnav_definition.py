from accelerator.models import (
    NavTree,
    NavTreeItem
)
from accelerator.sitetree_navigation.utils import (
    add_user_roles_to_nav_items,
    create_items,
    delete_nav_tree
)
from accelerator_abstract.models import BaseUserRole


ALUM = BaseUserRole.ALUM
FINALIST = BaseUserRole.FINALIST
STARTUP_DASHBOARD_TREE_ALIAS = 'startup_dashboard_subnav'
STARTUP_PROFILE_ALIAS = 'startup_profile'

STARTUP_DASHBOARD_SUBNAV_TREE = {
    "title": 'Startup Dashboard SubNav',
    "alias": STARTUP_DASHBOARD_TREE_ALIAS
}

STARTUP_DASHBOARD_SUBNAV_ITEMS = [
    {
        "title": 'Dashboard',
        "url": 'startup_dashboard startup.id',
        "urlaspattern": True,
        "alias": "dashbaord"
    }, {
        "title": 'Profile',
        "url": '/',
        "alias": STARTUP_PROFILE_ALIAS
    }, {
        "title": 'Team',
        "url": 'startup_team_view startup.id',
        "urlaspattern": True,
        "alias": "startup_team"
    }, {
        "title": 'Mentors & Goals',
        "url": (
            'startup_mentor_tracking_view startup.id'
            ' family_slug program_slug'
        ),
        "urlaspattern": True,
        "alias": 'startup_mentors_and_goals',
        "user_roles": [ALUM, FINALIST]
    }
]

STARTUP_DASHBOARD_SUBNAV_CHILDREN_ITEMS = [
    {
        "title": 'View Profile',
        "url": 'startup_preview startup.id',
        "urlaspattern": True,
        "alias": "startup_view"
    }, {
        "title": 'Edit Profile',
        "url": 'edit_startup startup.id',
        "urlaspattern": True,
        "alias": "startup_edit"
    }
]


def create_startup_dashboard_subnav():
    tree, _ = NavTree.objects.update_or_create(
        alias=STARTUP_DASHBOARD_SUBNAV_TREE['alias'],
        defaults=STARTUP_DASHBOARD_SUBNAV_TREE)
    create_items(tree, STARTUP_DASHBOARD_SUBNAV_ITEMS)
    profile_item = NavTreeItem.objects.filter(
        alias=STARTUP_PROFILE_ALIAS).first()
    create_items(tree, STARTUP_DASHBOARD_SUBNAV_CHILDREN_ITEMS, profile_item)
    add_user_roles_to_nav_items(STARTUP_DASHBOARD_SUBNAV_ITEMS)


def delete_startup_dashboard_subnav():
    delete_nav_tree(STARTUP_DASHBOARD_SUBNAV_TREE)
