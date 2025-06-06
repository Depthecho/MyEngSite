from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from typing import Any, Dict, Optional
from .models import Profile # Используем Profile, как и раньше
from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model

UserModel = get_user_model() # Получаем текущую модель User


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model: type[Profile] = Profile
        fields: list[str] = []
        widgets: Dict[str, forms.Widget] = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model: type[UserModel] = UserModel
        fields: list[str] = ['username', 'first_name', 'last_name', 'email']
        labels: Dict[str, str] = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }


class ProfileUpdateForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields: list[str] = [
            'english_level',
            'birth_date',
            'hide_first_name',
            'hide_last_name',
            'hide_birth_date',
            'bio',
            'location',
            'avatar',
        ]
        labels: Dict[str, str] = {
            'english_level': 'English Level',
            'birth_date': 'Birth Date',
            'hide_first_name': 'Hide First Name',
            'hide_last_name': 'Hide Last Name',
            'hide_birth_date': 'Hide Birth Date',
            'bio': 'Biography',
            'location': 'Location',
            'avatar': 'Avatar',
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._apply_common_styling()

    def _apply_common_styling(self) -> None:
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'new-password'
            })