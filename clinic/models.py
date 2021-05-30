from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

LIVE_CHAT_CHOICES = (
    ('Chatra', 'Chatra'),
    ('Livechat', 'Livechat'),
    ('Olark', 'Olark'),
    ('Tidio', 'Tidio'),
    )

TRUSTPILOT_CHOICES = (
    ('Micro Review Count', 'Micro Review Count'),
    ('Mini', 'Mini'),
    )

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

class BasicClinic(models.Model):
    ### Basic information
    clinicOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    clinicName = models.CharField(max_length=80)
    clinicTitle = models.CharField(max_length=100, blank=True, null = True)
    clinicGoogleReviewsUrl = models.URLField(null=True, blank=True)
    TYPE = (
        ('Clinic', 'Clinic'),
        ('Agency', 'Agency'),
        ('DonorBank', 'DonorBank'),
        )
    type = models.CharField(max_length=40, choices=TYPE, null = True, default='Clinic')
    description = models.TextField(max_length=800, blank=True, null = True)
    treatmentLimitations = models.TextField(max_length=800, blank=True, null = True)

    ### Contact information
    clinic_url = models.URLField(null=True, blank=True, max_length=500)
    contact_url = models.URLField(max_length=500)
    contact_phone = models.CharField(max_length=20, blank=True)

    contact_email = models.CharField(max_length=50, blank=True)
    fertilitycommunity_email = models.CharField(max_length=50, blank=True)
    query_email = models.CharField(max_length=50, blank=True)

    ### Counters:
    packageClinicCounterNumber = models.IntegerField(default=0,null=True, blank=True)
    guestBlogCounterNumber = models.IntegerField(default=0,null=True, blank=True)
    guestAuthorCounterNumber = models.IntegerField(default=0,null=True, blank=True)

    ### Socials:
    clinicFacebook = models.URLField(null=True, blank=True, max_length=500)
    clinicInstagram = models.URLField(null=True, blank=True, max_length=500)
    clinicTwitter = models.URLField(null=True, blank=True, max_length=500)
    clinicYoutube = models.URLField(null=True, blank=True, max_length=500)
    clinicLinkedIn = models.URLField(null=True, blank=True, max_length=500)
    clinicPinterest = models.URLField(null=True, blank=True, max_length=500)

    ### Adresses
    clinicStreetAddress = models.CharField(max_length=200)
    clinicCity = models.CharField(max_length=100)
    clinicState = models.CharField(max_length=100)
    clinicRegion = models.CharField(max_length=100, null=True, blank=True)
    clinicPostalCode = models.CharField(max_length=100)

    ### Clinic Links (SEO)
    clinicCityLink = models.URLField(null=True, blank=True)
    clinicRegionLink = models.URLField(null=True, blank=True)
    clinicStateLink = models.URLField(null=True, blank=True)
    clinicLocationLink = models.URLField(null=True, blank=True, default='https://www.fertilitycommunity.com/ivf-cost')

    ### Open Hours of clinic
    mondayOpens = models.CharField(max_length=30, null=True, blank=True)
    mondayCloses = models.CharField(max_length=30, null=True, blank=True)
    tuesdayOpens = models.CharField(max_length=30, null=True, blank=True)
    tuesdayCloses = models.CharField(max_length=30, null=True, blank=True)
    wednesdayOpens = models.CharField(max_length=30, null=True, blank=True)
    wednesdayCloses = models.CharField(max_length=30, null=True, blank=True)
    thursdayOpens = models.CharField(max_length=30, null=True, blank=True)
    thursdayCloses = models.CharField(max_length=30, null=True, blank=True)
    fridayOpens = models.CharField(max_length=30, null=True, blank=True)
    fridayCloses = models.CharField(max_length=30, null=True, blank=True)
    saturdayOpens = models.CharField(max_length=30, null=True, blank=True)
    saturdayCloses = models.CharField(max_length=30, null=True, blank=True)
    sundayOpens = models.CharField(max_length=30, null=True, blank=True)
    sundayCloses = models.CharField(max_length=30, null=True, blank=True)

    ### clinics Badges
    clinicSart = models.CharField(max_length=100, null=True, blank=True)
    clinicHfea = models.CharField(max_length=100, null=True, blank=True)
    CATEGORY_CHOICES_OWN = (
        ('Unknown', 'Unknown'),
        ('Private', 'Private'),
        ('State', 'State'),
        )
    clinicOwn = models.CharField(max_length=40, choices=CATEGORY_CHOICES_OWN, null = True)

    ### Clinic Language
    clinicEnglish = models.BooleanField(default=False)
    clinicSpanish = models.BooleanField(default=False)
    clinicPortuguese = models.BooleanField(default=False)
    clinicRussian = models.BooleanField(default=False)
    clinicGerman = models.BooleanField(default=False)
    clinicChinese = models.BooleanField(default=False)

    ### Clinic Currency - primarily accepted currency by clinic
    defaultClinicCurrency = models.CharField(max_length=40, choices=CATEGORY_CHOICES_CURRENCY, null = True, default='USD')

    ### -----------------------------------------------------------------------
    ### Primary treatments + ### anonymous egg donation = egg_donor_recipients
    initial_consultation = models.BooleanField(default=False)
    follow_up_consultation = models.BooleanField(default=False)
    ivf_treatment = models.BooleanField(default=False)
    mild_ivf_treatment = models.BooleanField(default=False)
    ovarian_ivf_treatment = models.BooleanField(default=False)
    icsi_treatment = models.BooleanField(default=False)
    egg_donor_recipients = models.BooleanField(default=False)
    known_egg_donor_recipients = models.BooleanField(default=False)
    shared_egg_donor_recipients = models.BooleanField(default=False)
    sperm_donor_recipients = models.BooleanField(default=False)
    known_sperm_donor_recipients = models.BooleanField(default=False)
    embryo_donor_recipients = models.BooleanField(default=False)
    known_embryo_donor_recipients = models.BooleanField(default=False)

    ### Primary treatments costs
    initial_consultation_cost = models.FloatField(blank=True, null=True)
    follow_up_consultation_cost = models.FloatField(blank=True, null=True)
    ivf_treatment_cost = models.FloatField(blank=True, null=True)
    mild_ivf_treatment_cost = models.FloatField(blank=True, null=True)
    ovarian_ivf_treatment_cost = models.FloatField(blank=True, null=True)
    icsi_treatment_cost = models.FloatField(blank=True, null=True)
    egg_donor_recipients_cost = models.FloatField(blank=True, null=True)
    known_egg_donor_recipients_cost = models.FloatField(blank=True, null=True)
    shared_egg_donor_recipients_cost = models.FloatField(blank=True, null=True)
    sperm_donor_recipients_cost = models.FloatField(blank=True, null=True)
    known_sperm_donor_recipients_cost = models.FloatField(blank=True, null=True)
    embryo_donor_recipients_cost = models.FloatField(blank=True, null=True)
    known_embryo_donor_recipients_cost = models.FloatField(blank=True, null=True)

    ### -----------------------------------------------------------------------
    ### Additional treatments
    egg_freezing = models.BooleanField(default=False)
    embryo_freezing = models.BooleanField(default=False)
    sperm_freezing = models.BooleanField(default=False)
    assisted_hatching = models.BooleanField(default=False)
    vasectomy_reversal = models.BooleanField(default=False)
    fertility_preservation = models.BooleanField(default=False)
    surrogacy = models.BooleanField(default=False)
    pgd = models.BooleanField(default=False)
    pgta_pgs = models.BooleanField(default=False)
    pgtst_pgs = models.BooleanField(default=False)
    iui_treatment = models.BooleanField(default=False)

    ### Additional treatments costs
    egg_freezing_cost = models.FloatField(blank=True, null=True)
    embryo_freezing_cost = models.FloatField(blank=True, null=True)
    sperm_freezing_cost = models.FloatField(blank=True, null=True)
    assisted_hatching_cost = models.FloatField(blank=True, null=True)
    vasectomy_reversal_cost = models.FloatField(blank=True, null=True)
    fertility_preservation_cost = models.FloatField(blank=True, null=True)
    surrogacy_cost = models.FloatField(blank=True, null=True)
    pgd_cost = models.FloatField(blank=True, null=True)
    pgta_pgs_cost = models.FloatField(blank=True, null=True)
    pgtst_pgs_cost = models.FloatField(blank=True, null=True)
    iui_treatment_cost = models.FloatField(blank=True, null=True)

    ### -----------------------------------------------------------------------
    ### Donations
    egg_donor = models.BooleanField(default=False)
    sperm_donor = models.BooleanField(default=False)
    egg_sharing = models.BooleanField(default=False)

    egg_donor_url = models.URLField(null=True, blank=True, max_length=500)
    sperm_donor_url = models.URLField(null=True, blank=True, max_length=500)
    egg_sharing_url = models.URLField(null=True, blank=True, max_length=500)

    egg_donor_compensation = models.FloatField(blank=True, null=True)
    sperm_donor_compensation = models.FloatField(blank=True, null=True)
    egg_sharing_compensation = models.FloatField(blank=True, null=True)

    ### -----------------------------------------------------------------------
    ### Conditions
    single_woman_treatment = models.BooleanField(default=False)
    reciprocal_treatment = models.BooleanField(default=False)
    hiv_patients_treatment = models.BooleanField(default=False)
    sex_selection = models.BooleanField(default=False)

    ### -----------------------------------------------------------------------
    ### Clinic Booleands
    is_published = models.BooleanField(default=False)
    is_claimed = models.BooleanField(default=False)
    accepts_patients_from_abroad = models.BooleanField(default=False)
    pro_is_published = models.BooleanField(default=False)
    ppq_is_published  = models.BooleanField(default=False)
    no_waiting_list = models.BooleanField(default=False)
    verified_is_published = models.BooleanField(default=False)
    popular_is_published = models.BooleanField(default=False)
    promotion_is_published = models.BooleanField(default=False)
    is_not_approved = models.BooleanField(default=False)

    is_published_list_date = models.DateTimeField(default=datetime.now, blank=True)
    update_list_date = models.DateTimeField(default=datetime.now, blank=True)
    pro_update_is_published_list_date = models.DateTimeField(default=datetime.now, blank=True)
    pro_list_date = models.DateTimeField(default=datetime.now, blank=True)
    ppq_update_is_published_list_date = models.DateTimeField(default=datetime.now, blank=True)
    ppq_list_date = models.DateTimeField(default=datetime.now, blank=True)

    ### ------------------------------------------------ ###
    ### BUILD FOR PRO + CLAIM FEATURES ###
    ### ------------------------------------------------ ###

    ### Consultants
    team1name = models.CharField(max_length=25, blank=True, null=True)
    team1pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    team1pic_del = models.BooleanField(default=False, blank=True, null=True)

    team2name = models.CharField(max_length=25, blank=True, null=True)
    team2pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    team2pic_del = models.BooleanField(default=False, blank=True, null=True)

    team3name = models.CharField(max_length=25, blank=True, null=True)
    team3pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    team3pic_del = models.BooleanField(default=False, blank=True, null=True)

    ### Clinics PRO logo of the clinic
    clinic_pro_logo_pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_logo_pic_del = models.BooleanField(default=False, blank=True, null=True)

    ### Clinics PRO main picture on detail page
    clinic_pro_main_pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)

    ### Clinic PRO optional photos
    clinic_pro_photo_1 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_1_del = models.BooleanField(default=False, blank=True, null=True)

    clinic_pro_photo_2 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_2_del = models.BooleanField(default=False, blank=True, null=True)

    clinic_pro_photo_3 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_3_del = models.BooleanField(default=False, blank=True, null=True)

    clinic_pro_photo_4 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_4_del = models.BooleanField(default=False, blank=True, null=True)

    clinic_pro_photo_5 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_5_del = models.BooleanField(default=False, blank=True, null=True)

    clinic_pro_photo_6 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_6_del = models.BooleanField(default=False, blank=True, null=True)

    ### Clinic Live Chat Code snippets (Pokud přidáváš nový chat tak uprav i badge na search lokacích)
    clinicLiveChatChoice = models.CharField(max_length=40, choices=LIVE_CHAT_CHOICES, null = True, blank=True,)
    clinicChatraCode = models.CharField(max_length=100, blank=True, null = True)
    clinicLiveChatCode = models.CharField(max_length=100, blank=True, null = True)
    clinicOlarkCode = models.CharField(max_length=100, blank=True, null = True)
    clinicTidioCode = models.CharField(max_length=100, blank=True, null = True)

    ### Clinic reviews snippets
    clinicGoogleReviews = models.URLField(null=True, blank=True, max_length=2000)

    clinicTrustPilotChoice = models.CharField(max_length=40, choices=TRUSTPILOT_CHOICES, null = True, blank=True,)
    clinicTrustPilotID = models.CharField(max_length=100, blank=True, null = True)
    clinicTrustPilotDomain = models.CharField(max_length=100, blank=True, null = True)



