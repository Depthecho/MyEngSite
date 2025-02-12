import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
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

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def _validate_unique_field(self, field_name, error_message):
        """validation of the uniqueness of fields."""
        value = self.cleaned_data.get(field_name)
        if CustomUser.objects.filter(**{field_name: value}).exists():
            raise ValidationError(error_message)
        return value

    def clean_email(self):
        return self._validate_unique_field('email', 'Email address already exists.')

    def clean_username(self):
        return self._validate_unique_field('username', 'Username already exists.')

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        if not re.search(r'[A-Za-z]', password1) or not re.search(r'\d', password1):
            raise ValidationError("Password must contain at least one letter and one number.")

        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user