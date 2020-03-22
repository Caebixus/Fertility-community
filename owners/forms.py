from django import forms
from clinic.models import BasicClinic
from .models import ownerProInterested
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput
from django.forms.widgets import datetime
from ckeditor.widgets import CKEditorWidget

class CreateClinic(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'))
    clinicTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False, label=('Clinics Title'))
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, label=('Clinics Description'))

    contact_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    clinicStreetAddress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics street address'))
    clinicCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics city'))

    CATEGORY_CHOICES_STATES = (
        ('select', 'select'),
        ('Afghanistan', 'Afghanistan'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('The Bahamas', 'The Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cape Verde', 'Cape Verde'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo, Republic', 'Congo, Republic'),
        ('Congo, Democratic Republic', 'Congo, Democratic Republic'),
        ('Costa Rica', 'Costa Rica'),
        ('Cote d’Ivoire', 'Cote d’Ivoire'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('East Timor (Timor-Leste)', 'East Timor (Timor-Leste)'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Gabon', 'Gabon'),
        ('The Gambia', 'The Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Greece', 'Greece'),
        ('Grenada', 'Grenada'),
        ('Guatemala', 'Guatemala'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Honduras', 'Honduras'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea, South', 'Korea, South'),
        ('Kosovo', 'Kosovo'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Laos', 'Laos'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macedonia', 'Macedonia'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mexico', 'Mexico'),
        ('Micronesia, Federated States', 'Micronesia, Federated States'),
        ('Moldova', 'Moldova'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar (Burma)', 'Myanmar (Burma)'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Romania', 'Romania'),
        ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
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
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Sudan', 'South Sudan'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
    )
    clinicState = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_STATES, attrs={'class': 'form-control',}), label=('Clinics state'))
    clinicPostalCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics postal code'))

    clinicEnglish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('English speaking personal'))
    clinicSpanish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Spanish speaking personal'))
    clinicPortuguese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Portguesse speaking personal'))
    clinicRussian = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Russian speaking personal'))
    clinicGerman = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('German speaking personal'))
    clinicChinese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Chinese speaking personal'))

    CATEGORY_CHOICES_CURRENCY = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        )
    defaultClinicCurrency = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_CURRENCY, attrs={'class': 'form-control',}))

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

    is_published = forms.BooleanField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)
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
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, label=('Clinics Description'))
    treatmentLimitations = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), required=False, label=('Clinics treatment limitations'))

    clinic_pro_logo_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Clinics Logo'))

    contact_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    contact_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    clinicStreetAddress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics street address'))
    clinicCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics city'))

    CATEGORY_CHOICES_STATES = (
        ('Afghanistan', 'Afghanistan'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('The Bahamas', 'The Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cape Verde', 'Cape Verde'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo, Republic', 'Congo, Republic'),
        ('Congo, Democratic Republic', 'Congo, Democratic Republic'),
        ('Costa Rica', 'Costa Rica'),
        ('Cote d’Ivoire', 'Cote d’Ivoire'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('East Timor (Timor-Leste)', 'East Timor (Timor-Leste)'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Gabon', 'Gabon'),
        ('The Gambia', 'The Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Greece', 'Greece'),
        ('Grenada', 'Grenada'),
        ('Guatemala', 'Guatemala'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Honduras', 'Honduras'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea, South', 'Korea, South'),
        ('Kosovo', 'Kosovo'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Laos', 'Laos'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macedonia', 'Macedonia'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mexico', 'Mexico'),
        ('Micronesia, Federated States', 'Micronesia, Federated States'),
        ('Moldova', 'Moldova'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar (Burma)', 'Myanmar (Burma)'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Romania', 'Romania'),
        ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
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
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Sudan', 'South Sudan'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
    )
    clinicState = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_STATES, attrs={'class': 'form-control',}), label=('Clinics state'))

    CATEGORY_CHOICES_US_REGIONS = (
        ('Alabama', 'Alabama'),
        ('Alaska', 'Alaska'),
        ('Arizona', 'Arizona'),
        ('Arkansas', 'Arkansas'),
        ('California', 'California'),
        ('Colorado', 'Colorado'),
        ('Connecticut', 'Connecticut'),
        ('Delaware', 'Delaware'),
        ('Georgia', 'Georgia'),
        ('Hawaii', 'Hawaii'),
        ('Idaho', 'Idaho'),
        ('Illinois', 'Illinois'),
        ('Indiana', 'Indiana'),
        ('Iowa', 'Iowa'),
        ('Kansas', 'Kansas'),
        ('Kentucky', 'Kentucky'),
        ('Louisiana', 'Louisiana'),
        ('Maine', 'Maine'),
        ('Maryland', 'Maryland'),
        ('Massachusetts', 'Massachusetts'),
        ('Michigan', 'Michigan'),
        ('Minnesota', 'Minnesota'),
        ('Mississippi', 'Mississippi'),
        ('Missouri', 'Missouri'),
        ('Nebraska', 'Nebraska'),
        ('New Hampshire', 'New Hampshire'),
        ('New Jersey', 'New Jersey'),
        ('New Mexico', 'New Mexico'),
        ('New York', 'New York'),
        ('North Carolina', 'North Carolina'),
        ('North Dakota', 'North Dakota'),
        ('Ohio', 'Ohio'),
        ('Oklahoma', 'Oklahoma'),
        ('Oregon', 'Oregon'),
        ('Pennsylvania', 'Pennsylvania'),
        ('Rhode Island', 'Rhode Island'),
        ('South Carolina', 'South Carolina'),
        ('South Dakota', 'South Dakota'),
        ('Tennessee', 'Tennessee'),
        ('Texas', 'Texas'),
        ('Utah', 'Utah'),
        ('Vermont', 'Vermont'),
        ('Virginia', 'Virginia'),
        ('Washington', 'Washington'),
        ('West Virginia', 'West Virginia'),
        ('Wisconsin', 'Wisconsin'),
        ('Wyoming', 'Wyoming'),
        ('District of Columbia', 'District of Columbia'),
        )
    clinicRegion = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_US_REGIONS, attrs={'class': 'form-control',}), label=('Clinics Region/Country'))
    clinicPostalCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics postal code'))

    clinicEnglish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('English speaking personal'))
    clinicSpanish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Spanish speaking personal'))
    clinicPortuguese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Portguesse speaking personal'))
    clinicRussian = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Russian speaking personal'))
    clinicGerman = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('German speaking personal'))
    clinicChinese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Chinese speaking personal'))

    CATEGORY_CHOICES_CURRENCY = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        )
    defaultClinicCurrency = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_CURRENCY, attrs={'class': 'form-control',}))

    is_published_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

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
        'clinic_pro_logo_pic',
        'contact_url',
        'contact_phone',
        'contact_email',
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
        ]


