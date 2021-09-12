from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class UserEmailBackend(ModelBackend):
    def autheticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            User().set_password(password)
        except User.MultipleObjectsReturned:
            return User.objects.filter(email=email).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user