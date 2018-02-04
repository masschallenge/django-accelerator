# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


def build_case_statement(cases_dict,
                         attr_field,
                         default_value=None,
                         output_field=models.IntegerField()):
    cases = [models.When(**{attr_field: key, 'then': models.Value(value)})
             for key, value in cases_dict.items()]
    case_statement = models.Case(default=models.Value(default_value),
                                 output_field=output_field)
    case_statement.cases = cases
    return case_statement


def compose_filter(key_pieces, value):
    return {'__'.join(key_pieces): value}


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
    if value:
        try:
            map(int, value.split('|'))
        except ValueError as e:
            provided = e.message.split(':')[-1].strip()
            raise ValidationError(
                '{} is not an integer value'.format(provided))


def convert_to_integer(string):
    if string == '' or string is None:
        return None
    try:
        return int(string)
    except ValueError:
        return None


def convert_from_integer(integer):
    if integer is None:
        return ''
    return str(integer)


def convert_to_float(string):
    if string == '' or string is None:
        return None
    try:
        return float(string)
    except ValueError:
        return None


def convert_from_float(floating):
    if floating is None:
        return ''
    return str(floating)


def convert_to_boolean(string):
    if string == '' or string is None:
        return None
    elif string == "False":
        return False
    else:
        return True


def convert_from_boolean(boolean):
    if boolean is None:
        return ''
    elif boolean:
        return 'True'
    else:
        return 'False'
