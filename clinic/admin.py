from django.contrib import admin
from .models import BasicClinic, ClinicsExportProxy, AcceptedPayment, AcceptedCurrency
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('clinicName',), }
    save_as = True
    list_display = ('id', 'digitalTransparencyIndex', 'clinicName', 'clinicOwner', 'is_published', 'is_claimed', 'pro_is_published', 'ppq_is_published', 'clinicCity', 'clinicRegion', 'clinicState', 'packageClinicCounterNumber', 'guestBlogCounterNumber', 'guestAuthorCounterNumber', 'best_article_country_boolean')
    list_filter = ('is_published', 'pro_is_published', 'verified_is_published', 'clinicOwner', 'clinicRegion', 'clinicState', 'clinicCity')
    search_fields = ('clinicName', 'clinicOwner__username', 'clinicRegion', 'clinicState', 'clinicCity')
    fieldsets = (
        ('Basic information', {'fields': ('clinicOwner', 'clinicName', 'clinicTitle', 'clinicGoogleReviewsUrl', 'digitalTransparencyIndex',)}),
        ('Links', {'fields': ('clinicCityLink', 'clinicRegionLink', 'clinicStateLink', 'clinicLocationLink',)}),
        ('Slugs', {'fields': ('slug',)}),
        ('Contact information', {'fields': ('clinic_url', 'contact_url', 'contact_phone', 'contact_email', 'query_email', 'fertilitycommunity_email', 'packageClinicCounterNumber', 'guestBlogCounterNumber', 'guestAuthorCounterNumber')}),
        ('Address information', {'fields': ('clinicStreetAddress', 'clinicCity', 'clinicState', 'clinicRegion', 'clinicPostalCode',)}),
        ('Opening hours', {'fields': ('mondayOpens', 'mondayCloses', 'tuesdayOpens', 'tuesdayCloses', 'wednesdayOpens', 'wednesdayCloses', 'thursdayOpens', 'thursdayCloses', 'fridayOpens', 'fridayCloses', 'saturdayOpens', 'saturdayCloses', 'sundayOpens', 'sundayCloses',)}),
        ('Secondary information', {'fields': ('clinicSart', 'clinicHfea', 'clinicOwn', 'clinicEnglish', 'clinicSpanish', 'clinicPortuguese', 'clinicRussian', 'clinicGerman', 'clinicChinese',)}),
        ('Payment information', {'fields': ('defaultClinicCurrency', 'payment_type_cash', 'payment_type_major_credit_cards', 'payment_type_debit_cards', 'payment_type_check', 'payment_type_cryptocurrency', 'payment_type_wire_transfer',)}),
        ('Primary treatments and costs', {'fields': ('initial_consultation', 'follow_up_consultation', 'ivf_treatment', 'mild_ivf_treatment', 'ovarian_ivf_treatment', 'icsi_treatment', 'egg_donor_recipients', 'known_egg_donor_recipients', 'shared_egg_donor_recipients', 'sperm_donor_recipients', 'known_sperm_donor_recipients', 'embryo_donor_recipients', 'known_embryo_donor_recipients', 'initial_consultation_cost', 'follow_up_consultation_cost', 'ivf_treatment_cost', 'mild_ivf_treatment_cost', 'ovarian_ivf_treatment_cost', 'icsi_treatment_cost', 'egg_donor_recipients_cost', 'known_egg_donor_recipients_cost', 'shared_egg_donor_recipients_cost', 'sperm_donor_recipients_cost', 'known_sperm_donor_recipients_cost', 'embryo_donor_recipients_cost', 'known_embryo_donor_recipients_cost', 'initial_consultation_faqs', 'follow_up_consultation_faqs', 'ivf_treatment_faqs', 'mild_ivf_treatment_faqs', 'ovarian_ivf_treatment_faqs', 'icsi_treatment_faqs', 'egg_donor_recipients_faqs', 'known_egg_donor_recipients_faqs', 'shared_egg_donor_recipients_faqs', 'sperm_donor_recipients_faqs', 'known_sperm_donor_recipients_faqs', 'embryo_donor_recipients_faqs', 'known_embryo_donor_recipients_faqs')}),
        ('Seconday treatments and costs', {'fields': ('egg_freezing', 'embryo_freezing', 'sperm_freezing', 'assisted_hatching', 'vasectomy_reversal', 'fertility_preservation', 'surrogacy', 'pgd', 'pgta_pgs', 'pgtst_pgs', 'iui_treatment', 'egg_freezing_cost', 'embryo_freezing_cost', 'sperm_freezing_cost', 'assisted_hatching_cost', 'vasectomy_reversal_cost', 'fertility_preservation_cost', 'surrogacy_cost', 'pgd_cost', 'pgta_pgs_cost', 'pgtst_pgs_cost', 'iui_treatment_cost', 'egg_freezing_faqs', 'embryo_freezing_faqs', 'sperm_freezing_faqs', 'assisted_hatching_faqs', 'vasectomy_reversal_faqs', 'fertility_preservation_faqs', 'surrogacy_faqs', 'pgd_faqs', 'pgta_pgs_faqs', 'pgtst_pgs_faqs', 'iui_treatment_faqs')}),
        ('Donor options', {'fields': ('egg_donor', 'egg_donor_url', 'egg_donor_compensation', 'sperm_donor', 'sperm_donor_url', 'sperm_donor_compensation', 'egg_sharing', 'egg_sharing_url', 'egg_sharing_compensation',)}),
        ('Conditions', {'fields': ('single_woman_treatment', 'reciprocal_treatment', 'hiv_patients_treatment', 'sex_selection',)}),
        ('Clinic settings', {'fields': ('is_published', 'is_claimed', 'accepts_patients_from_abroad', 'pro_is_published', 'ppq_is_published', 'is_not_approved', 'no_waiting_list', 'verified_is_published', 'popular_is_published', 'promotion_is_published', 'is_published_list_date', 'update_list_date', 'pro_update_is_published_list_date', 'pro_list_date', 'ppq_update_is_published_list_date', 'ppq_list_date',)}),
        ('Best Articles Country', {'fields': ('best_article_country_boolean', 'best_article_country_actual_text', 'best_article_country_actual_prototype', 'best_article_country_fcreview_text', 'best_article_country_blogpost_obj', )}),
        ('Best Articles State', {'fields': ('best_article_state_boolean', 'best_article_state_actual_text', 'best_article_state_actual_prototype', 'best_article_state_fcreview_text', 'best_article_state_blogpost_obj', )}),
        ('Best Articles City', {'fields': ('best_article_city_boolean', 'best_article_city_actual_text', 'best_article_city_actual_prototype', 'best_article_city_fcreview_text', 'best_article_city_blogpost_obj', )}),
        ('Team', {'fields': ('team1name', 'team1pic', 'team1position', 'team2name', 'team2pic', 'team2position', 'team3name', 'team3pic', 'team3position',)}),
        ('Socials', {'fields': ('clinicFacebook', 'clinicInstagram', 'clinicYoutube', 'clinicTwitter', 'clinicLinkedIn', 'clinicPinterest',)}),
        ('Images', {'fields': ('clinic_pro_logo_pic', 'clinic_pro_main_pic', 'clinic_pro_photo_1', 'clinic_pro_photo_2', 'clinic_pro_photo_3', 'clinic_pro_photo_4', 'clinic_pro_photo_5', 'clinic_pro_photo_6',)}),
        ('LiveChat tools', {'fields': ('clinicLiveChatChoice', 'clinicChatraCode', 'clinicLiveChatCode', 'clinicOlarkCode', 'clinicTidioCode',)}),
        ('Independent reviews', {'fields': ('clinicGoogleReviews', 'clinicTrustPilotChoice', 'clinicTrustPilotID', 'clinicTrustPilotDomain',)}),
        ('The rest', {'fields': ('description', 'treatmentLimitations', 'type',)}),
    )
    actions = ['clinicLocationLink_update_g']

    def clinicLocationLink_update_g(modeladmin, request, queryset):
        queryset.update(defaultClinicCurrency='USD')
    clinicLocationLink_update_g.short_description = "Update from Admin"

class ExportClinicTreatments(resources.ModelResource):
    class Meta:
        model = ClinicsExportProxy

class ExportClinic(ImportExportModelAdmin):
    resource_class = ExportClinicTreatments

#class AcceptedPaymentAdmin(admin.ModelAdmin):
    #model = AcceptedPayment
    #list_display = ('accepted_payment',)

#class AcceptedCurrencyAdmin(admin.ModelAdmin):
    #model = AcceptedCurrency
    #list_display = ('accepted_currency',)



admin.site.register(BasicClinic, PostAdmin)

admin.site.register(ClinicsExportProxy, ExportClinic)

#admin.site.register(AcceptedPayment, AcceptedPaymentAdmin)

#admin.site.register(AcceptedCurrency, AcceptedCurrencyAdmin)