class PostFormPro(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'))
    clinicTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Title'))
    description = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics Description'))
    treatmentLimitations = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics treatment limitations'))

    clinic_staff = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Clinics staff'), required=False)

    clinic_pro_promotion_name = forms.CharField(widget=CKEditorWidget(attrs={'class': 'form-control',}), label=('Promotion'), required=False)

    clinic_pro_logo_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Clinics Logo'))
    clinic_pro_main_pic = forms.ImageField(widget=forms.FileInput(), required=False, label=('Clinics Main picture'))

    contact_url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)
    contact_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), required=False)

    clinicStreetAddress = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    clinicCity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    clinicState = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    clinicPostalCode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))

    clinicEnglish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('English speaking personal'))
    clinicSpanish = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Spanish speaking personal'))
    clinicPortuguese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Portguesse speaking personal'))
    clinicRussian = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Russian speaking personal'))
    clinicGerman = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('German speaking personal'))
    clinicChinese = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Chinese speaking personal'))

    CATEGORY_CHOICES_CURRENCY = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        )
    defaultClinicCurrency = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_CURRENCY, attrs={'class': 'form-control',}))

    pro_is_published_list_date = forms.DateTimeField(widget=forms.HiddenInput(attrs={'class': 'form-control',}), initial=False, required=False)

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
        'contact_phone',
        'contact_email',
        'clinicStreetAddress',
        'clinicCity',
        'clinicState',
        'clinicPostalCode',
        'clinicEnglish',
        'clinicSpanish',
        'clinicPortuguese',
        'clinicRussian',
        'clinicGerman',
        'clinicChinese',
        'defaultClinicCurrency',
        'pro_is_published',
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
        'pro_is_published',
        'pro_is_published_list_date',
        ]

class OwnerProInterestedForm(forms.ModelForm):
    owner_interested = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False, label=('Check to be notified'))

    class Meta:
        model = ownerProInterested
        fields = [
        'owner_interested',
        ]
