from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from bullet_train import BulletTrain

BULLET_TRAIN_ENVIRONMENT_ID ="aX45EUqSsAqhTvv5nW7WEL"

def create_mc_permission(permission):
    ct, _ = ContentType.objects.get_or_create(
        app_label="mc",
        model=permission.content_type.model)
    new_perm, _ = Permission.objects.get_or_create(
        name=permission.name,
        content_type=ct,
        codename=permission.codename)
    for group in permission.group_set.all():
        group.permissions.add(new_perm)
    for user in permission.user_set.all():
        user.user_permissions.add(new_perm)

def bullet_train_access_util(feature_name):
    bt = BulletTrain(environment_id=BULLET_TRAIN_ENVIRONMENT_ID)
    if bt:
        if bt.has_feature(feature_name):
            return bt.feature_enabled(feature_name)
    return False
    