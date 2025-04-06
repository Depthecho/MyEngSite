from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['english_word', 'native_translation', 'category']
        widgets = {
            'english_word': forms.TextInput(attrs={
                'placeholder': 'For example: apple'
            }),
            'native_translation': forms.TextInput(attrs={
                'placeholder': 'For example: яблоко'
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'For example: fruits'
            })
        }