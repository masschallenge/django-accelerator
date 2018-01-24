# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from __future__ import unicode_literals
from django.db import models


def build_case_statement(cases_dict,
                         attr_field,
                         default_value=None,
                         output_field=models.IntegerField()):
    cases = [models.When(**{attr_field: key, "then": models.Value(value)})
             for key, value in cases_dict.items()]
    case_statement = models.Case(default=models.Value(default_value),
                                 output_field=output_field)
    case_statement.cases = cases
    return case_statement

def compose_filter(key_pieces, value):
    return {"__".join(key_pieces): value}
