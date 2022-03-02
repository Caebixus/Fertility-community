from django import forms
from blog.models import Blog
from .models import Coaches, PreferredLanguage, SnippetNew, Snippet
from ckeditor.widgets import CKEditorWidget
from clinic.choices import CATEGORY_CHOICES_STATES

LANGUAGE_CHOICES = (
    (1, 'English'),
    (2, 'German'),
    (3, 'Chinese'),
    (4, 'Portuguese'),
    (5, 'Spanish'),
)


class UpdateCoachForm(forms.ModelForm):
    coach_full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    coach_username = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    coach_bio = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}, config_name="toolbar_bestclinicarticles"), required=False, label=('Fertility coach BIO information'), max_length=150)

    coach_contact_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    coach_preferred_client_country = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_STATES, attrs={'class': 'form-control', }),label=('Clinics state'))

    m2m_languages = forms.ModelMultipleChoiceField(queryset=PreferredLanguage.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control','size': '5'}), required=False)

    coach_profile_photo = forms.ImageField(widget=forms.FileInput(), required=False, label=('Profile picture'))
    coach_profile_photo_delete = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete profile picture'))

    coach_social_instagram = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    coach_social_facebook = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_linkedin = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_pinterest = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_twitter = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_website = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    job_gynecologist = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    job_obstetrician = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    job_reproductive_immunologist = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    job_reproductive_surgeon = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    job_andrologist = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    job_reproductive_endocrinologist = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    job_fertility_specialist = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    job_fertility_coach = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = Coaches
        fields = [
            'coach_full_name',
            'coach_username',
            'coach_bio',
            'coach_contact_email',
            'coach_phone',
            'coach_preferred_client_country',

            'm2m_languages',

            'coach_profile_photo',
            'coach_profile_photo_delete',
            'coach_social_instagram',
            'coach_social_facebook',
            'coach_social_linkedin',
            'coach_social_pinterest',
            'coach_social_twitter',
            'coach_social_website',

            'job_gynecologist',
            'job_obstetrician',
            'job_reproductive_immunologist',
            'job_reproductive_surgeon',
            'job_andrologist',
            'job_reproductive_endocrinologist',
            'job_fertility_specialist',
            'job_fertility_coach',
        ]

    def __init__(self, user, *args, **kwargs):
        super(UpdateCoachForm, self).__init__(*args, **kwargs)
        #language_list = list(PreferredLanguage.objects.filter(coaches_relationship__coach_user=user))
        self.initial['m2m_languages'] = PreferredLanguage.objects.filter(coaches_relationship__coach_user=user)



class SnippetForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', }, config_name="toolbar_snippet"), required=False, max_length=1200)

    class Meta:
        model = SnippetNew
        fields = [
            'text',
        ]


class SnippetCreateForm2(forms.ModelForm):
    blog = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'form-control','size': '15'}), required=False)
    text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', }, config_name="toolbar_snippet"), required=False, max_length=1200)

    class Meta:
        model = Snippet
        fields = [
            'blog',
            'text',
        ]

    def __init__(self, coach, *args, **kwargs):
        super().__init__(*args, **kwargs)

        owner = Coaches.objects.get(pk=coach.pk)
        metadata = Snippet.objects.filter(owner=owner)
        tests = Blog.objects.exclude(snippet_blog__in=metadata).distinct()

        self.fields['blog'].queryset = tests

class SnippetUpdateForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', }, config_name="toolbar_snippet"), required=False, max_length=1200)

    class Meta:
        model = Snippet
        fields = [
            'text',
        ]
