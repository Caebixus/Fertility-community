from django import forms
from blog.models import Blog, BestClinicArticleCity, BestClinicArticleState, BestClinicArticleCountry
from .models import Coaches, PreferredLanguage, Snippet, TypeJobs, SnippetCity, SnippetState, SnippetCountry
from ckeditor.widgets import CKEditorWidget
from clinic.choices import CATEGORY_CHOICES_STATES

LANGUAGE_CHOICES = (
    (1, 'English'),
    (2, 'German'),
    (3, 'Chinese'),
    (4, 'Portuguese'),
    (5, 'Spanish'),
)

class CreateNewCoachForm(forms.ModelForm):
    coach_full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    coach_username = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    coach_bio = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}, config_name="toolbar_snippet"), required=False, label=('Fertility coach BIO information'), max_length=300)

    coach_contact_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    coach_preferred_client_country = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_STATES, attrs={'class': 'form-control', }),label=('Clinics state'))

    m2m_jobs = forms.ModelMultipleChoiceField(queryset=TypeJobs.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control', 'size': '10'}), required=False)
    m2m_languages = forms.ModelMultipleChoiceField(queryset=PreferredLanguage.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control','size': '10'}), required=False)

    coach_profile_photo = forms.ImageField(widget=forms.FileInput(), required=False, label=('Profile picture'))
    coach_profile_photo_delete = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete profile picture'))

    coach_social_instagram = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    coach_social_facebook = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_linkedin = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_pinterest = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_twitter = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_website = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    coach_is_published = forms.BooleanField(required=False)
    coach_is_premium = forms.BooleanField(required=False)

    class Meta:
        model = Coaches
        fields = [
            'coach_full_name',
            'coach_username',
            'coach_bio',
            'coach_contact_email',
            'coach_phone',
            'coach_preferred_client_country',

            'm2m_jobs',
            'm2m_languages',

            'coach_profile_photo',
            'coach_profile_photo_delete',
            'coach_social_instagram',
            'coach_social_facebook',
            'coach_social_linkedin',
            'coach_social_pinterest',
            'coach_social_twitter',
            'coach_social_website',
        ]

    # def __init__(self, user, *args, **kwargs):
    #     super(CreateNewCoachForm, self).__init__(*args, **kwargs)
    #     language_list = list(PreferredLanguage.objects.filter(coaches_relationship__coach_user=user))
    #     self.initial['coach_preferred_languages'] = language_list

    def __init__(self, *args, **kwargs):
        super(CreateNewCoachForm, self).__init__(*args, **kwargs)
        self.fields['m2m_languages'].queryset = PreferredLanguage.objects.all()
        self.fields['m2m_jobs'].queryset = TypeJobs.objects.all()


class UpdateCoachForm(forms.ModelForm):
    coach_full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    coach_username = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    coach_bio = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}, config_name="toolbar_snippet"), required=False, label=('Fertility coach BIO information'), max_length=300)

    coach_contact_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    coach_preferred_client_country = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_STATES, attrs={'class': 'form-control', }),label=('Clinics state'))

    m2m_jobs = forms.ModelMultipleChoiceField(queryset=TypeJobs.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control', 'size': '10'}), required=False)
    m2m_languages = forms.ModelMultipleChoiceField(queryset=PreferredLanguage.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control','size': '10'}), required=False)

    coach_profile_photo = forms.ImageField(widget=forms.FileInput(), required=False, label=('Profile picture'))
    coach_profile_photo_delete = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete profile picture'))

    coach_social_instagram = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    coach_social_facebook = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_linkedin = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_pinterest = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_twitter = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    coach_social_website = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    class Meta:
        model = Coaches
        fields = [
            'coach_full_name',
            'coach_username',
            'coach_bio',
            'coach_contact_email',
            'coach_phone',
            'coach_preferred_client_country',

            'm2m_jobs',
            'm2m_languages',

            'coach_profile_photo',
            'coach_profile_photo_delete',
            'coach_social_instagram',
            'coach_social_facebook',
            'coach_social_linkedin',
            'coach_social_pinterest',
            'coach_social_twitter',
            'coach_social_website',
        ]

    def __init__(self, coaches_id, *args, **kwargs):
        super(UpdateCoachForm, self).__init__(*args, **kwargs)
        coach = Coaches.objects.get(pk=coaches_id)
        language_filtered_obj = PreferredLanguage.objects.filter(coaches_relationship=coach.pk)
        jobs_filtered_obj = TypeJobs.objects.filter(coaches_relationship=coach.pk)

        self.fields['m2m_languages'].queryset = PreferredLanguage.objects.all()
        self.fields['m2m_jobs'].queryset = TypeJobs.objects.all()

        self.initial['m2m_languages'] = language_filtered_obj
        self.initial['m2m_jobs'] = jobs_filtered_obj


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


class SnippetCityCreateForm(forms.ModelForm):
    blog = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'form-control','size': '15'}), required=False)
    text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', }, config_name="toolbar_snippet"), required=False, max_length=1200)

    class Meta:
        model = SnippetCity
        fields = [
            'blog',
            'text',
        ]

    def __init__(self, coach, *args, **kwargs):
        super().__init__(*args, **kwargs)

        owner = Coaches.objects.get(pk=coach.pk)
        metadata = SnippetCity.objects.filter(owner=owner)
        tests = BestClinicArticleCity.objects.exclude(snippet_city_blog__in=metadata).distinct()

        self.fields['blog'].queryset = tests

class SnippetCityUpdateForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', }, config_name="toolbar_snippet"), required=False, max_length=1200)

    class Meta:
        model = SnippetCity
        fields = [
            'text',
        ]


class SnippetStateCreateForm(forms.ModelForm):
    blog = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'form-control','size': '15'}), required=False)
    text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', }, config_name="toolbar_snippet"), required=False, max_length=1200)

    class Meta:
        model = SnippetState
        fields = [
            'blog',
            'text',
        ]

    def __init__(self, coach, *args, **kwargs):
        super().__init__(*args, **kwargs)

        owner = Coaches.objects.get(pk=coach.pk)
        metadata = SnippetState.objects.filter(owner=owner)
        tests = BestClinicArticleState.objects.exclude(snippet_state_blog__in=metadata).distinct()

        self.fields['blog'].queryset = tests

class SnippetStateUpdateForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', }, config_name="toolbar_snippet"), required=False, max_length=1200)

    class Meta:
        model = SnippetState
        fields = [
            'text',
        ]


class SnippetCountryCreateForm(forms.ModelForm):
    blog = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'form-control','size': '15'}), required=False)
    text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', }, config_name="toolbar_snippet"), required=False, max_length=1200)

    class Meta:
        model = SnippetCountry
        fields = [
            'blog',
            'text',
        ]

    def __init__(self, coach, *args, **kwargs):
        super().__init__(*args, **kwargs)

        owner = Coaches.objects.get(pk=coach.pk)
        metadata = SnippetCountry.objects.filter(owner=owner)
        tests = BestClinicArticleCountry.objects.exclude(snippet_country_blog__in=metadata).distinct()

        self.fields['blog'].queryset = tests

class SnippetCountryUpdateForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control', }, config_name="toolbar_snippet"), required=False, max_length=1200)

    class Meta:
        model = SnippetCountry
        fields = [
            'text',
        ]