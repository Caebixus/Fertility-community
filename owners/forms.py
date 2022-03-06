from django import forms

from clinic.models import BasicClinic, LIVE_CHAT_CHOICES, TRUSTPILOT_CHOICES
from .models import ownerProInterested, SingleClinicBestArticleText
from packages.models import Package
from packages.packageChoices import CATEGORY_PACKAGE, PACKAGE_TYPE
from ckeditor.widgets import CKEditorWidget
from coaches.models import Coaches, PreferredLanguage

from clinic.choices import CATEGORY_CHOICES_CURRENCY, HOURS, CATEGORY_CHOICES_STATES
from coaches.choices import CATEGORY_CHOICES_LANGUAGES


class CreateClinic(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'))
    clinicTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False, label=('Clinics Title'))
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, label=('Clinics Description'), max_length=1300)

    contact_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    contact_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    fertilitycommunity_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    clinicStreetAddress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics street address'))
    clinicCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics city'))

    clinicState = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_STATES, attrs={'class': 'form-control',}), label=('Clinics state'))

    clinicRegion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False, label=('Clinics Region/Country'))

    clinicPostalCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics postal code'))

    clinicEnglish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('English speaking personal'))
    clinicSpanish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Spanish speaking personal'))
    clinicPortuguese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Portguesse speaking personal'))
    clinicRussian = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Russian speaking personal'))
    clinicGerman = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('German speaking personal'))
    clinicChinese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Chinese speaking personal'))

    mondayOpens = forms.CharField(widget=forms.Select(choices=HOURS, attrs={'class': 'form-control',}), required=False,)
    mondayCloses = forms.CharField(widget=forms.Select(choices=HOURS, attrs={'class': 'form-control',}), required=False,)
    tuesdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    tuesdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    wednesdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    wednesdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    thursdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    thursdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    fridayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    fridayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    saturdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    saturdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    sundayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    sundayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)

    is_claimed = forms.BooleanField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=True, required=False)
    is_published = forms.BooleanField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)
    pro_is_published = forms.BooleanField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)
    is_published_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    single_woman_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    reciprocal_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    hiv_patients_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sex_selection = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    accepts_patients_from_abroad = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}))

    class Meta:
        model = BasicClinic
        fields = [
        'clinicName',
        'clinicTitle',
        'description',
        'contact_url',
        'clinicStreetAddress',
        'clinicCity',
        'clinicState',
        'clinicRegion',
        'clinicPostalCode',
        'clinicEnglish',
        'clinicSpanish',
        'clinicPortuguese',
        'clinicRussian',
        'clinicGerman',
        'clinicChinese',
        'mondayOpens',
        'mondayCloses',
        'tuesdayOpens',
        'tuesdayCloses',
        'wednesdayOpens',
        'wednesdayCloses',
        'thursdayOpens',
        'thursdayCloses',
        'fridayOpens',
        'fridayCloses',
        'saturdayOpens',
        'saturdayCloses',
        'sundayOpens',
        'sundayCloses',
        'is_published',
        'is_published_list_date',
        'single_woman_treatment',
        'reciprocal_treatment',
        'hiv_patients_treatment',
        'sex_selection',
        'accepts_patients_from_abroad',
        ]


