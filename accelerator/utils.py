def create_mc_permission(permission):
    ct, _ = ContentType.objects.get_or_create(
        app_label="mc",
        model=perm.content_type.model)
    new_perm, _ = Permission.objects.get_or_create(
        name=perm.name,
        content_type=ct,
        codename=perm.codename)
    for group in perm.group_set.all():
        group.permissions.add(new_perm)
    for user in perm.user_set.all():
        user.user_permissions.add(new_perm)