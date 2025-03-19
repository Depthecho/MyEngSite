from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from .forms import CustomUserCreationForm, CustomAuthenticationForm

REGISTRATION_SUCCESS_MSG = 'Registration successful!'
REGISTRATION_FAIL_MSG = 'Registration failed. Please check the form.'
LOGIN_SUCCESS_MSG = 'You have been logged in successfully!'
LOGIN_FAIL_MSG = 'Invalid username/email or password.'


class UserRegistrationService:
    @staticmethod
    def register_user(form, request):
        if not form.is_valid():
            messages.error(request, REGISTRATION_FAIL_MSG)
            raise ValueError(form.errors)

        user = form.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        messages.success(request, REGISTRATION_SUCCESS_MSG)
        return user

class UserAuthenticationService:
    @staticmethod
    def authenticate_user(request, form):
        if not form.is_valid():
            messages.error(request, LOGIN_FAIL_MSG)
            return None

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, LOGIN_FAIL_MSG)
            return None

        login(request, user)
        remember_me = request.POST.get('remember_me')
        request.session.set_expiry(settings.REMEMBER_ME_AGE if remember_me else 0)
        messages.success(request, LOGIN_SUCCESS_MSG)
        return user