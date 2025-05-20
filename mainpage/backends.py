from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Q
from typing import Optional, Any

User = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request,  username: Optional[str] = None, password: Optional[str] = None, **kwargs: Any)\
            -> Optional[AbstractBaseUser]:
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None