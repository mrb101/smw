from django import forms
from django.forms import ModelForm

from .models import Cover


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=60,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))


class CoverForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn-file', 'value': 'Choose Image'}))

    class Meta:
        model = Cover
        fields = ['name', 'image']