class UpdateClinic(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'))
    clinicTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False, label=('Clinics Title'))
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics Description'), required=False, max_length=1300)
    treatmentLimitations = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics treatment limitations'), required=False, max_length=800)

    clinic_pro_logo_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Clinics Logo'))
    clinic_pro_logo_pic_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    contact_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    contact_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    fertilitycommunity_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    clinicStreetAddress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics street address'))
    clinicCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics city'))

    clinicState = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_STATES, attrs={'class': 'form-control',}), label=('Clinics state'))

    clinicRegion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False, label=('Clinics Region/Country'))
    clinicPostalCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics postal code'))

    clinicEnglish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('English speaking personal'))
    clinicSpanish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Spanish speaking personal'))
    clinicPortuguese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Portguesse speaking personal'))
    clinicRussian = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Russian speaking personal'))
    clinicGerman = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('German speaking personal'))
    clinicChinese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Chinese speaking personal'))

    clinic_pro_photo_1 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_1_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_2 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_2_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_3 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_3_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_4 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_4_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_5 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_5_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_6 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_6_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    is_published_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    mondayOpens = forms.CharField(widget=forms.Select(choices=HOURS, attrs={'class': 'form-control',}), required=False,)
    mondayCloses = forms.CharField(widget=forms.Select(choices=HOURS, attrs={'class': 'form-control',}), required=False,)
    tuesdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    tuesdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    wednesdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    wednesdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    thursdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    thursdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    fridayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    fridayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    saturdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    saturdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    sundayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    sundayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)

    single_woman_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    reciprocal_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    hiv_patients_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sex_selection = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    accepts_patients_from_abroad = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    clinicFacebook = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    clinicInstagram = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    clinicTwitter = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    clinicYoutube = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    clinicLinkedIn = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    clinicPinterest = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    payment_type_cash = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    payment_type_major_credit_cards = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    payment_type_debit_cards = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    payment_type_check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    payment_type_cryptocurrency = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    payment_type_wire_transfer = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)


    class Meta:
        model = BasicClinic
        fields = [
        'clinicName',
        'clinicTitle',
        'description',
        'treatmentLimitations',
        'clinic_pro_logo_pic',
        'clinic_pro_logo_pic_del',
        'contact_url',
        'contact_phone',
        'contact_email',
        'fertilitycommunity_email',
        'clinicStreetAddress',
        'clinicCity',
        'clinicState',
        'clinicRegion',
        'clinicPostalCode',
        'clinicEnglish',
        'clinicSpanish',
        'clinicPortuguese',
        'clinicRussian',
        'clinicGerman',
        'clinicChinese',
        'mondayOpens',
        'mondayCloses',
        'tuesdayOpens',
        'tuesdayCloses',
        'wednesdayOpens',
        'wednesdayCloses',
        'thursdayOpens',
        'thursdayCloses',
        'fridayOpens',
        'fridayCloses',
        'saturdayOpens',
        'saturdayCloses',
        'sundayOpens',
        'sundayCloses',
        'is_published_list_date',
        'clinic_pro_photo_1',
        'clinic_pro_photo_1_del',
        'clinic_pro_photo_2',
        'clinic_pro_photo_2_del',
        'clinic_pro_photo_3',
        'clinic_pro_photo_3_del',
        'clinic_pro_photo_4',
        'clinic_pro_photo_4_del',
        'clinic_pro_photo_5',
        'clinic_pro_photo_5_del',
        'clinic_pro_photo_6',
        'clinic_pro_photo_6_del',
        'single_woman_treatment',
        'reciprocal_treatment',
        'hiv_patients_treatment',
        'sex_selection',
        'accepts_patients_from_abroad',
        'clinicFacebook',
        'clinicInstagram',
        'clinicTwitter',
        'clinicYoutube',
        'clinicLinkedIn',
        'clinicPinterest',
        'payment_type_cash',
        'payment_type_major_credit_cards',
        'payment_type_debit_cards',
        'payment_type_check',
        'payment_type_cryptocurrency',
        'payment_type_wire_transfer',
        ]


