from accelerator.sitetree_navigation.utils import (
    create_subnav,
    delete_nav_tree,
    FLUENT_REDIRECT_URL,
    REGISTER_FOR_EVENTS_URL
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
        "url": FLUENT_REDIRECT_URL,
        "urlaspattern": False,
        "display_single_item": False,
        'active_program': True,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'event_session_slides',
    }, {
        "title": 'Calendar',
        "url": FLUENT_REDIRECT_URL,
        "urlaspattern": False,
        "display_single_item": False,
        'active_program': True,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'event_calendar',
    }, {
        "title": 'Key Dates',
        "url": FLUENT_REDIRECT_URL,
        "urlaspattern": False,
        "display_single_item": False,
        'active_program': True,
        "user_roles": [FINALIST, MENTOR],
        "alias": 'event_key_dates',
    }, {
        "title": 'Register for Events',
        "url": REGISTER_FOR_EVENTS_URL,
        "urlaspattern": False,
        "display_single_item": False,
        'active_program': True,
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'register_for_events',
    }

]


def create_events_subnav():
    create_subnav(EVENTS_SUBNAV_TREE, EVENTS_SUBNAV_ITEMS)


def delete_events_subnav():
    delete_nav_tree(EVENTS_SUBNAV_TREE)
