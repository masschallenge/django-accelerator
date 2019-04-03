from accelerator.models import NavTree
from accelerator.sitetree_navigation.utils import (
    create_items,
    add_user_roles_to_nav_items
)
from accelerator_abstract.models import BaseUserRole

FINALIST = BaseUserRole.FINALIST
ALUMNI = BaseUserRole.ALUM
MENTOR = BaseUserRole.MENTOR
JUDGE = BaseUserRole.JUDGE

HOME_SUBNAV_TREE = {
    "title": 'Home Sub Nav',
    "alias": 'home_subnav'
}

HOME_SUBNAV_ITEMS = [
    {
        "title": 'Finalist Dashboard',
        "url": '/fluent-redirect',
        "urlaspattern": False,
        'active_program': True,
        "display_single_item": False,
        "user_roles": [FINALIST],
        "alias": 'finalist_dashboard',
    }, {
        "title": 'Alumni Dashboard',
        "url": '/fluent-redirect',
        "alias": 'alumni_dashboard',
        'active_program': True,
        "urlaspattern": False,
        "user_roles": [ALUMNI]
    }, {
        "title": 'Mentor Dashboard',
        "url": '/fluent-redirect',
        "urlaspattern": False,
        'active_program': True,
        "display_single_item": False,
        "user_roles": [MENTOR],
        "alias": 'mentor_dashboard',
    }, {
        "title": 'Judge Dashboard',
        "url": '/fluent-redirect',
        "urlaspattern": False,
        "alias": 'judge_dashboard',
        "user_roles": [JUDGE]
    }
]


def create_home_subnav():
    tree, _ = NavTree.objects.update_or_create(
        alias=HOME_SUBNAV_TREE['alias'],
        defaults=HOME_SUBNAV_TREE)
    create_items(tree, HOME_SUBNAV_ITEMS)
    add_user_roles_to_nav_items(HOME_SUBNAV_ITEMS)