class UpdatePrice(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'), required=False)
    defaultClinicCurrency = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_CURRENCY, attrs={'class': 'form-control', }), label=('Clinics default currency'))
    ### Primary treatments
    ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    mild_ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    ovarian_ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    icsi_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    iui_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    mild_ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    ovarian_ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    icsi_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    iui_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')

    ivf_treatment_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    mild_ivf_treatment_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    ovarian_ivf_treatment_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    icsi_treatment_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    iui_treatment_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)

    ### IVF with donation & costs treatments
    egg_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    known_egg_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    embryo_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    known_embryo_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sperm_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    known_sperm_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    egg_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    known_egg_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    embryo_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    known_embryo_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    sperm_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    known_sperm_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')

    egg_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    known_egg_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    embryo_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    known_embryo_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    sperm_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    known_sperm_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)

    ### Additional treatments & costs
    egg_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    embryo_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sperm_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    surrogacy = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    egg_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    embryo_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    sperm_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    surrogacy_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')

    egg_freezing_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    embryo_freezing_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    sperm_freezing_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    surrogacy_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)

    is_published_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    class Meta:
        model = BasicClinic
        fields = [
        'clinicName',
        'defaultClinicCurrency',
        'ivf_treatment',
        'mild_ivf_treatment',
        'ovarian_ivf_treatment',
        'icsi_treatment',
        'iui_treatment',
        'ivf_treatment_cost',
        'mild_ivf_treatment_cost',
        'ovarian_ivf_treatment_cost',
        'icsi_treatment_cost',
        'iui_treatment_cost',
        'ivf_treatment_faqs',
        'mild_ivf_treatment_faqs',
        'ovarian_ivf_treatment_faqs',
        'icsi_treatment_faqs',
        'iui_treatment_faqs',
        'egg_donor_recipients',
        'known_egg_donor_recipients',
        'embryo_donor_recipients',
        'known_embryo_donor_recipients',
        'sperm_donor_recipients',
        'known_sperm_donor_recipients',
        'egg_donor_recipients_cost',
        'known_egg_donor_recipients_cost',
        'embryo_donor_recipients_cost',
        'known_embryo_donor_recipients_cost',
        'sperm_donor_recipients_cost',
        'known_sperm_donor_recipients_cost',
        'egg_donor_recipients_faqs',
        'known_egg_donor_recipients_faqs',
        'embryo_donor_recipients_faqs',
        'known_embryo_donor_recipients_faqs',
        'sperm_donor_recipients_faqs',
        'known_sperm_donor_recipients_faqs',
        'egg_freezing',
        'embryo_freezing',
        'sperm_freezing',
        'surrogacy',
        'egg_freezing_cost',
        'embryo_freezing_cost',
        'sperm_freezing_cost',
        'surrogacy_cost',
        'egg_freezing_faqs',
        'embryo_freezing_faqs',
        'sperm_freezing_faqs',
        'surrogacy_faqs',
        'is_published_list_date',
        ]


class UpdateClinicPro(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'))
    clinicTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Title'), required=False)
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics Description'), required=False, max_length=1300)
    treatmentLimitations = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics treatment limitations'), required=False, max_length=800)

    clinic_staff = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics staff'), required=False, max_length=300)

    clinic_pro_promotion_name = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Promotion'), required=False, max_length=80)

    clinic_pro_logo_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Clinics Logo'))
    clinic_pro_logo_pic_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))
    clinic_pro_main_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Clinics Main picture'))

    contact_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    contact_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    query_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    fertilitycommunity_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    clinicStreetAddress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    clinicCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    clinicState = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_STATES, attrs={'class': 'form-control',}), label=('Clinics state'))

    clinicRegion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Region/Country'), required=False)

    clinicPostalCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    clinicEnglish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('English speaking personal'))
    clinicSpanish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Spanish speaking personal'))
    clinicPortuguese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Portguesse speaking personal'))
    clinicRussian = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Russian speaking personal'))
    clinicGerman = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('German speaking personal'))
    clinicChinese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Chinese speaking personal'))

    team1name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('First team member'), required=False)
    team1pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    team1pic_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))
    team1position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Position of first team member'), required=False)

    team2name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Second team member'), required=False)
    team2pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of second team member'))
    team2pic_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))
    team2position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Position of second team member'), required=False)

    team3name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Third team member'), required=False)
    team3pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of third team member'))
    team3pic_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))
    team3position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Position of third team member'), required=False)

    clinic_pro_photo_1 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_1_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_2 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_2_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_3 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_3_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_4 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_4_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_5 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_5_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_6 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_6_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    pro_is_published_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    mondayOpens = forms.CharField(widget=forms.Select(choices=HOURS, attrs={'class': 'form-control',}), required=False,)
    mondayCloses = forms.CharField(widget=forms.Select(choices=HOURS, attrs={'class': 'form-control',}), required=False,)
    tuesdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    tuesdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    wednesdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    wednesdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    thursdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    thursdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    fridayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    fridayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    saturdayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    saturdayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    sundayOpens = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)
    sundayCloses = forms.CharField(widget=forms.Select(choices = HOURS, attrs={'class': 'form-control',}), required=False,)

    single_woman_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    reciprocal_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    hiv_patients_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sex_selection = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    accepts_patients_from_abroad = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    clinicFacebook = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    clinicInstagram = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    clinicTwitter = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    clinicYoutube = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    clinicLinkedIn = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    clinicPinterest = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    payment_type_cash = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    payment_type_major_credit_cards = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    payment_type_debit_cards = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    payment_type_check = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    payment_type_cryptocurrency = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    payment_type_wire_transfer = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    class Meta:
        model = BasicClinic
        fields = [
        'clinicName',
        'clinicTitle',
        'description',
        'treatmentLimitations',
        'clinic_staff',
        'clinic_pro_promotion_name',
        'clinic_pro_logo_pic',
        'clinic_pro_logo_pic_del',
        'clinic_pro_main_pic',
        'contact_url',
        'query_email',
        'contact_phone',
        'contact_email',
        'fertilitycommunity_email',
        'clinicStreetAddress',
        'clinicCity',
        'clinicState',
        'clinicRegion',
        'clinicPostalCode',
        'clinicEnglish',
        'clinicSpanish',
        'clinicPortuguese',
        'clinicRussian',
        'clinicGerman',
        'clinicChinese',
        'pro_is_published_list_date',
        'mondayOpens',
        'mondayCloses',
        'tuesdayOpens',
        'tuesdayCloses',
        'wednesdayOpens',
        'wednesdayCloses',
        'thursdayOpens',
        'thursdayCloses',
        'fridayOpens',
        'fridayCloses',
        'saturdayOpens',
        'saturdayCloses',
        'sundayOpens',
        'sundayCloses',
        'team1name',
        'team1pic',
        'team1pic_del',
        'team1position',
        'team2name',
        'team2pic',
        'team2pic_del',
        'team2position',
        'team3name',
        'team3pic',
        'team3pic_del',
        'team3position',
        'clinic_pro_photo_1',
        'clinic_pro_photo_1_del',
        'clinic_pro_photo_2',
        'clinic_pro_photo_2_del',
        'clinic_pro_photo_3',
        'clinic_pro_photo_3_del',
        'clinic_pro_photo_4',
        'clinic_pro_photo_4_del',
        'clinic_pro_photo_5',
        'clinic_pro_photo_5_del',
        'clinic_pro_photo_6',
        'clinic_pro_photo_6_del',
        'single_woman_treatment',
        'reciprocal_treatment',
        'hiv_patients_treatment',
        'sex_selection',
        'accepts_patients_from_abroad',
        'clinicFacebook',
        'clinicInstagram',
        'clinicTwitter',
        'clinicYoutube',
        'clinicLinkedIn',
        'clinicPinterest',
        'payment_type_cash',
        'payment_type_major_credit_cards',
        'payment_type_debit_cards',
        'payment_type_check',
        'payment_type_cryptocurrency',
        'payment_type_wire_transfer',
        ]


