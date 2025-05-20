from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from typing import Any, Dict, Optional
from .models import Profile
from django.contrib.auth import password_validation


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model: type[Profile] = Profile
        fields: list[str] = []
        widgets: Dict[str, forms.Widget] = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


class ProfileUpdateForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields: list[str] = [
            'username', 'first_name', 'last_name', 'birth_date',
            'hide_first_name', 'hide_last_name', 'hide_birth_date',
            'bio', 'website', 'location', 'avatar'
        ]

    def clean_email(self) -> Optional[str]:
        email: Optional[str] = self.cleaned_data.get('email')
        if email:
            try:
                validate_email(email)
            except ValidationError:
                raise forms.ValidationError("Enter a valid email address.")
        return email


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