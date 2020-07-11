# Django Imports
from django import forms

# Enter search term for utils.py
class TagsForm(forms.Form):
    url = forms.CharField(label='', max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'YouTube URL'}))