class UpdatePricePro(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'), required=False)
    defaultClinicCurrency = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_CURRENCY, attrs={'class': 'form-control', }), label=('Clinics default currency'))
    ### Primary treatments
    ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    mild_ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    ovarian_ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    icsi_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    iui_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    mild_ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    ovarian_ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    icsi_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    iui_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')

    ivf_treatment_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    mild_ivf_treatment_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    ovarian_ivf_treatment_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    icsi_treatment_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    iui_treatment_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)

    ### IVF with donation & costs treatments
    egg_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    known_egg_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    embryo_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    known_embryo_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sperm_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    known_sperm_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    egg_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    known_egg_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    embryo_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    known_embryo_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    sperm_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    known_sperm_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')

    egg_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    known_egg_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    embryo_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    known_embryo_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    sperm_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    known_sperm_donor_recipients_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)

    ### Additional treatments & costs
    egg_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    embryo_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sperm_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    surrogacy = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    egg_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    embryo_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    sperm_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')
    surrogacy_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False, min_value=0, help_text='put price in USD ($)')

    egg_freezing_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    embryo_freezing_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    sperm_freezing_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    surrogacy_faqs = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)

    pro_is_published_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    class Meta:
        model = BasicClinic
        fields = [
        'clinicName',
        'defaultClinicCurrency',
        'ivf_treatment',
        'mild_ivf_treatment',
        'ovarian_ivf_treatment',
        'icsi_treatment',
        'iui_treatment',
        'ivf_treatment_cost',
        'mild_ivf_treatment_cost',
        'ovarian_ivf_treatment_cost',
        'icsi_treatment_cost',
        'iui_treatment_cost',
        'ivf_treatment_faqs',
        'mild_ivf_treatment_faqs',
        'ovarian_ivf_treatment_faqs',
        'icsi_treatment_faqs',
        'iui_treatment_faqs',
        'egg_donor_recipients',
        'known_egg_donor_recipients',
        'embryo_donor_recipients',
        'known_embryo_donor_recipients',
        'sperm_donor_recipients',
        'known_sperm_donor_recipients',
        'egg_donor_recipients_cost',
        'known_egg_donor_recipients_cost',
        'embryo_donor_recipients_cost',
        'known_embryo_donor_recipients_cost',
        'sperm_donor_recipients_cost',
        'known_sperm_donor_recipients_cost',
        'egg_donor_recipients_faqs',
        'known_egg_donor_recipients_faqs',
        'embryo_donor_recipients_faqs',
        'known_embryo_donor_recipients_faqs',
        'sperm_donor_recipients_faqs',
        'known_sperm_donor_recipients_faqs',
        'egg_freezing',
        'embryo_freezing',
        'sperm_freezing',
        'surrogacy',
        'egg_freezing_cost',
        'embryo_freezing_cost',
        'sperm_freezing_cost',
        'surrogacy_cost',
        'egg_freezing_faqs',
        'embryo_freezing_faqs',
        'sperm_freezing_faqs',
        'surrogacy_faqs',
        'pro_is_published_list_date',
        ]


