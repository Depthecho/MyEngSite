from django import forms
from .models import Text

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['title', 'content', 'english_level']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter text title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Enter the text content'}),
            'english_level': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'english_level': 'English Level',
        }
