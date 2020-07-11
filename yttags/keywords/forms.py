# Django Imports
from django import forms


class KeywordsForm(forms.Form):
    keywords = forms.CharField(label='', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'YouTube Search'}))