class OwnerProInterestedForm(forms.ModelForm):
    owner_interested = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Check to be notified'))

    class Meta:
        model = ownerProInterested
        fields = [
        'owner_interested',
        ]


class CreatePackage(forms.ModelForm):
    packageclinic = forms.ModelChoiceField(queryset=BasicClinic.objects.all(), widget=forms.HiddenInput(attrs={'class': 'form-control',}), required=False)
    packagetitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Package name'))
    packagecategory = forms.CharField(widget=forms.Select(choices=CATEGORY_PACKAGE, attrs={'class': 'form-control',}), label=('Package category'))
    packagedesc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Package description'), max_length=800)
    packagecost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), label=('Package cost in your clinic currency'), min_value=0)
    package_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Package picture'))

    package_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    package_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    package_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    package_limit_days = forms.CharField(widget=forms.Select(choices=PACKAGE_TYPE, attrs={'class': 'form-control',}))

    is_package_active = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    class Meta:
        model = Package
        fields = [
        'packageclinic',
        'packagetitle',
        'packagecategory',
        'packagedesc',
        'packagecost',
        'package_pic',
        'package_list_date',
        'package_url',
        'package_phone',
        'package_limit_days',
        'is_package_active',
        ]


class CreatePackageEmail(forms.ModelForm):
    query_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    class Meta:
        model = BasicClinic
        fields = ['query_email']


class PostFormProUpdatePackage(forms.ModelForm):
    packagetitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Package name'))
    packagecategory = forms.CharField(widget=forms.Select(choices=CATEGORY_PACKAGE, attrs={'class': 'form-control',}), label=('Package category'))
    packagedesc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Package description'), max_length=800)
    packagecost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), label=('Package cost in your clinic currency'), min_value=0)
    package_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Package picture'))
    package_pic_delete = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    package_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    package_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    class Meta:
        model = Package
        fields = [
        'packagetitle',
        'packagecategory',
        'packagedesc',
        'packagecost',
        'package_update_date',
        'package_url',
        'package_phone',
        'package_pic',
        'package_pic_delete',
        ]


class ProlongPackage(forms.ModelForm):
    package_limit_days = forms.CharField(widget=forms.Select(choices=PACKAGE_TYPE, attrs={'class': 'form-control',}))

    class Meta:
        model = Package
        fields = [
        'package_limit_days',
        ]


class LiveChatForm(forms.ModelForm):
    clinicLiveChatChoice = forms.CharField(widget=forms.Select(choices=LIVE_CHAT_CHOICES, attrs={'class': 'form-control',}), required=False)

    class Meta:
        model = BasicClinic
        fields = [
        'clinicLiveChatChoice',
        ]


class LiveChatForm2(forms.ModelForm):
    clinicChatraCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Snippet Code'), required=False)
    clinicLiveChatCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Snippet Code'), required=False)
    clinicOlarkCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Snippet Code'), required=False)
    clinicTidioCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Snippet Code'), required=False)
    class Meta:
        model = BasicClinic
        fields = [
        'clinicChatraCode',
        'clinicLiveChatCode',
        'clinicOlarkCode',
        'clinicTidioCode',
        ]


