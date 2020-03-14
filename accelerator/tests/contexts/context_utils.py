from accelerator.tests.factories import UserRoleFactory
from django.conf import settings
import swapper

app_label, model = swapper.split(settings.ACCELERATOR_USERROLE_MODEL)
UserRole = swapper.load_model(app_label, model)


def user_role_for_name(user_role_name):
    return (UserRole.objects.filter(name=user_role_name).first() or
            UserRoleFactory(name=user_role_name))
