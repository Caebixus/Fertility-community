from django import forms
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.forms.widgets import HiddenInput
from django.forms.widgets import datetime
from ckeditor.widgets import CKEditorWidget
from .choices import GUEST_BLOG_TAG_CHOICES
from django.forms import ModelChoiceField
from .models import GuestAuthor, GuestBlog


class CreateGuestAuthor(forms.ModelForm):
    guestauthor = forms.ModelChoiceField(queryset=BasicClinic.objects.all(), widget=forms.HiddenInput(attrs={'class': 'form-control',}), required=False)
    guestauthorname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=True)
    guestauthorlastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=True)

    guestauthorpic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Author profile photo'))
    guestauthorpicdelete = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete author profile photo'))

    guestauthordescription = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Package description'), max_length=400, required=True)

    guestlinkedinurl = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    guestfacebookurl = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    guesttwitterurl = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    guestadditionalurl = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    class Meta:
        model = GuestAuthor
        fields = [
        'guestauthorname',
        'guestauthorlastname',
        'guestauthorpic',
        'guestauthorpicdelete',
        'guestauthordescription',
        'guestlinkedinurl',
        'guestfacebookurl',
        'guesttwitterurl',
        'guestadditionalurl',
        ]

class CreateGuestBlog(forms.ModelForm):
    guestblogauthor = forms.ModelChoiceField(queryset=GuestAuthor.objects.all(), required=True)
    guestblogtitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=True)
    guestblogdescription = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}, config_name="toolbar_full"), required=True, label=('Package description'), max_length=10000)

    guestblogpicblogmain = forms.ImageField(widget=forms.FileInput(), required=True, label=('Blog main image'))
    guestblogpicblog1 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Additional image 1'))
    guestblogpicblog2 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Additional image 2'))
    guestblogpicblog3 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Additional image 3'))

    guestblogcreatedat = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    guestblogminuteread = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=True)

    class Meta:
        model = GuestBlog
        fields = [
        'guestblogauthor',
        'guestblogtitle',
        'guestblogdescription',
        'guestblogpicblogmain',
        'guestblogpicblog1',
        'guestblogpicblog2',
        'guestblogpicblog3',
        'guestblogminuteread',
        ]
