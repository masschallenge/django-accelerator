from accelerator.models import (
    NavTreeItem,
    UserRole
)


def create_items(tree, item_props_list):
    tree_item_objects = []
    for item_props in item_props_list:
        item_kwargs = dict(item_props)
        item_kwargs.pop('user_roles', None)
        tree_item_objects.append(
            NavTreeItem(
                tree=tree,
                **item_kwargs
            )
        )
    NavTreeItem.objects.bulk_create(tree_item_objects)


def add_user_roles_to_item(item_props):
    allowed_user_roles = item_props.get('user_roles', [])
    user_roles = UserRole.objects.filter(name__in=allowed_user_roles)
    tree_item = NavTreeItem.objects.filter(alias=item_props["alias"]).first()
    for user_role in user_roles:
        tree_item.user_role.add(user_role)


def add_user_roles_to_side_nav_items(item_props_list):
    for item_props in item_props_list:
        add_user_roles_to_item(item_props)
