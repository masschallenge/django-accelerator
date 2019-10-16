from datetime import (
    date,
    datetime,
    time,
)
from pytz import (
    timezone,
    utc,
)
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


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


def localized_today_utc_date(_timezone):
    tz = timezone(_timezone)
    today = tz.localize(datetime.combine(
        date.today(), time(0))).astimezone(utc)
    return today
