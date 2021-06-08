from bullet_train import BulletTrain
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.conf import settings


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


def flag_smith_has_feature(feature_name):
    if settings.FLAG_SMITH_API_KEY:
        flag_smith_key = settings.FLAG_SMITH_API_KEY.strip('"')
    else:
        flag_smith_key = ''
    bt = BulletTrain(environment_id=flag_smith_key)
    if bt:
        if bt.has_feature(feature_name):
            return bt.feature_enabled(feature_name)
    return False


class UserAlert(object):
    alert_type = ''  # identifies the type/class of an alert
    alert_style = 'info'  # info, error, success, warning
    message = ''  # message to be displayed to the user (can be HTML)


def copy_m2m_fields(old_obj, new_obj, m2m_fields):
    for field in m2m_fields:
        field_pk = set(
            getattr(old_obj, field).all().values_list('pk', flat=True))
        getattr(new_obj, field).add(*field_pk)
