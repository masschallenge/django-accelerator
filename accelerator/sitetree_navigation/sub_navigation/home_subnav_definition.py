from accelerator_abstract.models import BaseUserRole
from accelerator.sitetree_navigation.utils import (
    create_items,
    add_user_roles_to_nav_items
)
from accelerator.models import NavTree

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
        "url": 'add_panel_judge',
        "urlaspattern": True,
        'active_program': True,
        "display_single_item": False,
        "user_roles": [FINALIST],
        "alias": 'finalist_dashboard',
    }, {
        "title": 'Alumni Dashboard',
        "url": 'allocation_panel_stats scenario.id',
        "alias": 'alumni_dashboard',
        'active_program': True,
        "user_roles": [ALUMNI]
    }, {
        "title": 'Mentor Dashboard',
        "url": 'allocation_stats scenario.id',
        "urlaspattern": True,
        'active_program': True,
        "display_single_item": False,
        "user_roles": [MENTOR],
        "alias": 'mentor_dashboard',
    }, {
        "title": 'Judge Dashboard',
        "url": 'analysis_results',
        "urlaspattern": True,
        "alias": 'judge_dashboard',
        "user_roles": [JUDGE]
    }
]


def create_home_subnav():
    tree = NavTree.objects.create(**HOME_SUBNAV_TREE)
    create_items(tree, HOME_SUBNAV_ITEMS)
    add_user_roles_to_nav_items(HOME_SUBNAV_ITEMS)
