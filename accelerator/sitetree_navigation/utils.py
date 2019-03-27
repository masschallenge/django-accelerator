from accelerator.models import (
    NavTreeItem,
    UserRole,
)


def create_items(tree, item_props_list, parent=None):
    for item_props in item_props_list:
        item_kwargs = dict(item_props)
        item_kwargs.pop('user_roles', None)
        NavTreeItem.objects.update_or_create(
                tree=tree,
                **item_kwargs
            )


def _add_user_roles_to_item(item_props):
    allowed_user_roles = item_props.get('user_roles', [])
    if not allowed_user_roles:
        return None

    user_roles = UserRole.objects.filter(name__in=allowed_user_roles)
    tree_item = NavTreeItem.objects.filter(alias=item_props["alias"]).first()
    tree_item.user_role.clear()
    for user_role in user_roles:
        tree_item.user_role.add(user_role)


def add_user_roles_to_nav_items(item_props_list):
    for item_props in item_props_list:
        _add_user_roles_to_item(item_props)
