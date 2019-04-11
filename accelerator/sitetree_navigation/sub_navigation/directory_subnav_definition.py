from accelerator.models import NavTree
from accelerator.sitetree_navigation.utils import (
    add_user_roles_to_nav_items,
    create_items,
    delete_nav_tree
)
from accelerator_abstract.models import BaseUserRole

FINALIST = BaseUserRole.FINALIST
ALUMNI = BaseUserRole.ALUM
MENTOR = BaseUserRole.MENTOR

DIRECTORY_SUBNAV_TREE = {
    "title": 'Directories SubNav',
    "alias": 'directories_subnav'
}

DIRECTORY_SUBNAV_ITEMS = [
    {
        "title": 'Mentors',
        "url": '/directory',
        "alias": 'mentor_directory',
        "user_roles": [FINALIST, ALUMNI, MENTOR]
    }, {
        "title": 'People',
        "url": '/people',
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'people_directory',
    }
]


def create_directory_subnav():
    tree, _ = NavTree.objects.update_or_create(
        alias=DIRECTORY_SUBNAV_TREE['alias'],
        defaults=DIRECTORY_SUBNAV_TREE)
    create_items(tree, DIRECTORY_SUBNAV_ITEMS)
    add_user_roles_to_nav_items(DIRECTORY_SUBNAV_ITEMS)


def delete_directory_subnav():
    delete_nav_tree(DIRECTORY_SUBNAV_TREE)
