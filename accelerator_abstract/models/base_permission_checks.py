from accelerator_abstract.models.base_user_utils import (
    is_employee,
)
from accelerator_abstract.models.base_utils import (
    finalist_startup_member
)
from accelerator_abstract.models.base_user_role import (
    is_finalist_user
)


def base_accelerator_check(user):
    return (
        _see_active_pages(user) or
        _see_finalist_pages(user, inactive_programs=True) or
        user.get_profile().is_alum())


def _see_employee_pages(user):
    if user is None:
        return False
    return is_employee(user)


def _see_staff_pages(user):
    return _see_employee_pages(user) or user.is_superuser


def _see_active_pages(user):
    profile = user.get_profile()
    return (_see_finalist_pages(user) or
            profile.is_mentor() or
            profile.is_office_hour_holder() or
            profile.is_alum_in_residence())


def _see_finalist_pages(user, inactive_programs=False):
    return (_see_staff_pages(user) or
            is_finalist_user(user, inactive_programs=inactive_programs) or
            finalist_startup_member(user))
