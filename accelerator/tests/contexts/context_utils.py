import swapper
from django.conf import settings

from accelerator.tests.factories import (
    ClearanceFactory,
    EntrepreneurFactory,
    ProgramFamilyFactory,
    UserRoleFactory
)
from accelerator_abstract.models import CLEARANCE_LEVEL_STAFF

app_label, model = swapper.split(settings.ACCELERATOR_USERROLE_MODEL)
UserRole = swapper.load_model(app_label, model)


def get_user_role_by_name(user_role_name):
    return (UserRole.objects.filter(name=user_role_name).first() or
            UserRoleFactory(name=user_role_name))


def employee_user(user=None,
                  program_family=None,
                  is_superuser=False):
    if user:
        user.is_superuser = is_superuser
        user.save()
    clearance = ClearanceFactory(
        level=CLEARANCE_LEVEL_STAFF,
        user=user or EntrepreneurFactory(is_superuser=is_superuser),
        program_family=program_family or ProgramFamilyFactory()
    )
    return clearance.user
