from accelerator.sitetree_navigation.utils import (
    create_subnav,
    delete_nav_tree,
    FLUENT_REDIRECT_URL
)
from accelerator_abstract.models import BaseUserRole

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
        "url": FLUENT_REDIRECT_URL,
        "urlaspattern": False,
        "display_single_item": False,
        'active_program': True,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'resources_session_slides',
    }, {
        "title": 'Program Guide',
        "url": FLUENT_REDIRECT_URL,
        "urlaspattern": False,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'resources_program_guide',
    }, {
        "title": 'Office Guide',
        "url": FLUENT_REDIRECT_URL,
        "urlaspattern": False,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'resources_office_guide',
    }, {
        "title": 'In-kind Deals',
        "url": FLUENT_REDIRECT_URL,
        "urlaspattern": False,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'resources_in_kind_deals',
    }
]


def create_resources_subnav():
    create_subnav(RESOURCES_SUBNAV_TREE, RESOURCES_SUBNAV_ITEMS)


def delete_resources_subnav():
    delete_nav_tree(RESOURCES_SUBNAV_TREE)
