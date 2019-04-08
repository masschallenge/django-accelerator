from accelerator_abstract.models import BaseUserRole


AIR = BaseUserRole.AIR
ALUM = BaseUserRole.ALUM
FINALIST = BaseUserRole.FINALIST
JUDGE = BaseUserRole.JUDGE
MENTOR = BaseUserRole.MENTOR

SIDE_NAV_ITEM_PROPS_LIST = [
    {
        'title': 'Home',
        'alias': 'home',
        'url': '/',
    },
    {
        'title': 'Events',
        'alias': 'events',
        'url': '/nav/events',
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
        'user_roles': [AIR, FINALIST, MENTOR],
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
        'url': '/nav/resources',
        'active_program': True,
        'user_roles': [AIR, ALUM, FINALIST, MENTOR],
    },
    {
        'title': 'My startups',
        'alias': 'mystartups',
        'url': '/mystartups',
    },
    {
        'title': 'Judging',
        'alias': 'judging',
        'url': '/nav/judging',
        'active_program': True,
        'user_roles': [ALUM, FINALIST, JUDGE],
    },
]
