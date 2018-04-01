# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

import os
import pytz
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

IS_NOT_AN_INTEGER_VALUE_MSG = '{} is not an integer value'


def local_time(utc_time):
    if utc_time:
        return utc_time.astimezone(pytz.timezone(os.environ['TZ']))


def url_validator():
    schema = '^[hH][tT][tT][pP][sS]?://'
    netloc_element = '([^/:@]+(:[^/@]+)?@)?([\w-]+)'
    dot = '\.'

    url_regex = '{schema}({netloc_element}{dot})+{netloc_element}'.format(
        schema=schema,
        netloc_element=netloc_element,
        dot=dot
    )

    return RegexValidator(
        regex=url_regex,
        message='Enter a valid URL')


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


HOUR_FORMAT = "%I:%M %p"
