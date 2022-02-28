from __future__ import unicode_literals

from datetime import (
    datetime,
    timedelta,
)

from django.urls import reverse
from pytz import utc
import logging


logger = logging.getLogger(__name__)

TEST_PASSWORD = 'simplepass1'


def get_app_name():
    try:
        from mc.apps import MCAppConfig
        return MCAppConfig.name
    except ImportError as error:
        logger.warning(error)
        return 'accelerator'


def login_as_user(test, user):
    user.set_password(TEST_PASSWORD)
    user.save()
    return test.client.login(username=user.email, password=TEST_PASSWORD)


def login_as_new_user(test, factory, is_superuser=False):
    user = factory(is_superuser=is_superuser)
    login_as_user(test, user)
    return user


def check_not_http_success(test, data={}, **kwargs):
    url = reverse(test.view_name, kwargs=kwargs)
    response = test.client.get(url, data=data)
    assert response.status_code >= 300
    return response


# There was nothing particularly 'anon' about this
# method, but keeping the old name around for now.
# Also this isn't a simple "assert" in that they don't
# simply test the state of the world, but actually
# load a page.  We've decided to move to calling these
# "checks".
assert_not_http_success = check_not_http_success
assert_anon_cannot_view = check_not_http_success


def check_http_success(test, data={}, **kwargs):
    url = reverse(test.view_name, kwargs=kwargs)
    response = test.client.get(url, data=data)
    assert 200 <= response.status_code and response.status_code < 300
    return response


# 'view' is ambiguous, but keeing the old name around
# for now.
# Also this isn't a simple "assert" in that they don't
# simply test the state of the world, but actually
# load a page.  We've decided to move to calling these
# "checks".
assert_http_success = check_http_success
assert_can_view = check_http_success


def delete_user_profile(user):
    user.get_profile().delete()
    user.save()


def days_from_now(days):
    return utc.localize(datetime.now() + timedelta(days))


def minutes_from_now(minutes):
    return utc.localize(datetime.now()) + timedelta(minutes=minutes)


def months_from_now(months):
    return days_from_now(months * 30)


def fake_method_value_error(*args, **kwargs):
    raise ValueError


def find_row(rows, header, value):
    for row in rows:
        if row[header] == value:
            return row
    return None

def fake_flag_smith_response(feature_of_interest, feature_on):
    def fake_feature_check(feature_to_check):
        return feature_on == (feature_to_check == feature_of_interest)

    return fake_feature_check