class IndependentReviewForm(forms.ModelForm):
    clinicGoogleReviews = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Google reviews link'), required=False)
    clinicTrustPilotChoice = forms.CharField(widget=forms.Select(choices=TRUSTPILOT_CHOICES, attrs={'class': 'form-control',}), required=False)
    clinicTrustPilotID = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Trustpilot ID'), required=False)
    clinicTrustPilotDomain = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Trustpilot Domain'), required=False)

    class Meta:
        model = BasicClinic
        fields = [
        'clinicGoogleReviews',
        'clinicTrustPilotChoice',
        'clinicTrustPilotID',
        'clinicTrustPilotDomain',
        ]


class Bestarticleproposition(forms.ModelForm):
    best_article_country_boolean = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    best_article_country_actual_text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}, config_name="toolbar_bestclinicarticles"), required=False, label=('Best IVF clinics in Country - actual text'), max_length=3600)
    best_article_country_actual_prototype = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}, config_name="toolbar_bestclinicarticles"), required=False, label=('Best IVF clinics in Country - proposition text'), max_length=3600)

    best_article_city_boolean = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    best_article_city_actual_text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}, config_name="toolbar_bestclinicarticles"), required=False, label=('Best IVF clinics in Country - actual text'), max_length=3600)
    best_article_city_actual_prototype = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}, config_name="toolbar_bestclinicarticles"), required=False, label=('Best IVF clinics in Country - proposition text'), max_length=3600)

    class Meta:
        model = BasicClinic
        fields = [
        'best_article_country_boolean',
        'best_article_country_actual_text',
        'best_article_country_actual_prototype',

        'best_article_city_boolean',
        'best_article_city_actual_text',
        'best_article_city_actual_prototype',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['best_article_country_actual_text'].disabled = True


class Picclinicform(forms.ModelForm):
    clinic_pro_photo_1 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of your clinic'))
    clinic_pro_photo_1_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_2 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of your clinic'))
    clinic_pro_photo_2_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    clinic_pro_photo_3 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of your clinic'))
    clinic_pro_photo_3_del = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=('Delete image'))

    class Meta:
        model = BasicClinic
        fields = [
        'clinic_pro_photo_1',
        'clinic_pro_photo_2',
        'clinic_pro_photo_3',
        'clinic_pro_photo_1_del',
        'clinic_pro_photo_2_del',
        'clinic_pro_photo_3_del',
        ]


class Singleclinicbestarticleform(forms.ModelForm):
    clinic_world = forms.ModelChoiceField(queryset=None, required=True, empty_label="Choose your primary clinic", to_field_name='clinicName',)
    best_clinic_world_text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}, config_name="toolbar_bestclinicarticles"), required=False, label=('Best IVF clinics in World - your introduction'), max_length=1000)
    best_clinic_world_activated = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    class Meta:
        model = SingleClinicBestArticleText
        fields = [
        'clinic_world',
        'best_clinic_world_text',
        'best_clinic_world_activated',
        ]

    def __init__(self, current_user, *args, **kwargs):
        super(Singleclinicbestarticleform, self).__init__(*args, **kwargs)
        self.fields['clinic_world'].queryset = BasicClinic.objects.all().filter(clinicOwner=current_user)


class Singleclinicbestarticleupdateform(forms.ModelForm):
    clinic_world = forms.ModelChoiceField(queryset=None, required=True, empty_label="Choose different clinic", to_field_name='clinicName',)
    best_clinic_world_text = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}, config_name="toolbar_bestclinicarticles"), required=False, label=('Best IVF clinics in World - your introduction'), max_length=1000)
    best_clinic_world_activated = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    class Meta:
        model = SingleClinicBestArticleText
        fields = [
        'clinic_world',
        'best_clinic_world_text',
        'best_clinic_world_activated',
        ]

    def __init__(self, current_user, *args, **kwargs):
        super(Singleclinicbestarticleupdateform, self).__init__(*args, **kwargs)
        self.fields['clinic_world'].queryset = BasicClinic.objects.all().filter(clinicOwner=current_user)