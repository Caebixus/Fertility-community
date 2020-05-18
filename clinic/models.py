from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class BasicClinic(models.Model):
    ### Basic information
    clinicOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    clinicName = models.CharField(max_length=80)
    clinicTitle = models.CharField(max_length=100, blank=True, null = True)
    clinicGoogleReviewsUrl = models.URLField(null=True, blank=True)
    TYPE = (
        ('Clinic', 'Clinic'),
        ('Agency', 'Agency'),
        )
    type = models.CharField(max_length=40, choices=TYPE, null = True, default='Clinic')

    ### Users option to promote their clinic & treatments
    description = models.TextField(max_length=800, blank=True, null = True)
    treatmentLimitations = models.TextField(max_length=800, blank=True, null = True)

    ### Clinics Doctors & Staff
    clinic_staff = RichTextField(blank=True, null=True, max_length=300)

    ### URL address for contact button to redirections
    clinic_url = models.URLField(null=True, blank=True)
    contact_url = models.URLField()
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_email = models.CharField(max_length=50, blank=True)
    query_email = models.CharField(max_length=50, blank=True)

    ### Adresses
    clinicStreetAddress = models.CharField(max_length=200)
    clinicCity = models.CharField(max_length=100)
    clinicState = models.CharField(max_length=100)
    clinicRegion = models.CharField(max_length=100, null=True, blank=True)
    clinicPostalCode = models.CharField(max_length=100)

    ### Clinic Links
    clinicCityLink = models.URLField(null=True, blank=True)
    clinicRegionLink = models.URLField(null=True, blank=True)
    clinicStateLink = models.URLField(null=True, blank=True, default='https://www.fertilitycommunity.com/locations/us-regions')
    clinicLocationLink = models.URLField(null=True, blank=True, default='https://www.fertilitycommunity.com/locations')

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
    CATEGORY_CHOICES_CURRENCY = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        )
    defaultClinicCurrency = models.CharField(max_length=40, choices=CATEGORY_CHOICES_CURRENCY, null = True)

    ivf_treatment = models.BooleanField(default=False)
    mild_ivf_treatment = models.BooleanField(default=False)
    ovarian_ivf_treatment = models.BooleanField(default=False)
    icsi_treatment = models.BooleanField(default=False)
    egg_donor_recipients = models.BooleanField(default=False)
    sperm_donor_recipients = models.BooleanField(default=False)
    embryo_donor_recipients = models.BooleanField(default=False)

    ### Basic fertility treatments costs
    ivf_treatment_cost = models.FloatField(blank=True, null=True)
    mild_ivf_treatment_cost = models.FloatField(blank=True, null=True)
    ovarian_ivf_treatment_cost = models.FloatField(blank=True, null=True)
    icsi_treatment_cost = models.FloatField(blank=True, null=True)
    egg_donor_recipients_cost = models.FloatField(blank=True, null=True)
    sperm_donor_recipients_cost = models.FloatField(blank=True, null=True)
    embryo_donor_recipients_cost = models.FloatField(blank=True, null=True)

    ### Additional treatments
    egg_freezing = models.BooleanField(default=False)
    embryo_freezing = models.BooleanField(default=False)
    sperm_freezing = models.BooleanField(default=False)
    assisted_hatching = models.BooleanField(default=False)
    vasectomy_reversal = models.BooleanField(default=False)
    fertility_preservation = models.BooleanField(default=False)
    surrogacy = models.BooleanField(default=False)
    pgd = models.BooleanField(default=False)
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
    iui_treatment_cost = models.FloatField(blank=True, null=True)

    ### Conditions
    single_woman_treatment = models.BooleanField(default=False)
    reciprocal_treatment = models.BooleanField(default=False)
    hiv_patients_treatment = models.BooleanField(default=False)
    sex_selection = models.BooleanField(default=False)

    ### Clinic Booleands
    is_published = models.BooleanField(default=False)
    is_claimed = models.BooleanField(default=False)
    pro_is_published = models.BooleanField(default=False)
    ppq_is_published  = models.BooleanField(default=False)
    no_waiting_list = models.BooleanField(default=False)
    verified_is_published = models.BooleanField(default=False)
    popular_is_published = models.BooleanField(default=False)
    promotion_is_published = models.BooleanField(default=False)

    is_published_list_date = models.DateTimeField(default=datetime.now, blank=True)
    update_list_date = models.DateTimeField(default=datetime.now, blank=True)
    pro_update_is_published_list_date = models.DateTimeField(default=datetime.now, blank=True)
    pro_list_date = models.DateTimeField(default=datetime.now, blank=True)
    ppq_update_is_published_list_date = models.DateTimeField(default=datetime.now, blank=True)
    ppq_list_date = models.DateTimeField(default=datetime.now, blank=True)

    ### ------------------------------------------------ ###
    ### BUILD FOR PRO FEATURES ###
    ### ------------------------------------------------ ###

    ### Packages
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

    ### Consultants
    team1name = models.CharField(max_length=25, blank=True, null=True)
    team1pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    team2name = models.CharField(max_length=25, blank=True, null=True)
    team2pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    team3name = models.CharField(max_length=25, blank=True, null=True)
    team3pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)

    ### Promotions
    clinic_pro_promotion_name = models.CharField(max_length=80, blank=True, null=True)
    clinic_pro_promotion_description = models.TextField(max_length=800, blank=True, null=True)
    clinic_pro_promotion_landing_url = models.URLField(null=True, blank=True)

    ### Clinics PRO logo of the clinic
    clinic_pro_logo_pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)

    ### Clinics PRO main picture on detail page
    clinic_pro_main_pic = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)

    ### Clinic PRO optional photos
    clinic_pro_photo_1 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_2 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_3 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_4 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_5 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)
    clinic_pro_photo_6 = models.ImageField(upload_to='ownerPhotos', blank=True, null=True)

    def __str__(self):
        return self.clinicName + str(self.pro_is_published)
