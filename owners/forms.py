from django import forms
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from .models import ownerProInterested
from packages.models import Packages, Package
from packages.choices import CATEGORY_PACKAGE
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_CZ_CITIES, CATEGORY_CHOICES_UK_CITIES
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.forms.widgets import HiddenInput
from django.forms.widgets import datetime
from ckeditor.widgets import CKEditorWidget

CATEGORY_CHOICES_CURRENCY = (
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('GBP', 'GBP'),
    )

HOURS = (
    ("00:00", "00:00"),
    ("00:30", "00:30"),
    ("01:00", "01:00"),
    ("01:30", "01:30"),
    ("02:00", "02:00"),
    ("02:30", "02:30"),
    ("03:00", "03:00"),
    ("03:30", "03:30"),
    ("04:00", "04:00"),
    ("04:30", "04:30"),
    ("05:00", "05:00"),
    ("05:30", "05:30"),
    ("06:00", "06:00"),
    ("06:30", "06:30"),
    ("07:00", "07:00"),
    ("07:30", "07:30"),
    ("08:00", "08:00"),
    ("08:30", "08:30"),
    ("09:00", "09:00"),
    ("09:30", "09:30"),
    ("10:00", "10:00"),
    ("10:30", "10:30"),
    ("11:00", "11:00"),
    ("11:30", "11:30"),
    ("12:00", "12:00"),
    ("12:30", "12:30"),
    ("13:00", "13:00"),
    ("13:30", "13:30"),
    ("14:00", "14:00"),
    ("14:30", "14:30"),
    ("15:00", "15:00"),
    ("15:30", "15:30"),
    ("16:00", "16:00"),
    ("16:30", "16:30"),
    ("17:00", "17:00"),
    ("17:30", "17:30"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30"),
    ("21:00", "21:00"),
    ("21:30", "21:30"),
    ("22:00", "22:00"),
    ("22:30", "22:30"),
    ("23:00", "23:00"),
    ("23:30", "23:30"),
    ("CLOSED", "CLOSED"),
)

CATEGORY_CHOICES_STATES = (
    ('DF', 'Select State'),
    ('US', 'United States'),
    ('UK', 'United Kingdom'),
    ('CZ', 'Czech Republic'),
)

CATEGORY_CHOICES_WORLD_STATES = (
    ('Afghanistan', 'Afghanistan'),
    ('Åland Islands', 'Åland Islands'),
    ('Albania', 'Albania'),
    ('Algeria', 'Algeria'),
    ('American Samoa', 'American Samoa'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Anguilla', 'Anguilla'),
    ('Antigua and Barbuda', 'Antigua and Barbuda'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Aruba', 'Aruba'),
    ('Australia', 'Australia'),
    ('Austria', 'Austria'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bahrain', 'Bahrain'),
    ('Bahamas', 'Bahamas'),
    ('Bangladesh', 'Bangladesh'),
    ('Barbados', 'Barbados'),
    ('Belarus', 'Belarus'),
    ('Belgium', 'Belgium'),
    ('Belize', 'Belize'),
    ('Benin', 'Benin'),
    ('Bermuda', 'Bermuda'),
    ('Bhutan', 'Bhutan'),
    ('Bolivia', 'Bolivia'),
    ('Bonaire, Sint Eustatius and Saba', 'Bonaire, Sint Eustatius and Saba'),
    ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
    ('Botswana', 'Botswana'),
    ('Bouvet Island', 'Bouvet Island'),
    ('Brazil', 'Brazil'),
    ('British Indian Ocean Territory', 'British Indian Ocean Territory'),
    ('Brunei Darussalam', 'Brunei Darussalam'),
    ('Bulgaria', 'Bulgaria'),
    ('Burkina Faso', 'Burkina Faso'),
    ('Burundi', 'Burundi'),
    ('Cambodia', 'Cambodia'),
    ('Cameroon', 'Cameroon'),
    ('Canada', 'Canada'),
    ('Cape Verde', 'Cape Verde'),
    ('Cayman Islands', 'Cayman Islands'),
    ('Central African Republic', 'Central African Republic'),
    ('Chad', 'Chad'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Christmas Island', 'Christmas Island'),
    ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
    ('Colombia', 'Colombia'),
    ('Comoros', 'Comoros'),
    ('Congo', 'Congo'),
    ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'),
    ('Cook Islands', 'Cook Islands'),
    ('Costa Rica', 'Costa Rica'),
    ('Croatia', 'Croatia'),
    ('Cuba', 'Cuba'),
    ('Curaçao', 'Curaçao'),
    ('Cyprus', 'Cyprus'),
    ('Czech Republic', 'Czech Republic'),
    ('Denmark', 'Denmark'),
    ('Djibouti', 'Djibouti'),
    ('Dominica', 'Dominica'),
    ('Dominican Republic', 'Dominican Republic'),
    ('Ecuador', 'Ecuador'),
    ('Egypt', 'Egypt'),
    ('El Salvador', 'El Salvador'),
    ('Equatorial Guinea', 'Equatorial Guinea'),
    ('Eritrea', 'Eritrea'),
    ('Estonia', 'Estonia'),
    ('Ethiopia', 'Ethiopia'),
    ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
    ('Faroe Islands', 'Faroe Islands'),
    ('Fiji', 'Fiji'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('French Guiana', 'French Guiana'),
    ('French Polynesia', 'French Polynesia'),
    ('French Southern Territories', 'French Southern Territories'),
    ('Gabon', 'Gabon'),
    ('Gambia', 'Gambia'),
    ('Georgia', 'Georgia'),
    ('Germany', 'Germany'),
    ('Ghana', 'Ghana'),
    ('Gibraltar', 'Gibraltar'),
    ('Greece', 'Greece'),
    ('Greenland', 'Greenland'),
    ('Grenada', 'Grenada'),
    ('Guadeloupe', 'Guadeloupe'),
    ('Guam', 'Guam'),
    ('Guatemala', 'Guatemala'),
    ('Guernsey', 'Guernsey'),
    ('Guinea', 'Guinea'),
    ('Guinea-Bissau', 'Guinea-Bissau'),
    ('Guyana', 'Guyana'),
    ('Haiti', 'Haiti'),
    ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'),
    ('Vatican City State', 'Vatican City State'),
    ('Honduras', 'Honduras'),
    ('Hong Kong', 'Hong Kong'),
    ('Hungary', 'Hungary'),
    ('Iceland', 'Iceland'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Ireland', 'Ireland'),
    ('Isle of Man', 'Isle of Man'),
    ('Israel', 'Israel'),
    ('Italy', 'Italy'),
    ('Jamaica', 'Jamaica'),
    ('Japan', 'Japan'),
    ('Jersey', 'Jersey'),
    ('Jordan', 'Jordan'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Kenya', 'Kenya'),
    ('Kiribati', 'Kiribati'),
    ('Republic of Korea', 'Republic of Korea'),
    ('Kuwait', 'Kuwait'),
    ('Kyrgyzstan', 'Kyrgyzstan'),
    ('Lao Peoples Democratic Republic', 'Lao Peoples Democratic Republic'),
    ('Latvia', 'Latvia'),
    ('Lebanon', 'Lebanon'),
    ('Lesotho', 'Lesotho'),
    ('Liberia', 'Liberia'),
    ('Liechtenstein', 'Liechtenstein'),
    ('Lithuania', 'Lithuania'),
    ('Luxembourg', 'Luxembourg'),
    ('Macao', 'Macao'),
    ('Macedonia', 'Macedonia'),
    ('Madagascar', 'Madagascar'),
    ('Malawi', 'Malawi'),
    ('Malaysia', 'Malaysia'),
    ('Maldives', 'Maldives'),
    ('Mali', 'Mali'),
    ('Malta', 'Malta'),
    ('Marshall Islands', 'Marshall Islands'),
    ('Martinique', 'Martinique'),
    ('Mauritania', 'Mauritania'),
    ('Mauritius', 'Mauritius'),
    ('Mayotte', 'Mayotte'),
    ('Mexico', 'Mexico'),
    ('Federated States of Micronesia', 'Federated States of Micronesia'),
    ('Republic of Moldova', 'Republic of Moldova'),
    ('Monaco', 'Monaco'),
    ('Mongolia', 'Mongolia'),
    ('Montenegro', 'Montenegro'),
    ('Montserrat', 'Montserrat'),
    ('Morocco', 'Morocco'),
    ('Mozambique', 'Mozambique'),
    ('Myanmar', 'Myanmar'),
    ('Namibia', 'Namibia'),
    ('Nauru', 'Nauru'),
    ('Nepal', 'Nepal'),
    ('Netherlands', 'Netherlands'),
    ('New Caledonia', 'New Caledonia'),
    ('New Zealand', 'New Zealand'),
    ('Nicaragua', 'Nicaragua'),
    ('Niger', 'Niger'),
    ('Nigeria', 'Nigeria'),
    ('Niue', 'Niue'),
    ('Norfolk Island', 'Norfolk Island'),
    ('Northern Mariana Islands', 'Northern Mariana Islands'),
    ('Norway', 'Norway'),
    ('Oman', 'Oman'),
    ('Palau', 'Palau'),
    ('Panama', 'Panama'),
    ('Papua New Guinea', 'Papua New Guinea'),
    ('Paraguay', 'Paraguay'),
    ('Peru', 'Peru'),
    ('Philippines', 'Philippines'),
    ('Pitcairn', 'Pitcairn'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Puerto Rico', 'Puerto Rico'),
    ('Qatar', 'Qatar'),
    ('Réunion', 'Réunion'),
    ('Romania', 'Romania'),
    ('Russian Federation', 'Russian Federation'),
    ('Rwanda', 'Rwanda'),
    ('Saint Barthélemy', 'Saint Barthélemy'),
    ('Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'),
    ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
    ('Saint Lucia', 'Saint Lucia'),
    ('Saint Martin (French part)', 'Saint Martin (French part)'),
    ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
    ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
    ('Samoa', 'Samoa'),
    ('San Marino', 'San Marino'),
    ('Sao Tome and Principe', 'Sao Tome and Principe'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Senegal', 'Senegal'),
    ('Serbia', 'Serbia'),
    ('Seychelles', 'Seychelles'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Singapore', 'Singapore'),
    ('Sint Maarten (Dutch part)', 'Sint Maarten (Dutch part)'),
    ('Slovakia', 'Slovakia'),
    ('Slovenia', 'Slovenia'),
    ('Solomon Islands', 'Solomon Islands'),
    ('Somalia', 'Somalia'),
    ('South Africa', 'South Africa'),
    ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'),
    ('South Sudan', 'South Sudan'),
    ('Spain', 'Spain'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Sudan', 'Sudan'),
    ('Suriname', 'Suriname'),
    ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'),
    ('Swaziland', 'Swaziland'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Syrian Arab Republic', 'Syrian Arab Republic'),
    ('Taiwan, Province of China', 'Taiwan, Province of China'),
    ('Tajikistan', 'Tajikistan'),
    ('United Republic of Tanzania', 'United Republic of Tanzania'),
    ('Thailand', 'Thailand'),
    ('Timor Leste', 'Timor Leste'),
    ('Togo', 'Togo'),
    ('Tokelau', 'Tokelau'),
    ('Tonga', 'Tonga'),
    ('Trinidad and Tobago', 'Trinidad and Tobago'),
    ('Tunisia', 'Tunisia'),
    ('Turkey', 'Turkey'),
    ('Turkmenistan', 'Turkmenistan'),
    ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
    ('Tuvalu', 'Tuvalu'),
    ('Uganda', 'Uganda'),
    ('Ukraine', 'Ukraine'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('United Kingdom', 'United Kingdom'),
    ('United States', 'United States'),
    ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'),
    ('Uruguay', 'Uruguay'),
    ('Uzbekistan', 'Uzbekistan'),
    ('Vanuatu', 'Vanuatu'),
    ('Viet Nam', 'Viet Nam'),
    ('British Virgin Islands', 'British Virgin Islands'),
    ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'),
    ('Wallis and Futuna', 'Wallis and Futuna'),
    ('Western Sahara', 'Western Sahara'),
    ('Yemen', 'Yemen'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
    )

CATEGORY_CHOICES_US_REGION = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NV', 'Nevada'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
    ('DC', 'District of Columbia'),
)


class CreateClinic(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'))
    clinicTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False, label=('Clinics Title'))
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, label=('Clinics Description'), max_length=800)

    contact_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    clinicStreetAddress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics street address'))
    clinicCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics city'))

    clinicState = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_STATES, attrs={'class': 'form-control',}), label=('Clinics state'))

    clinicRegion = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_US_REGION, attrs={'class': 'form-control',}), label=('Clinics Region/Country'))

    clinicPostalCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics postal code'))

    clinicEnglish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('English speaking personal'))
    clinicSpanish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Spanish speaking personal'))
    clinicPortuguese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Portguesse speaking personal'))
    clinicRussian = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Russian speaking personal'))
    clinicGerman = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('German speaking personal'))
    clinicChinese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Chinese speaking personal'))

    defaultClinicCurrency = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_CURRENCY, attrs={'class': 'form-control',}))

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
        'defaultClinicCurrency',
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
        ]


class PostForm(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'))
    clinicTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False, label=('Clinics Title'))

    clinic_pro_logo_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Clinics Logo'))

    contact_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    contact_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    fertilitycommunity_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    clinicStreetAddress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics street address'))
    clinicCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics city'))

    clinicState = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_WORLD_STATES, attrs={'class': 'form-control',}), label=('Clinics state'))

    clinicRegion = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_US_REGION, attrs={'class': 'form-control',}), label=('Clinics Region/Country'))
    clinicPostalCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics postal code'))

    clinicEnglish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('English speaking personal'))
    clinicSpanish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Spanish speaking personal'))
    clinicPortuguese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Portguesse speaking personal'))
    clinicRussian = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Russian speaking personal'))
    clinicGerman = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('German speaking personal'))
    clinicChinese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Chinese speaking personal'))

    clinic_pro_photo_1 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_2 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_3 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_4 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_5 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_6 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))

    defaultClinicCurrency = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_CURRENCY, attrs={'class': 'form-control',}))

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

    class Meta:
        model = BasicClinic
        fields = [
        'clinicName',
        'clinicTitle',
        'clinic_pro_logo_pic',
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
        'defaultClinicCurrency',
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
        'clinic_pro_photo_2',
        'clinic_pro_photo_3',
        'clinic_pro_photo_4',
        'clinic_pro_photo_5',
        'clinic_pro_photo_6',
        ]


