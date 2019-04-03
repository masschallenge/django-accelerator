from accelerator.models import NavTree
from accelerator.sitetree_navigation.utils import (
    create_items,
    add_user_roles_to_nav_items
)
from accelerator_abstract.models import BaseUserRole

FINALIST = BaseUserRole.FINALIST
ALUMNI = BaseUserRole.ALUM
MENTOR = BaseUserRole.MENTOR

EVENTS_SUBNAV_TREE = {
    "title": 'Events Sub Nav',
    "alias": 'events_subnav'
}

EVENTS_SUBNAV_ITEMS = [
    {
        "title": 'Session Slides',
        "url": '/fluent-redirect',
        "urlaspattern": False,
        "display_single_item": False,
        'active_program': True,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'event_session_slides',
    }, {
        "title": 'Calendar',
        "url": '/fluent-redirect',
        "urlaspattern": False,
        "display_single_item": False,
        'active_program': True,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'event_calendar',
    }, {
        "title": 'Key Dates',
        "url": '/fluent-redirect',
        "urlaspattern": False,
        "display_single_item": False,
        'active_program': True,
        "user_roles": [FINALIST, MENTOR],
        "alias": 'event_key_dates',
    }
]


def create_events_subnav():
    tree, _ = NavTree.objects.update_or_create(
        alias=EVENTS_SUBNAV_TREE['alias'],
        defaults=EVENTS_SUBNAV_TREE)
    create_items(tree, EVENTS_SUBNAV_ITEMS)
    add_user_roles_to_nav_items(EVENTS_SUBNAV_ITEMS)
