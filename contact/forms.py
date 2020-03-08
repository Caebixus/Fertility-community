from django import forms
from .models import contactClinic, claimClinic, contactWebsite
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from django.forms.widgets import datetime
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.ModelForm):
    contactTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Title'))
    contactMessage = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',}), label=('Message'))

    class Meta:
        model = contactClinic
        fields = [
        'contactTitle',
        'contactMessage',
        ]

class ClaimForm(forms.ModelForm):
    claimTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Title'))
    claimMessage = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',}), label=('Message'))
    claimUrl = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control',}), label=('URL of your clinic on our website'))

    class Meta:
        model = claimClinic
        fields = [
        'claimTitle',
        'claimMessage',
        'claimUrl',
        ]

class WebsiteForm(forms.ModelForm):
    contactTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Title'))
    contactMessage = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',}), label=('Message'))
    contact_email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Your email address, please'))

    class Meta:
        model = contactWebsite
        fields = [
        'contactTitle',
        'contactMessage',
        ]
