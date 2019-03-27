from accelerator_abstract.models import BaseUserRole
from accelerator.sitetree_navigation.utils import (
    create_items,
    add_user_roles_to_nav_items
)
from accelerator.models import NavTree

FINALIST = BaseUserRole.FINALIST
ALUMNI = BaseUserRole.ALUM
JUDGE = BaseUserRole.JUDGE

JUDGING_SUBNAV_TREE = {
    "title": 'Judging Sub Nav',
    "alias": 'judging_subnav'
}

JUDGING_SUBNAV_ITEMS = [
    {
        "title": 'Feedback',
        "url": 'application_judging_progress_view',
        "urlaspattern": True,
        "user_roles": [FINALIST, ALUMNI],
        "alias": 'judging_feedbakc',
    }, {
        "title": 'Documentation',
        "url": 'application_pdf_view application.id',
        "urlaspattern": True,
        "user_roles": [FINALIST, ALUMNI],
        "alias": 'judging_documentation',
    }, {
        "title": 'Judging Landing Page',
        "url": 'application_stats scenario.id',
        "urlaspattern": True,
        "user_roles": [JUDGE],
        "alias": 'judging_landing_page',
    }, {
        "title": 'Judging Panels',
        "url": 'application_stats_csv scenario.id',
        "urlaspattern": True,
        "alias": 'mentors_and_goals',
        "user_roles": [JUDGE],
        "alias": 'judging_panels',
    }
]


def create_judging_subnav():
    tree = NavTree.objects.create(**JUDGING_SUBNAV_TREE)
    create_items(tree, JUDGING_SUBNAV_ITEMS)
    add_user_roles_to_nav_items(JUDGING_SUBNAV_ITEMS)
