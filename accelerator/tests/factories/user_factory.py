from factory import (
    DjangoModelFactory,
    Sequence,
)

from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(DjangoModelFactory):

    class Meta:
        model = User

    username = Sequence(lambda n: "username_{0}".format(n))
    email = Sequence(lambda n: "user_{0}@example.com".format(n))
    first_name = Sequence(lambda n: "First {0}".format(n))
    last_name = Sequence(lambda n: "Last {0}".format(n))
    is_superuser = False
    is_staff = False
    is_active = True

    @classmethod
    def _prepare(cls, create, **kwargs):
        # Hash the password if it has been provided
        if 'password' in kwargs:
            kwargs['password'] = make_password(kwargs['password'])
        else:
            kwargs['password'] = make_password('password!')

        return super(UserFactory, cls)._prepare(create, **kwargs)
