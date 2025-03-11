import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.cache import cache
from django.core.exceptions import ValidationError
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email address',
        max_length=100,
        required=True,
    )
    username = forms.CharField(
        label='Username',
        max_length=150,
        required=True
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=True,
        help_text="Password must be at least 8 characters long and contain at least one letter and one number."
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput,
        required=True
    )
    verification_code = forms.CharField(
        label='Verification Code',
        max_length=6,
        required=True,
        help_text="Enter the 6-digit code sent to your email."
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'verification_code')

    def _validate_unique_field(self, field_name, error_message):
        """Validation of the uniqueness of fields."""
        value = self.cleaned_data.get(field_name)
        if CustomUser.objects.filter(**{field_name: value}).exists():
            raise ValidationError(error_message)
        return value

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Email already exists.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('Email already exists.')
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        if not re.search(r'[A-Za-z]', password1) or not re.search(r'\d', password1):
            raise ValidationError("Password must contain at least one letter and one number.")

        return password1

    def clean_verification_code(self):
        """Validate the verification code from Redis."""
        email = self.cleaned_data.get('email')
        code = self.cleaned_data.get('verification_code')

        if not email or not code:
            raise ValidationError("Email and verification code are required.")

        # Получаем код из Redis
        cached_code = cache.get(email)

        if not cached_code or cached_code != code:
            raise ValidationError('Invalid or expired verification code.')

        return code

    def clean(self):
        """Validate the form."""
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match.')

        return cleaned_data

    def save(self, commit=True):
        """Save the user."""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Username or Email',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your email or username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )