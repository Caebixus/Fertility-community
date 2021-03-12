from django.contrib import admin
from .models import BasicClinic, ClinicsExportProxy
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('id', 'clinicName', 'clinicOwner', 'clinicRegionLink', 'update_list_date', 'is_published', 'is_claimed', 'pro_is_published', 'ppq_is_published', 'is_published_list_date', 'pro_update_is_published_list_date', 'clinicRegion', 'clinicState')
    list_filter = ('is_published', 'pro_is_published', 'verified_is_published', 'clinicOwner', 'clinicRegion', 'clinicState', 'clinicCity')
    search_fields = ('clinicName', 'clinicOwner__username', 'clinicRegion', 'clinicState', 'clinicCity')
    fieldsets = (
        ('Basic information', {'fields': ('clinicOwner', 'clinicName', 'clinicTitle',)}),
        ('Links', {'fields': ('clinicCityLink', 'clinicRegionLink', 'clinicStateLink', 'clinicLocationLink',)}),
        ('Contact information', {'fields': ('clinic_url', 'contact_url', 'contact_phone', 'contact_email', 'query_email', 'fertilitycommunity_email', 'packageClinicCounterNumber', 'guestBlogCounterNumber', 'guestAuthorCounterNumber')}),
        ('Address information', {'fields': ('clinicStreetAddress', 'clinicCity', 'clinicState', 'clinicRegion', 'clinicPostalCode',)}),
        ('Opening hours', {'fields': ('mondayOpens', 'mondayCloses', 'tuesdayOpens', 'tuesdayCloses', 'wednesdayOpens', 'wednesdayCloses', 'thursdayOpens', 'thursdayCloses', 'fridayOpens', 'fridayCloses', 'saturdayOpens', 'saturdayCloses', 'sundayOpens', 'sundayCloses',)}),
        ('Secondary information', {'fields': ('clinicSart', 'clinicHfea', 'clinicOwn', 'clinicEnglish', 'clinicSpanish', 'clinicPortuguese', 'clinicRussian', 'clinicGerman', 'clinicChinese', 'defaultClinicCurrency',)}),
        ('Primary treatments and costs', {'fields': ('initial_consultation', 'follow_up_consultation', 'ivf_treatment', 'mild_ivf_treatment', 'ovarian_ivf_treatment', 'icsi_treatment', 'egg_donor_recipients', 'known_egg_donor_recipients', 'shared_egg_donor_recipients', 'sperm_donor_recipients', 'known_sperm_donor_recipients', 'embryo_donor_recipients', 'known_embryo_donor_recipients', 'initial_consultation_cost', 'follow_up_consultation_cost', 'ivf_treatment_cost', 'mild_ivf_treatment_cost', 'ovarian_ivf_treatment_cost', 'icsi_treatment_cost', 'egg_donor_recipients_cost', 'known_egg_donor_recipients_cost', 'shared_egg_donor_recipients_cost', 'sperm_donor_recipients_cost', 'known_sperm_donor_recipients_cost', 'embryo_donor_recipients_cost', 'known_embryo_donor_recipients_cost')}),
        ('Seconday treatments and costs', {'fields': ('egg_freezing', 'embryo_freezing', 'sperm_freezing', 'assisted_hatching', 'vasectomy_reversal', 'fertility_preservation', 'surrogacy', 'pgd', 'pgta_pgs', 'pgtst_pgs', 'iui_treatment', 'egg_freezing_cost', 'embryo_freezing_cost', 'sperm_freezing_cost', 'assisted_hatching_cost', 'vasectomy_reversal_cost', 'fertility_preservation_cost', 'surrogacy_cost', 'pgd_cost', 'pgta_pgs_cost', 'pgtst_pgs_cost', 'iui_treatment_cost',)}),
        ('Donor options', {'fields': ('egg_donor', 'egg_donor_url', 'egg_donor_compensation', 'sperm_donor', 'sperm_donor_url', 'sperm_donor_compensation', 'egg_sharing', 'egg_sharing_url', 'egg_sharing_compensation',)}),
        ('Conditions', {'fields': ('single_woman_treatment', 'reciprocal_treatment', 'hiv_patients_treatment', 'sex_selection',)}),
        ('Clinic settings', {'fields': ('is_published', 'is_claimed', 'pro_is_published', 'ppq_is_published', 'is_not_approved', 'no_waiting_list', 'verified_is_published', 'popular_is_published', 'promotion_is_published', 'is_published_list_date', 'update_list_date', 'pro_update_is_published_list_date', 'pro_list_date', 'ppq_update_is_published_list_date', 'ppq_list_date',)}),
        ('Packages', {'fields': ('package1title', 'package1category', 'package1desc', 'package1cost', 'package2title', 'package2category', 'package2desc', 'package2cost', 'package3title', 'package3category', 'package3desc', 'package3cost', 'package4title', 'package4category', 'package4desc', 'package4cost', 'package5title', 'package5category', 'package5desc', 'package5cost', 'package6title', 'package6category', 'package6desc', 'package6cost',)}),
        ('Team', {'fields': ('team1name', 'team1pic', 'team2name', 'team2pic', 'team3name', 'team3pic',)}),
        ('Promotion', {'fields': ('clinic_pro_promotion_name', 'clinic_pro_promotion_description', 'clinic_pro_promotion_landing_url',)}),
        ('Images', {'fields': ('clinic_pro_logo_pic', 'clinic_pro_main_pic', 'clinic_pro_photo_1', 'clinic_pro_photo_2', 'clinic_pro_photo_3', 'clinic_pro_photo_4', 'clinic_pro_photo_5', 'clinic_pro_photo_6',)}),
        ('The rest', {'fields': ('clinicGoogleReviewsUrl', 'description', 'treatmentLimitations', 'clinic_staff', 'type',)}),
    )
    actions = ['clinicLocationLink_update_g']

    def clinicLocationLink_update_g(modeladmin, request, queryset):
        queryset.update(clinicStateLink='https://www.fertilitycommunity.com/fertility-clinics/usa')
    clinicLocationLink_update_g.short_description = "Update from Admin"

class ExportClinicTreatments(resources.ModelResource):
    class Meta:
        model = ClinicsExportProxy

class ExportClinic(ImportExportModelAdmin):
    resource_class = ExportClinicTreatments

admin.site.register(BasicClinic, PostAdmin)

admin.site.register(ClinicsExportProxy, ExportClinic)
