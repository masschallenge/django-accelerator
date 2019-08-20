from accelerator.sitetree_navigation.utils import (
    create_subnav,
    delete_nav_tree
)
from accelerator_abstract.models import BaseUserRole

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
        "url": 'judge_feedback_view judging_round.id',
        "urlaspattern": True,
        "user_roles": [FINALIST, ALUMNI],
        "alias": 'judging_feedback',
    }, {
        "title": 'Judging Landing Page',
        "url": 'judge_homepage',
        "urlaspattern": True,
        "user_roles": [JUDGE],
        "alias": 'judging_landing_page',
    }, {
        "title": 'Judging Panels',
        "url": 'panel_listing',
        "urlaspattern": True,
        "user_roles": [JUDGE],
        "alias": 'judging_panels',
    }
]


def create_judging_subnav():
    create_subnav(JUDGING_SUBNAV_TREE, JUDGING_SUBNAV_ITEMS)


def delete_judging_subnav():
    delete_nav_tree(JUDGING_SUBNAV_TREE)
