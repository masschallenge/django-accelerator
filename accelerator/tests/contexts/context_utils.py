from accelerator.tests.factories import UserRoleFactory
from django.conf import settings

app_label, model = swapper.split(settings.ACCELERATOR_USERROLE_MODEL)
from accelerator.models import UserRole


def get_user_role_by_name(user_role_name):
    return (UserRole.objects.filter(name=user_role_name).first() or
            UserRoleFactory(name=user_role_name))
