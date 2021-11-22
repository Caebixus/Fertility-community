from django import forms
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from clinic.models import BasicClinic, LIVE_CHAT_CHOICES, TRUSTPILOT_CHOICES, AcceptedPayment, AcceptedCurrency
from .models import ownerProInterested
from packages.models import Packages, Package
from packages.packageChoices import CATEGORY_PACKAGE
from search.choices import CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES, CATEGORY_CHOICES_CZ_CITIES, CATEGORY_CHOICES_SP_CITIES, CATEGORY_CHOICES_IN_CITIES, CATEGORY_CHOICES_GR_CITIES, CATEGORY_CHOICES_CY_CITIES, CATEGORY_CHOICES_MX_CITIES
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.forms.widgets import HiddenInput
from django.forms.widgets import datetime
from ckeditor.widgets import CKEditorWidget

CATEGORY_CHOICES_CURRENCY = (
    ('AED', 'AED'),
    ('AFN', 'AFN'),
    ('ALL', 'ALL'),
    ('AMD', 'AMD'),
    ('ANG', 'ANG'),
    ('AOA', 'AOA'),
    ('ARS', 'ARS'),
    ('AUD', 'AUD'),
    ('AWG', 'AWG'),
    ('AZN', 'AZN'),
    ('BAM', 'BAM'),
    ('BBD', 'BBD'),
    ('BDT', 'BDT'),
    ('BGN', 'BGN'),
    ('BHD', 'BHD'),
    ('BIF', 'BIF'),
    ('BMD', 'BMD'),
    ('BND', 'BND'),
    ('BOB', 'BOB'),
    ('BRL', 'BRL'),
    ('BSD', 'BSD'),
    ('BTN', 'BTN'),
    ('BWP', 'BWP'),
    ('BYN', 'BYN'),
    ('BZD', 'BZD'),
    ('CAD', 'CAD'),
    ('CDF', 'CDF'),
    ('CLP', 'CLP'),
    ('CNY', 'CNY'),
    ('COP', 'COP'),
    ('CRC', 'CRC'),
    ('CUP', 'CUP'),
    ('CVE', 'CVE'),
    ('CZK', 'CZK'),
    ('DJF', 'DJF'),
    ('DKK', 'DKK'),
    ('DOP', 'DOP'),
    ('DZD', 'DZD'),
    ('EGP', 'EGP'),
    ('ERN', 'ERN'),
    ('ETB', 'ETB'),
    ('EUR', 'EUR'),
    ('FJD', 'FJD'),
    ('FKP', 'FKP'),
    ('GBP', 'GBP'),
    ('GEL', 'GEL'),
    ('GHS', 'GHS'),
    ('GIP', 'GIP'),
    ('GMD', 'GMD'),
    ('GNF', 'GNF'),
    ('GTQ', 'GTQ'),
    ('GYD', 'GYD'),
    ('HKD', 'HKD'),
    ('HNL', 'HNL'),
    ('HRK', 'HRK'),
    ('HTG', 'HTG'),
    ('HUF', 'HUF'),
    ('CHF', 'CHF'),
    ('CHW', 'CHW'),
    ('IDR', 'IDR'),
    ('ILS', 'ILS'),
    ('INR', 'INR'),
    ('IQD', 'IQD'),
    ('IRR', 'IRR'),
    ('ISK', 'ISK'),
    ('JMD', 'JMD'),
    ('JOD', 'JOD'),
    ('JPY', 'JPY'),
    ('KES', 'KES'),
    ('KGS', 'KGS'),
    ('KHR', 'KHR'),
    ('KMF', 'KMF'),
    ('KRW', 'KRW'),
    ('KWD', 'KWD'),
    ('KYD', 'KYD'),
    ('KZT', 'KZT'),
    ('LAK', 'LAK'),
    ('LBP', 'LBP'),
    ('LKR', 'LKR'),
    ('LRD', 'LRD'),
    ('LSL', 'LSL'),
    ('MAD', 'MAD'),
    ('MDL', 'MDL'),
    ('MGA', 'MGA'),
    ('MKD', 'MKD'),
    ('MMK', 'MMK'),
    ('MNT', 'MNT'),
    ('MOP', 'MOP'),
    ('MRU', 'MRU'),
    ('MUR', 'MUR'),
    ('MVR', 'MVR'),
    ('MWK', 'MWK'),
    ('MXN', 'MXN'),
    ('MYR', 'MYR'),
    ('MZN', 'MZN'),
    ('NAD', 'NAD'),
    ('NGN', 'NGN'),
    ('NIO', 'NIO'),
    ('NOK', 'NOK'),
    ('NPR', 'NPR'),
    ('NZD', 'NZD'),
    ('OMR', 'OMR'),
    ('PAB', 'PAB'),
    ('PEN', 'PEN'),
    ('PGK', 'PGK'),
    ('PHP', 'PHP'),
    ('PKR', 'PKR'),
    ('PLN', 'PLN'),
    ('PYG', 'PYG'),
    ('QAR', 'QAR'),
    ('RON', 'RON'),
    ('RSD', 'RSD'),
    ('RUB', 'RUB'),
    ('RWF', 'RWF'),
    ('SAR', 'SAR'),
    ('SBD', 'SBD'),
    ('SCR', 'SCR'),
    ('SDG', 'SDG'),
    ('SEK', 'SEK'),
    ('SGD', 'SGD'),
    ('SHP', 'SHP'),
    ('SLL', 'SLL'),
    ('SOS', 'SOS'),
    ('SRD', 'SRD'),
    ('SSP', 'SSP'),
    ('STN', 'STN'),
    ('SVC', 'SVC'),
    ('SYP', 'SYP'),
    ('SZL', 'SZL'),
    ('THB', 'THB'),
    ('TJS', 'TJS'),
    ('TMT', 'TMT'),
    ('TND', 'TND'),
    ('TOP', 'TOP'),
    ('TRY', 'TRY'),
    ('TTD', 'TTD'),
    ('TWD', 'TWD'),
    ('TZS', 'TZS'),
    ('UAH', 'UAH'),
    ('UGX', 'UGX'),
    ('USD', 'USD'),
    ('USN', 'USN'),
    ('UYI', 'UYI'),
    ('UYU', 'UYU'),
    ('UYW', 'UYW'),
    ('UZS', 'UZS'),
    ('VES', 'VES'),
    ('VND', 'VND'),
    ('VUV', 'VUV'),
    ('WST', 'WST'),
    ('XAF', 'XAF'),
    ('XCD', 'XCD'),
    ('XOF', 'XOF'),
    ('XPF', 'XPF'),
    ('XSU', 'XSU'),
    ('XUA', 'XUA'),
    ('YER', 'YER'),
    ('ZMW', 'ZMW'),
    ('ZWL', 'ZWL'),
    )

PACKAGE_TYPE = (
    ('30 Days', '30 Days'),
    ('90 Days', '90 Days'),
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
    ('Select State', 'Select State'),
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
    ('None', 'None'),
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
    reciprocal_ivf = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
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
        'reciprocal_ivf',
        'hiv_patients_treatment',
        'sex_selection',
        'accepts_patients_from_abroad',
        ]


class PostForm(forms.ModelForm):
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

    clinicState = forms.CharField(widget=forms.Select(choices=CATEGORY_CHOICES_WORLD_STATES, attrs={'class': 'form-control',}), label=('Clinics state'))

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
    reciprocal_ivf = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
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
        'reciprocal_ivf',
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


class PostFormPro(forms.ModelForm):
    clinicName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Name'))
    clinicTitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}), label=('Clinics Title'))
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
    reciprocal_ivf = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}), required=False)
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
        'reciprocal_ivf',
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

class bestarticleproposition(forms.ModelForm):
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

class picclinicform(forms.ModelForm):
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