class UpdatePrice(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'), required=False)
    ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    mild_ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    ovarian_ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    icsi_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    iui_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    egg_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    embryo_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    mild_ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    ovarian_ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    icsi_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    iui_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    egg_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    embryo_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    egg_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    embryo_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sperm_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    surrogacy = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sperm_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    egg_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    embryo_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    sperm_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    surrogacy_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    sperm_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    single_woman_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    reciprocal_ivf = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    hiv_patients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sex_selection = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    package1title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    package1category = forms.CharField(widget=forms.Select(choices=CATEGORY_PACKAGE, attrs={'class': 'form-control',}), required=False,)
    package1desc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    package1cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    is_published_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    class Meta:
        model = BasicClinic
        fields = [
        'clinicName',
        'ivf_treatment',
        'mild_ivf_treatment',
        'ovarian_ivf_treatment',
        'icsi_treatment',
        'iui_treatment',
        'egg_donor_recipients',
        'embryo_donor_recipients',
        'ivf_treatment_cost',
        'mild_ivf_treatment_cost',
        'ovarian_ivf_treatment_cost',
        'icsi_treatment_cost',
        'iui_treatment_cost',
        'egg_donor_recipients_cost',
        'embryo_donor_recipients_cost',
        'egg_freezing',
        'embryo_freezing',
        'sperm_freezing',
        'surrogacy',
        'sperm_donor_recipients',
        'egg_freezing_cost',
        'embryo_freezing_cost',
        'sperm_freezing_cost',
        'surrogacy_cost',
        'sperm_donor_recipients_cost',
        'single_woman_treatment',
        'reciprocal_ivf',
        'hiv_patients',
        'sex_selection',
        'is_published_list_date',
        'package1title',
        'package1desc',
        'package1cost',
        ]


class PostFormPro(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'))
    clinicTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Title'))
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics Description'), required=False, max_length=800)
    treatmentLimitations = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics treatment limitations'), required=False, max_length=800)

    clinic_staff = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics staff'), required=False, max_length=300)

    clinic_pro_promotion_name = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Promotion'), required=False, max_length=80)

    clinic_pro_logo_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Clinics Logo'))
    clinic_pro_main_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Clinics Main picture'))

    contact_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    contact_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    query_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    fertilitycommunity_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    clinicStreetAddress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    clinicCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    clinicState = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_STATES, attrs={'class': 'form-control',}), label=('Clinics state'))

    clinicRegion = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_US_REGION, attrs={'class': 'form-control',}), label=('Clinics Region/Country'))

    clinicPostalCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    clinicEnglish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('English speaking personal'))
    clinicSpanish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Spanish speaking personal'))
    clinicPortuguese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Portguesse speaking personal'))
    clinicRussian = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Russian speaking personal'))
    clinicGerman = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('German speaking personal'))
    clinicChinese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Chinese speaking personal'))

    team1name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('First team member'), required=False)
    team1pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    team2name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Second team member'), required=False)
    team2pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of second team member'))
    team3name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Third team member'), required=False)
    team3pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of third team member'))

    clinic_pro_photo_1 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_2 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_3 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_4 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_5 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))
    clinic_pro_photo_6 = forms.ImageField(widget=forms.FileInput(), required=False, label=('Picture of first team member'))

    defaultClinicCurrency = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_CURRENCY, attrs={'class': 'form-control',}))

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
        'defaultClinicCurrency',
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
        'team2name',
        'team2pic',
        'team3name',
        'team3pic',
        'clinic_pro_photo_1',
        'clinic_pro_photo_2',
        'clinic_pro_photo_3',
        'clinic_pro_photo_4',
        'clinic_pro_photo_5',
        'clinic_pro_photo_6',
        ]

