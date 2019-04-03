from accelerator.models import NavTree
from accelerator_abstract.models import BaseUserRole
from accelerator.sitetree_navigation.utils import (
    add_user_roles_to_nav_items,
    create_items
)

FINALIST = BaseUserRole.FINALIST
ALUMNI = BaseUserRole.ALUM
MENTOR = BaseUserRole.MENTOR

RESOURCES_SUBNAV_TREE = {
    "title": 'Resources Sub Nav',
    "alias": 'resources_subnav'
}

RESOURCES_SUBNAV_ITEMS = [
    {
        "title": 'Session Slides',
        "url": '/fluent-redirect',
        "urlaspattern": False,
        "display_single_item": False,
        'active_program': True,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'resources_session_slides',
    }, {
        "title": 'Program Guide',
        "url": '/fluent-redirect',
        "urlaspattern": False,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'resources_program_guide',
    }, {
        "title": 'Office Guide',
        "url": '/fluent-redirect',
        "urlaspattern": False,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'resources_office_guide',
    }, {
        "title": 'In-kind Deals',
        "url": '/fluent-redirect',
        "urlaspattern": False,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'resources_in_kind_deals',
    }
]


def create_resources_subnav():
    tree, _ = NavTree.objects.update_or_create(
        alias=RESOURCES_SUBNAV_TREE['alias'],
        defaults=RESOURCES_SUBNAV_TREE)
    create_items(tree, RESOURCES_SUBNAV_ITEMS)
    add_user_roles_to_nav_items(RESOURCES_SUBNAV_ITEMS)
