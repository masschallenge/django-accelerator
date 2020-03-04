from accelerator.models import UserRole
from accelerator.tests.factories import UserRoleFactory

def user_role_for_name(user_role_name):

    return (UserRole.objects.filter(name=user_role_name).first() or
            UserRoleFactory(name=user_role_name))
 
