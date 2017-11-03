from django.contrib.auth import get_user_model

User = get_user_model()


class EmailModelBackend(object):

    def authenticate(self, email=None, password=None, username=None):
        try:
            if not email:
                email = username
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