class UpdatePricePro(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'), required=False)
    ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    mild_ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    ovarian_ivf_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    icsi_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    iui_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    egg_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    embryo_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    mild_ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    ovarian_ivf_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    icsi_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    iui_treatment_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    egg_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    embryo_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    egg_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    embryo_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sperm_freezing = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    surrogacy = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    sperm_donor_recipients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    egg_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    embryo_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    sperm_freezing_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    surrogacy_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)
    sperm_donor_recipients_cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    single_woman_treatment = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    reciprocal_ivf = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
    hiv_patients = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)

    package1title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    package1category = forms.CharField(widget=forms.Select(choices=CATEGORY_PACKAGE, attrs={'class': 'form-control',}), required=False,)
    package1desc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    package1cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    package2title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    package2category = forms.CharField(widget=forms.Select(choices=CATEGORY_PACKAGE, attrs={'class': 'form-control',}), required=False,)
    package2desc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    package2cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    package3title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    package3category = forms.CharField(widget=forms.Select(choices=CATEGORY_PACKAGE, attrs={'class': 'form-control',}), required=False,)
    package3desc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    package3cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    package4title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    package4category = forms.CharField(widget=forms.Select(choices=CATEGORY_PACKAGE, attrs={'class': 'form-control',}), required=False,)
    package4desc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    package4cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    package5title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    package5category = forms.CharField(widget=forms.Select(choices=CATEGORY_PACKAGE, attrs={'class': 'form-control',}), required=False,)
    package5desc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    package5cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    package6title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    package6category = forms.CharField(widget=forms.Select(choices=CATEGORY_PACKAGE, attrs={'class': 'form-control',}), required=False)
    package6desc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, max_length=500)
    package6cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), required=False)

    pro_is_published_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    class Meta:
        model = BasicClinic
        fields = [
        'clinicName',
        'ivf_treatment',
        'mild_ivf_treatment',
        'ovarian_ivf_treatment',
        'icsi_treatment',
        'iui_treatment',
        'egg_donor_recipients',
        'embryo_donor_recipients',
        'ivf_treatment_cost',
        'mild_ivf_treatment_cost',
        'ovarian_ivf_treatment_cost',
        'icsi_treatment_cost',
        'iui_treatment_cost',
        'egg_donor_recipients_cost',
        'embryo_donor_recipients_cost',
        'egg_freezing',
        'embryo_freezing',
        'sperm_freezing',
        'surrogacy',
        'sperm_donor_recipients',
        'egg_freezing_cost',
        'embryo_freezing_cost',
        'sperm_freezing_cost',
        'surrogacy_cost',
        'sperm_donor_recipients_cost',
        'single_woman_treatment',
        'reciprocal_ivf',
        'hiv_patients',
        'pro_is_published_list_date',
        'package1title',
        'package1category',
        'package1desc',
        'package1cost',
        'package2title',
        'package2category',
        'package2desc',
        'package2cost',
        'package3title',
        'package3category',
        'package3desc',
        'package3cost',
        'package4title',
        'package4category',
        'package4desc',
        'package4cost',
        'package5title',
        'package5category',
        'package5desc',
        'package5cost',
        'package6title',
        'package6category',
        'package6desc',
        'package6cost',
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
    packagecost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), label=('Package cost in your clinic currency'))

    package_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

    class Meta:
        model = Package
        fields = [
        'packageclinic',
        'packagetitle',
        'packagecategory',
        'packagedesc',
        'packagecost',
        'package_list_date',
        ]

class CreatePackageEmail(forms.ModelForm):
    query_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    class Meta:
        model = BasicClinic
        fields = ['query_email']

class PostFormProUpdatePackage(forms.ModelForm):
    packageclinic = forms.ModelChoiceField(queryset=BasicClinic.objects.all(), widget=forms.HiddenInput(attrs={'class': 'form-control',}), required=False)
    packagetitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Package name'))
    packagecategory = forms.CharField(widget=forms.Select(choices=CATEGORY_PACKAGE, attrs={'class': 'form-control',}), label=('Package category'))
    packagedesc = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Package description'), max_length=800)
    packagecost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control',}), label=('Package cost in your clinic currency'))

    class Meta:
        model = Package
        fields = [
        'packageclinic',
        'packagetitle',
        'packagecategory',
        'packagedesc',
        'packagecost',
        'package_update_date',
        ]
