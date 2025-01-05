from django import forms
from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('about', 'interest', 'wanted', 'future' )
        widgets = {
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'interest': forms.Textarea(attrs={'class': 'form-control'}),
            'wanted': forms.Textarea(attrs={'class': 'form-control'}),
            'future': forms.Textarea(attrs={'class': 'form-control'}),
        }