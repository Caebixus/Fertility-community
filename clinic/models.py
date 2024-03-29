from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
from blog.models import BestClinicArticleCountry, BestClinicArticleState, BestClinicArticleCity, ModularBestClinics
from .calculate_dti import calculate_dti_single
from .validators import validate_file_size

from .choices import CATEGORY_CHOICES_CURRENCY
from coaches.models import Coaches

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

class BasicClinic(models.Model):
    ### Basic information
    clinicOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    clinicName = models.CharField(max_length=80)
    clinicTitle = models.CharField(max_length=100, blank=True, null=True)
    clinicGoogleReviewsUrl = models.URLField(max_length=600, null=True, blank=True)
    TYPE = (
        ('Clinic', 'Clinic'),
        ('Agency', 'Agency'),
        ('DonorBank', 'DonorBank'),
        )
    type = models.CharField(max_length=40, choices=TYPE, null=True, default='Clinic')
    description = models.TextField(max_length=1300, blank=True, null=True)
    treatmentLimitations = models.TextField(max_length=800, blank=True, null=True)

    ### Clinic's digital transparency index
    digitalTransparencyIndex = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    experts = models.ManyToManyField(Coaches, related_name='experts_from_clinic', blank=True)

    ### Contact information
    slug = models.SlugField(max_length=100, null=True)
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
    active_30 = models.BooleanField(default=False,null=True, blank=True)
    active_90 = models.BooleanField(default=False, null=True, blank=True)
    active_180 = models.BooleanField(default=False, null=True, blank=True)

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
    accepted_currency_type = models.ManyToManyField('AcceptedCurrency', blank=True)
    accepted_payment_type = models.ManyToManyField('AcceptedPayment', blank=True, related_name='payment_types_related_name')

    payment_type_cash = models.BooleanField(default=False)
    payment_type_major_credit_cards = models.BooleanField(default=False)
    payment_type_debit_cards = models.BooleanField(default=False)
    payment_type_check = models.BooleanField(default=False)
    payment_type_cryptocurrency = models.BooleanField(default=False)
    payment_type_wire_transfer = models.BooleanField(default=False)

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

    ### Primary treatments faqs
    initial_consultation_faqs = models.CharField(max_length=500, null=True, blank=True)
    follow_up_consultation_faqs = models.CharField(max_length=500, null=True, blank=True)
    ivf_treatment_faqs = models.CharField(max_length=500, null=True, blank=True)
    mild_ivf_treatment_faqs = models.CharField(max_length=500, null=True, blank=True)
    ovarian_ivf_treatment_faqs = models.CharField(max_length=500, null=True, blank=True)
    icsi_treatment_faqs = models.CharField(max_length=500, null=True, blank=True)
    egg_donor_recipients_faqs = models.CharField(max_length=500, null=True, blank=True)
    known_egg_donor_recipients_faqs = models.CharField(max_length=500, null=True, blank=True)
    shared_egg_donor_recipients_faqs = models.CharField(max_length=500, null=True, blank=True)
    sperm_donor_recipients_faqs = models.CharField(max_length=500, null=True, blank=True)
    known_sperm_donor_recipients_faqs = models.CharField(max_length=500, null=True, blank=True)
    embryo_donor_recipients_faqs = models.CharField(max_length=500, null=True, blank=True)
    known_embryo_donor_recipients_faqs = models.CharField(max_length=500, null=True, blank=True)


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

    ### Additional treatments faqs
    egg_freezing_faqs = models.CharField(max_length=500, null=True, blank=True)
    embryo_freezing_faqs = models.CharField(max_length=500, null=True, blank=True)
    sperm_freezing_faqs = models.CharField(max_length=500, null=True, blank=True)
    assisted_hatching_faqs = models.CharField(max_length=500, null=True, blank=True)
    vasectomy_reversal_faqs = models.CharField(max_length=500, null=True, blank=True)
    fertility_preservation_faqs = models.CharField(max_length=500, null=True, blank=True)
    surrogacy_faqs = models.CharField(max_length=500, null=True, blank=True)
    pgd_faqs = models.CharField(max_length=500, null=True, blank=True)
    pgta_pgs_faqs = models.CharField(max_length=500, null=True, blank=True)
    pgtst_pgs_faqs = models.CharField(max_length=500, null=True, blank=True)
    iui_treatment_faqs = models.CharField(max_length=500, null=True, blank=True)

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
    accepts_patients_from_abroad = models.BooleanField(default=False)

    ### -----------------------------------------------------------------------
    ### Clinic Booleands
    is_published = models.BooleanField(default=False)
    is_claimed = models.BooleanField(default=False)
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
    team1pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
    team1pic_del = models.BooleanField(default=False, blank=True, null=True)
    team1position = models.CharField(max_length=30, blank=True, null=True)

    team2name = models.CharField(max_length=25, blank=True, null=True)
    team2pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
    team2pic_del = models.BooleanField(default=False, blank=True, null=True)
    team2position = models.CharField(max_length=30, blank=True, null=True)

    team3name = models.CharField(max_length=25, blank=True, null=True)
    team3pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
    team3pic_del = models.BooleanField(default=False, blank=True, null=True)
    team3position = models.CharField(max_length=30, blank=True, null=True)

    ### Clinics PRO logo of the clinic
    clinic_pro_logo_pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
    clinic_pro_logo_pic_del = models.BooleanField(default=False, blank=True, null=True)

    ### Clinics PRO main picture on detail page
    clinic_pro_main_pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])

    ### Clinic PRO optional photos
    clinic_pro_photo_1 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
    clinic_pro_photo_1_del = models.BooleanField(default=False, blank=True, null=True)

    clinic_pro_photo_2 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
    clinic_pro_photo_2_del = models.BooleanField(default=False, blank=True, null=True)

    clinic_pro_photo_3 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
    clinic_pro_photo_3_del = models.BooleanField(default=False, blank=True, null=True)

    clinic_pro_photo_4 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
    clinic_pro_photo_4_del = models.BooleanField(default=False, blank=True, null=True)

    clinic_pro_photo_5 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
    clinic_pro_photo_5_del = models.BooleanField(default=False, blank=True, null=True)

    clinic_pro_photo_6 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True, validators=[validate_file_size])
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

    ### Article - Best Clinics in Country
    best_article_country_boolean = models.BooleanField(default=False, blank=True, null=True)
    best_article_country_actual_text = models.TextField(max_length=3750, blank=True, null = True)
    best_article_country_actual_prototype = models.TextField(max_length=3750, blank=True, null = True)
    best_article_country_fcreview_text = models.TextField(max_length=1000, blank=True, null = True)
    best_article_country_blogpost_obj = models.ForeignKey(BestClinicArticleCountry, on_delete=models.PROTECT, blank=True, null=True, related_name='best_article_country_fk')

    ### Article - Best Clinics in State
    best_article_state_boolean = models.BooleanField(default=False, blank=True, null=True)
    best_article_state_actual_text = models.TextField(max_length=3750, blank=True, null = True)
    best_article_state_actual_prototype = models.TextField(max_length=3750, blank=True, null = True)
    best_article_state_fcreview_text = models.TextField(max_length=1000, blank=True, null = True)
    best_article_state_blogpost_obj = models.ForeignKey(BestClinicArticleState, on_delete=models.PROTECT, blank=True, null=True, related_name='best_article_state_fk')

    ### Article - Best Clinics in City
    best_article_city_boolean = models.BooleanField(default=False, blank=True, null=True)
    best_article_city_actual_text = models.TextField(max_length=3750, blank=True, null = True)
    best_article_city_actual_prototype = models.TextField(max_length=3750, blank=True, null = True)
    best_article_city_fcreview_text = models.TextField(max_length=1000, blank=True, null = True)
    best_article_city_blogpost_obj = models.ForeignKey(BestClinicArticleCity, on_delete=models.PROTECT, blank=True, null=True, related_name='best_article_city_fk')
    best_article_city_google_reviews_section_content = models.TextField(max_length=3750, blank=True, null = True)
    best_article_city_pricing_section_content = models.TextField(max_length=3750, blank=True, null = True)
    best_article_city_distance_section_content = models.TextField(max_length=3750, blank=True, null = True)
    best_article_city_accommodation_section_content = models.TextField(max_length=3750, blank=True, null = True)
    best_article_city_packages_section_content = models.TextField(max_length=3750, blank=True, null = True)


    DEMO_CHOICES = (
        ("Value for money", "Value for money"),
        ("Renowned surgeons", "Renowned surgeons"),
        ("Professional staff", "Professional staff"),
        ("Honest expectations", "Honest expectations"),
        ("Brilliant attention from staff", "Brilliant attention from staff"),
        ("Excellent customer care", "Excellent customer care"),
        ("Friendly staff", "Friendly staff"),
        ("Stress-free treatment", "Stress-free treatment"),
        ("Outstanding aftercare", "Outstanding aftercare"),
        ("Personalized and Tailored Treatment", "Personalized and Tailored Treatment"),
        ("Renowned Team of Fertility Specialists", "Renowned Team of Fertility Specialists"),
        ("Technologically latest Services", "Technologically latest Services"),
    )

    # Country - Modular
    modular_country_active = models.BooleanField(default=False, blank=True, null=True)
    modular_country = models.ForeignKey(ModularBestClinics, on_delete=models.PROTECT, blank=True, null=True, related_name='best_modular_country', limit_choices_to={'state': None, 'city': None})
    modular_country_actual_text = models.TextField(max_length=3750, blank=True, null = True)
    modular_country_actual_prototype = models.TextField(max_length=3750, blank=True, null = True)
    modular_country_fcreview_text = models.TextField(max_length=1000, blank=True, null = True)
    choices_of_best_list_country = models.CharField(max_length=500, choices=DEMO_CHOICES, blank=True, null=True)

    # State - Modular
    modular_state_active = models.BooleanField(default=False, blank=True, null=True)
    modular_state = models.ForeignKey(ModularBestClinics, on_delete=models.PROTECT, blank=True, null=True, related_name='best_modular_state', limit_choices_to={'country': None, 'city': None})
    modular_state_actual_text = models.TextField(max_length=3750, blank=True, null = True)
    modular_state_actual_prototype = models.TextField(max_length=3750, blank=True, null = True)
    modular_state_fcreview_text = models.TextField(max_length=1000, blank=True, null = True)
    choices_of_best_list_state = models.CharField(max_length=500, choices=DEMO_CHOICES, blank=True, null=True)

    # City - Modular
    modular_city_active = models.BooleanField(default=False, blank=True, null=True)
    modular_city = models.ForeignKey(ModularBestClinics, on_delete=models.PROTECT, blank=True, null=True, related_name='best_modular_city', limit_choices_to={'state': None, 'country': None})
    modular_city_actual_text = models.TextField(max_length=3750, blank=True, null = True)
    modular_city_actual_prototype = models.TextField(max_length=3750, blank=True, null = True)
    modular_city_fcreview_text = models.TextField(max_length=1000, blank=True, null = True)
    choices_of_best_list_city = models.CharField(max_length=500, choices=DEMO_CHOICES, blank=True, null=True)


    class Meta:
        ordering = ["id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.clinicName)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('clinics:clinic-detail', kwargs={'pk': self.id, 'slug': self.slug})

    def __int__(self):
        return self.pk

    def user(self):
        return self.user


@receiver(pre_save, sender=BasicClinic)
def dti_calculate_on_save(sender, instance, *args, **kwargs):
    calculate_dti_single(instance=instance)


class AcceptedPayment(models.Model):
    accepted_payment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.accepted_payment)

class AcceptedCurrency(models.Model):
    accepted_currency = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.accepted_currency)

class ClinicsExportProxy(BasicClinic):
    class Meta:
        proxy = True

class PayProCustomerClinic(models.Model):
    proClinic = models.OneToOneField(BasicClinic, on_delete=models.CASCADE, blank=True, null = True, related_name='proClinic')

    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)

    membership = models.BooleanField(default=False)
