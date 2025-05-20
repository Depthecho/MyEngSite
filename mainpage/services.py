from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.http import HttpRequest
from django.forms import Form
from django.contrib.auth.models import AbstractBaseUser
from typing import Optional, Dict, Any
from .forms import CustomUserCreationForm, CustomAuthenticationForm

REGISTRATION_SUCCESS_MSG: str = 'Registration successful!'
REGISTRATION_FAIL_MSG: str = 'Registration failed. Please check the form.'
LOGIN_SUCCESS_MSG: str = 'You have been logged in successfully!'
LOGIN_FAIL_MSG: str = 'Invalid username/email or password.'


class UserRegistrationService:
    @staticmethod
    def register_user(
            form: CustomUserCreationForm,
            request: HttpRequest
    ) -> AbstractBaseUser:
        if not form.is_valid():
            messages.error(request, REGISTRATION_FAIL_MSG)
            raise ValueError(form.errors)

        user: AbstractBaseUser = form.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        messages.success(request, REGISTRATION_SUCCESS_MSG)
        return user


class UserAuthenticationService:
    @staticmethod
    def authenticate_user(
            request: HttpRequest,
            form: CustomAuthenticationForm
    ) -> Optional[AbstractBaseUser]:
        if not form.is_valid():
            messages.error(request, LOGIN_FAIL_MSG)
            return None

        username: Optional[str] = form.cleaned_data.get('username')
        password: Optional[str] = form.cleaned_data.get('password')

        if not username or not password:
            messages.error(request, LOGIN_FAIL_MSG)
            return None

        user: Optional[AbstractBaseUser] = authenticate(
            request,
            username=username,
            password=password
        )

        if not user:
            messages.error(request, LOGIN_FAIL_MSG)
            return None

        login(request, user)
        remember_me: Optional[str] = request.POST.get('remember_me')
        request.session.set_expiry(
            settings.REMEMBER_ME_AGE if remember_me else 0
        )
        messages.success(request, LOGIN_SUCCESS_MSG)
        return user