#
###
####
#####
######
#######
######## DEPRECIATED MODELS FIELDS ------------------- ------------------- ------------------- ------------------- -------------------
    CATEGORY_PACKAGE = (
        ('IVF', 'IVF'),
        ('Egg Donation', 'Egg Donation'),
        ('Embryo Donation', 'Embryo Donation'),
        )

    package1title = models.CharField(max_length=30, blank=True, null = True)
    package1category = models.CharField(max_length=40, choices=CATEGORY_PACKAGE, null = True, default=CATEGORY_PACKAGE[0][0])
    package1desc = models.TextField(max_length=500, blank=True, null = True)
    package1cost = models.FloatField(blank=True, null=True)

    package2title = models.CharField(max_length=30, blank=True, null = True)
    package2category = models.CharField(max_length=40, choices=CATEGORY_PACKAGE, null = True, default=CATEGORY_PACKAGE[0][0])
    package2desc = models.TextField(max_length=500, blank=True, null = True)
    package2cost = models.FloatField(blank=True, null=True)

    package3title = models.CharField(max_length=30, blank=True, null = True)
    package3category = models.CharField(max_length=40, choices=CATEGORY_PACKAGE, null = True, default=CATEGORY_PACKAGE[0][0])
    package3desc = models.TextField(max_length=500, blank=True, null = True)
    package3cost = models.FloatField(blank=True, null=True)

    package4title = models.CharField(max_length=30, blank=True, null = True)
    package4category = models.CharField(max_length=40, choices=CATEGORY_PACKAGE, null = True, default=CATEGORY_PACKAGE[0][0])
    package4desc = models.TextField(max_length=500, blank=True, null = True)
    package4cost = models.FloatField(blank=True, null=True)

    package5title = models.CharField(max_length=30, blank=True, null = True)
    package5category = models.CharField(max_length=40, choices=CATEGORY_PACKAGE, null = True, default=CATEGORY_PACKAGE[0][0])
    package5desc = models.TextField(max_length=500, blank=True, null = True)
    package5cost = models.FloatField(blank=True, null=True)

    package6title = models.CharField(max_length=30, blank=True, null = True)
    package6category = models.CharField(max_length=40, choices=CATEGORY_PACKAGE, null = True, default=CATEGORY_PACKAGE[0][0])
    package6desc = models.TextField(max_length=500, blank=True, null = True)
    package6cost = models.FloatField(blank=True, null=True)

    clinic_pro_promotion_name = models.CharField(max_length=80, blank=True, null=True)
    clinic_pro_promotion_description = models.TextField(max_length=800, blank=True, null=True)
    clinic_pro_promotion_landing_url = models.URLField(null=True, blank=True, max_length=500)
    clinic_staff = RichTextField(blank=True, null=True, max_length=300)

    def __str__(self):
        return str(self.clinicName)

class ClinicsExportProxy(BasicClinic):
    class Meta:
        proxy = True

class PayProCustomerClinic(models.Model):
    proClinic = models.OneToOneField(BasicClinic, on_delete=models.CASCADE, blank=True, null = True, related_name='proClinic')

    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)

    membership = models.BooleanField(default=False)
