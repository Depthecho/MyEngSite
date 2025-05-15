from django import forms
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, Tuple
from .models import Card

# Type variable for form class
T = TypeVar('T', bound='BaseCardForm')

class BaseCardForm(forms.ModelForm):
    """Base form with common styling and placeholders."""
    PLACEHOLDERS: Dict[str, str] = {
        'english_word': 'For example: apple',
        'native_translation': 'For example: яблоко',
        'category': 'For example: fruits (optional)'
    }

    def __init__(self: T, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._add_form_control_class()
        self._set_placeholders()

    def _add_form_control_class(self: T) -> None:
        """Add Bootstrap form-control class to all fields."""
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def _set_placeholders(self: T) -> None:
        """Set placeholder texts from PLACEHOLDERS mapping."""
        for field_name, placeholder in self.PLACEHOLDERS.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['placeholder'] = placeholder

    def clean_english_word(self: T) -> str:
        english_word: str = self.cleaned_data.get('english_word', '').strip()
        if not english_word:
            raise forms.ValidationError("English word is required")
        return english_word

    def clean_native_translation(self: T) -> str:
        native_translation: str = self.cleaned_data.get('native_translation', '').strip()
        if not native_translation:
            raise forms.ValidationError("Native translation is required")
        return native_translation

    class Meta:
        model: Type[Card] = Card
        fields: List[str] = ['english_word', 'native_translation', 'category']


class CardForm(BaseCardForm):
    """Form for creating/editing cards with additional validation."""
    pass


class QuizSettingsForm(forms.Form):
    """Form for configuring quiz parameters."""
    DIRECTION_CHOICES: List[Tuple[str, str]] = [
        ('en_to_native', 'English → Native'),
        ('native_to_en', 'Native → English')
    ]
    MODE_CHOICES: List[Tuple[str, str]] = [
        ('multiple_choice', 'Multiple Choice'),
        ('spelling', 'Spelling')
    ]

    direction: forms.ChoiceField = forms.ChoiceField(
        choices=DIRECTION_CHOICES,
        initial='en_to_native',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    category: forms.CharField = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Filter by category (optional)'
        })
    )
    mode: forms.ChoiceField = forms.ChoiceField(
        choices=MODE_CHOICES,
        initial='multiple_choice',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    limit: forms.IntegerField = forms.IntegerField(
        required=False,
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of questions (empty for all)'
        })
    )


class QuizAnswerForm(forms.Form):
    """Dynamic form for quiz answers processing."""
    def __init__(
        self,
        *args: Any,
        questions: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)
        if questions:
            for question in questions:
                self.fields[f'question_{question["id"]}'] = forms.CharField(
                    required=False,
                    label=question['question']
                )
                self.fields[f'correct_answer_{question["id"]}'] = forms.CharField(
                    widget=forms.HiddenInput(),
                    initial=question['correct_answer']
                )
        self.fields['mode'] = forms.CharField(widget=forms.HiddenInput())