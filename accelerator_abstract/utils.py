from __future__ import unicode_literals

import os
import pytz
from django.core.exceptions import ValidationError

IS_NOT_AN_INTEGER_VALUE_MSG = '{} is not an integer value'


def local_time(utc_time):
    if utc_time:
        return utc_time.astimezone(pytz.timezone(os.environ['TZ']))


def validate_capacity_options(value):
    '''
    validate that the option is a pipe-separated list of integer values
    '''
    for elem in value.split('|'):
        try:
            int(elem)
        except ValueError as e:
            provided = _error_msg(e).split(':')[-1].strip()
            raise ValidationError(IS_NOT_AN_INTEGER_VALUE_MSG.format(provided))


def _error_msg(e):
    try:
        msg = e.message
    except AttributeError:
        msg = str(e)
    return msg


def _calc_progress(total, progress_num, **kwargs):
    return {'progress': round(progress_num/total, 2),
            'milestone': kwargs.get('milestone'),
            'profile-complete': kwargs.get('is_profile_complete'),
            'bus-prop-complete': kwargs.get('is_bus_prop_complete')}


def _get_model_fields(model, excluded_fields):
    return [
        field.name for field in
        model._meta.get_fields(
            include_parents=False)
        if field.name not in excluded_fields
    ]


HOUR_FORMAT = "%I:%M %p"
