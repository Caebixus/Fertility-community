import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
django.setup()

from clinic.models import BasicClinic

basic = BasicClinic.objects.filter(is_published=True, pro_is_published = False, ppq_is_published=False)
for bas in basic:
    pointsBasic = 0
    ### Pricing = 10
    if bas.is_claimed == True:
        pointsBasic = pointsBasic + 5

    ### Pricing = 15
    if bas.ivf_treatment is not None:
        pointsBasic = pointsBasic + 1
    if bas.ivf_treatment_cost:
        pointsBasic = pointsBasic + 1
    if bas.ivf_treatment_faqs:
        pointsBasic = pointsBasic + 1

    if bas.mild_ivf_treatment is not None:
        pointsBasic = pointsBasic + 1
    if bas.mild_ivf_treatment_cost:
        pointsBasic = pointsBasic + 1
    if bas.mild_ivf_treatment_faqs:
        pointsBasic = pointsBasic + 1

    if bas.ovarian_ivf_treatment is not None:
        pointsBasic = pointsBasic + 1
    if bas.ovarian_ivf_treatment_cost:
        pointsBasic = pointsBasic + 1
    if bas.ovarian_ivf_treatment_faqs:
        pointsBasic = pointsBasic + 1

    if bas.iui_treatment is not None:
        pointsBasic = pointsBasic + 1
    if bas.iui_treatment_cost:
        pointsBasic = pointsBasic + 1
    if bas.iui_treatment_faqs:
        pointsBasic = pointsBasic + 1

    if bas.icsi_treatment is not None:
        pointsBasic = pointsBasic + 1
    if bas.icsi_treatment_cost:
        pointsBasic = pointsBasic + 1
    if bas.icsi_treatment_faqs:
        pointsBasic = pointsBasic + 1

    ### Pricing = 18
    if bas.egg_donor_recipients is not None:
        pointsBasic = pointsBasic + 1
    if bas.egg_donor_recipients_cost:
        pointsBasic = pointsBasic + 1
    if bas.egg_donor_recipients_faqs:
        pointsBasic = pointsBasic + 1

    if bas.known_egg_donor_recipients is not None:
        pointsBasic = pointsBasic + 1
    if bas.known_egg_donor_recipients_cost:
        pointsBasic = pointsBasic + 1
    if bas.known_egg_donor_recipients_faqs:
        pointsBasic = pointsBasic + 1

    if bas.embryo_donor_recipients is not None:
        pointsBasic = pointsBasic + 1
    if bas.embryo_donor_recipients_cost:
        pointsBasic = pointsBasic + 1
    if bas.embryo_donor_recipients_faqs:
        pointsBasic = pointsBasic + 1

    if bas.known_embryo_donor_recipients is not None:
        pointsBasic = pointsBasic + 1
    if bas.known_embryo_donor_recipients_cost:
        pointsBasic = pointsBasic + 1
    if bas.known_embryo_donor_recipients_faqs:
        pointsBasic = pointsBasic + 1

    if bas.sperm_donor_recipients is not None:
        pointsBasic = pointsBasic + 1
    if bas.sperm_donor_recipients_cost:
        pointsBasic = pointsBasic + 1
    if bas.sperm_donor_recipients_faqs:
        pointsBasic = pointsBasic + 1

    if bas.known_sperm_donor_recipients is not None:
        pointsBasic = pointsBasic + 1
    if bas.known_sperm_donor_recipients_cost:
        pointsBasic = pointsBasic + 1
    if bas.known_sperm_donor_recipients_faqs:
        pointsBasic = pointsBasic + 1

    ### Pricing = 12
    if bas.egg_freezing:
        pointsBasic = pointsBasic + 1
    if bas.egg_freezing_cost:
        pointsBasic = pointsBasic + 1
    if bas.egg_freezing_faqs:
        pointsBasic = pointsBasic + 1

    if bas.embryo_freezing:
        pointsBasic = pointsBasic + 1
    if bas.embryo_freezing_cost:
        pointsBasic = pointsBasic + 1
    if bas.embryo_freezing_faqs:
        pointsBasic = pointsBasic + 1

    if bas.sperm_freezing:
        pointsBasic = pointsBasic + 1
    if bas.sperm_freezing_cost:
        pointsBasic = pointsBasic + 1
    if bas.sperm_freezing_faqs:
        pointsBasic = pointsBasic + 1

    if bas.surrogacy:
        pointsBasic = pointsBasic + 1
    if bas.surrogacy_cost:
        pointsBasic = pointsBasic + 1
    if bas.surrogacy_faqs:
        pointsBasic = pointsBasic + 1

    ### Clinic's Conditions = 2
    if bas.single_woman_treatment == True or bas.reciprocal_treatment == True or bas.hiv_patients_treatment == True or bas.sex_selection == True:
        pointsBasic = pointsBasic + 1
    if bas.accepts_patients_from_abroad == True:
        pointsBasic = pointsBasic + 1

    ### Clinic's Languages NEW = 2
    if bas.clinicEnglish is not None:
        pointsBasic = pointsBasic + 1
    if bas.clinicSpanish is not None or bas.clinicPortuguese is not None or bas.clinicRussian is not None or bas.clinicGerman is not None or bas.clinicChinese is not None:
        pointsBasic = pointsBasic + 1

    ### Clinic's Basic Information = 1
    if bas.clinicTitle:
        pointsBasic = pointsBasic + 1
    if bas.description:
        pointsBasic = pointsBasic + 1
    if bas.treatmentLimitations:
        pointsBasic = pointsBasic + 1

    ### Clinic's Images = 9
    if bas.clinic_pro_logo_pic:
        pointsBasic = pointsBasic + 3
    if bas.clinic_pro_photo_1:
        pointsBasic = pointsBasic + 1
    if bas.clinic_pro_photo_2:
        pointsBasic = pointsBasic + 1
    if bas.clinic_pro_photo_3:
        pointsBasic = pointsBasic + 1
    if bas.clinic_pro_photo_4:
        pointsBasic = pointsBasic + 1
    if bas.clinic_pro_photo_5:
        pointsBasic = pointsBasic + 1
    if bas.clinic_pro_photo_6:
        pointsBasic = pointsBasic + 1

    ### Clinic's Contact Information = 5
    if bas.contact_url:
        pointsBasic = pointsBasic + 1
    if bas.contact_phone:
        pointsBasic = pointsBasic + 1
    if bas.contact_email:
        pointsBasic = pointsBasic + 1
    if bas.query_email:
        pointsBasic = pointsBasic + 1
    if bas.fertilitycommunity_email:
        pointsBasic = pointsBasic + 1

    ### Clinic's Social Media = 6
    if bas.clinicFacebook:
        pointsBasic = pointsBasic + 1
    if bas.clinicInstagram:
        pointsBasic = pointsBasic + 1
    if bas.clinicTwitter:
        pointsBasic = pointsBasic + 1
    if bas.clinicYoutube:
        pointsBasic = pointsBasic + 1
    if bas.clinicLinkedIn:
        pointsBasic = pointsBasic + 1
    if bas.clinicPinterest:
        pointsBasic = pointsBasic + 1

    bas.digitalTransparencyIndex = pointsBasic
    bas.save()

profesional = BasicClinic.objects.filter(is_published=True, pro_is_published = True, ppq_is_published = False)
for pro in profesional:
    pointsPro = 0
    if pro.is_claimed == True:
        pointsPro = pointsPro + 5

    ### Pricing = 15
    if pro.ivf_treatment is not None:
        pointsPro = pointsPro + 1
    if pro.ivf_treatment_cost:
        pointsPro = pointsPro + 1
    if pro.ivf_treatment_faqs:
        pointsPro = pointsPro + 1

    if pro.mild_ivf_treatment is not None:
        pointsPro = pointsPro + 1
    if pro.mild_ivf_treatment_cost:
        pointsPro = pointsPro + 1
    if pro.mild_ivf_treatment_faqs:
        pointsPro = pointsPro + 1

    if pro.ovarian_ivf_treatment is not None:
        pointsPro = pointsPro + 1
    if pro.ovarian_ivf_treatment_cost:
        pointsPro = pointsPro + 1
    if pro.ovarian_ivf_treatment_faqs:
        pointsPro = pointsPro + 1

    if pro.iui_treatment is not None:
        pointsPro = pointsPro + 1
    if pro.iui_treatment_cost:
        pointsPro = pointsPro + 1
    if pro.iui_treatment_faqs:
        pointsPro = pointsPro + 1

    if pro.icsi_treatment is not None:
        pointsPro = pointsPro + 1
    if pro.icsi_treatment_cost:
        pointsPro = pointsPro + 1
    if pro.icsi_treatment_faqs:
        pointsPro = pointsPro + 1

    ### Pricing = 18
    if pro.egg_donor_recipients is not None:
        pointsPro = pointsPro + 1
    if pro.egg_donor_recipients_cost:
        pointsPro = pointsPro + 1
    if pro.egg_donor_recipients_faqs:
        pointsPro = pointsPro + 1

    if pro.known_egg_donor_recipients is not None:
        pointsPro = pointsPro + 1
    if pro.known_egg_donor_recipients_cost:
        pointsPro = pointsPro + 1
    if pro.known_egg_donor_recipients_faqs:
        pointsPro = pointsPro + 1

    if pro.embryo_donor_recipients is not None:
        pointsPro = pointsPro + 1
    if pro.embryo_donor_recipients_cost:
        pointsPro = pointsPro + 1
    if pro.embryo_donor_recipients_faqs:
        pointsPro = pointsPro + 1

    if pro.known_embryo_donor_recipients is not None:
        pointsPro = pointsPro + 1
    if pro.known_embryo_donor_recipients_cost:
        pointsPro = pointsPro + 1
    if pro.known_embryo_donor_recipients_faqs:
        pointsPro = pointsPro + 1

    if pro.sperm_donor_recipients is not None:
        pointsPro = pointsPro + 1
    if pro.sperm_donor_recipients_cost:
        pointsPro = pointsPro + 1
    if pro.sperm_donor_recipients_faqs:
        pointsPro = pointsPro + 1

    if pro.known_sperm_donor_recipients is not None:
        pointsPro = pointsPro + 1
    if pro.known_sperm_donor_recipients_cost:
        pointsPro = pointsPro + 1
    if pro.known_sperm_donor_recipients_faqs:
        pointsPro = pointsPro + 1

    ### Pricing = 12
    if pro.egg_freezing:
        pointsPro = pointsPro + 1
    if pro.egg_freezing_cost:
        pointsPro = pointsPro + 1
    if pro.egg_freezing_faqs:
        pointsPro = pointsPro + 1

    if pro.embryo_freezing:
        pointsPro = pointsPro + 1
    if pro.embryo_freezing_cost:
        pointsPro = pointsPro + 1
    if pro.embryo_freezing_faqs:
        pointsPro = pointsPro + 1

    if pro.sperm_freezing:
        pointsPro = pointsPro + 1
    if pro.sperm_freezing_cost:
        pointsPro = pointsPro + 1
    if pro.sperm_freezing_faqs:
        pointsPro = pointsPro + 1

    if pro.surrogacy:
        pointsPro = pointsPro + 1
    if pro.surrogacy_cost:
        pointsPro = pointsPro + 1
    if pro.surrogacy_faqs:
        pointsPro = pointsPro + 1

    ### Clinic's Conditions = 2
    if pro.single_woman_treatment == True or pro.reciprocal_treatment == True or pro.hiv_patients_treatment == True or pro.sex_selection == True:
        pointsPro = pointsPro + 1
    if pro.accepts_patients_from_abroad == True:
        pointsPro = pointsPro + 1

    ### Clinic's Languages NEW = 2
    if pro.clinicEnglish is not None:
        pointsPro = pointsPro + 1
    if pro.clinicSpanish is not None or pro.clinicPortuguese is not None or pro.clinicRussian is not None or pro.clinicGerman is not None or pro.clinicChinese is not None:
        pointsPro = pointsPro + 1

    ### Clinic's Basic Information
    if pro.clinicTitle:
        pointsPro = pointsPro + 1
    if pro.description:
        pointsPro = pointsPro + 1
    if pro.treatmentLimitations:
        pointsPro = pointsPro + 1

    ### Clinic's Images
    if pro.clinic_pro_logo_pic:
        pointsPro = pointsPro + 3
    if pro.clinic_pro_photo_1:
        pointsPro = pointsPro + 1
    if pro.clinic_pro_photo_2:
        pointsPro = pointsPro + 1
    if pro.clinic_pro_photo_3:
        pointsPro = pointsPro + 1
    if pro.clinic_pro_photo_4:
        pointsPro = pointsPro + 1
    if pro.clinic_pro_photo_5:
        pointsPro = pointsPro + 1
    if pro.clinic_pro_photo_6:
        pointsPro = pointsPro + 1

    ### Clinic's Contact Information
    if pro.contact_url:
        pointsPro = pointsPro + 1
    if pro.contact_phone:
        pointsPro = pointsPro + 1
    if pro.contact_email:
        pointsPro = pointsPro + 1
    if pro.query_email:
        pointsPro = pointsPro + 1
    if pro.fertilitycommunity_email:
        pointsPro = pointsPro + 1

    ### Clinic's Social Media
    if pro.clinicFacebook:
        pointsPro = pointsPro + 1
    if pro.clinicInstagram:
        pointsPro = pointsPro + 1
    if pro.clinicTwitter:
        pointsPro = pointsPro + 1
    if pro.clinicYoutube:
        pointsPro = pointsPro + 1
    if pro.clinicLinkedIn:
        pointsPro = pointsPro + 1
    if pro.clinicPinterest:
        pointsPro = pointsPro + 1

    ### Clinic's team
    if pro.team1pic:
        pointsPro = pointsPro + 1
    if pro.team1position:
        pointsPro = pointsPro + 1
    if pro.team2pic:
        pointsPro = pointsPro + 1
    if pro.team2position:
        pointsPro = pointsPro + 1
    if pro.team3pic:
        pointsPro = pointsPro + 1
    if pro.team3position:
        pointsPro = pointsPro + 1

    ### Clinic's Independent Reviews
    if pro.clinicGoogleReviews:
        pointsPro = pointsPro + 1
    if pro.clinicTrustPilotID:
        pointsPro = pointsPro + 1

    ### Clinic's Live Chat
    if pro.clinicLiveChatChoice:
        pointsPro = pointsPro + 1

    ### Clinic's Packages
    if pro.packageClinicCounterNumber == 0:
        pointsPro = pointsPro + 0
    elif pro.packageClinicCounterNumber == 1:
        pointsPro = pointsPro + 1
    elif pro.packageClinicCounterNumber == 2:
        pointsPro = pointsPro + 2
    else:
        pointsPro = pointsPro + 0

    ### Clinic's Guest Blogs
    if pro.guestBlogCounterNumber == 0:
        pointsPro = pointsPro + 0
    elif pro.guestBlogCounterNumber == 1:
        pointsPro = pointsPro + 1
    else:
        pointsPro = pointsPro + 0

    pro.digitalTransparencyIndex = pointsPro
    pro.save()

premium = BasicClinic.objects.filter(is_published=True, pro_is_published = False, ppq_is_published = True)
for pre in premium:
    pointsPremium = 0
    if pre.is_claimed == True:
        pointsPremium = pointsPremium + 5

    ### Pricing = 15
    if pre.ivf_treatment is not None:
        pointsPremium = pointsPremium + 1
    if pre.ivf_treatment_cost:
        pointsPremium = pointsPremium + 1
    if pre.ivf_treatment_faqs:
        pointsPremium = pointsPremium + 1

    if pre.mild_ivf_treatment is not None:
        pointsPremium = pointsPremium + 1
    if pre.mild_ivf_treatment_cost:
        pointsPremium = pointsPremium + 1
    if pre.mild_ivf_treatment_faqs:
        pointsPremium = pointsPremium + 1

    if pre.ovarian_ivf_treatment is not None:
        pointsPremium = pointsPremium + 1
    if pre.ovarian_ivf_treatment_cost:
        pointsPremium = pointsPremium + 1
    if pre.ovarian_ivf_treatment_faqs:
        pointsPremium = pointsPremium + 1

    if pre.iui_treatment is not None:
        pointsPremium = pointsPremium + 1
    if pre.iui_treatment_cost:
        pointsPremium = pointsPremium + 1
    if pre.iui_treatment_faqs:
        pointsPremium = pointsPremium + 1

    if pre.icsi_treatment is not None:
        pointsPremium = pointsPremium + 1
    if pre.icsi_treatment_cost:
        pointsPremium = pointsPremium + 1
    if pre.icsi_treatment_faqs:
        pointsPremium = pointsPremium + 1

    ### Pricing = 18
    if pre.egg_donor_recipients is not None:
        pointsPremium = pointsPremium + 1
    if pre.egg_donor_recipients_cost:
        pointsPremium = pointsPremium + 1
    if pre.egg_donor_recipients_faqs:
        pointsPremium = pointsPremium + 1

    if pre.known_egg_donor_recipients is not None:
        pointsPremium = pointsPremium + 1
    if pre.known_egg_donor_recipients_cost:
        pointsPremium = pointsPremium + 1
    if pre.known_egg_donor_recipients_faqs:
        pointsPremium = pointsPremium + 1

    if pre.embryo_donor_recipients is not None:
        pointsPremium = pointsPremium + 1
    if pre.embryo_donor_recipients_cost:
        pointsPremium = pointsPremium + 1
    if pre.embryo_donor_recipients_faqs:
        pointsPremium = pointsPremium + 1

    if pre.known_embryo_donor_recipients is not None:
        pointsPremium = pointsPremium + 1
    if pre.known_embryo_donor_recipients_cost:
        pointsPremium = pointsPremium + 1
    if pre.known_embryo_donor_recipients_faqs:
        pointsPremium = pointsPremium + 1

    if pre.sperm_donor_recipients is not None:
        pointsPremium = pointsPremium + 1
    if pre.sperm_donor_recipients_cost:
        pointsPremium = pointsPremium + 1
    if pre.sperm_donor_recipients_faqs:
        pointsPremium = pointsPremium + 1

    if pre.known_sperm_donor_recipients is not None:
        pointsPremium = pointsPremium + 1
    if pre.known_sperm_donor_recipients_cost:
        pointsPremium = pointsPremium + 1
    if pre.known_sperm_donor_recipients_faqs:
        pointsPremium = pointsPremium + 1

    ### Pricing = 12
    if pre.egg_freezing:
        pointsPremium = pointsPremium + 1
    if pre.egg_freezing_cost:
        pointsPremium = pointsPremium + 1
    if pre.egg_freezing_faqs:
        pointsPremium = pointsPremium + 1

    if pre.embryo_freezing:
        pointsPremium = pointsPremium + 1
    if pre.embryo_freezing_cost:
        pointsPremium = pointsPremium + 1
    if pre.embryo_freezing_faqs:
        pointsPremium = pointsPremium + 1

    if pre.sperm_freezing:
        pointsPremium = pointsPremium + 1
    if pre.sperm_freezing_cost:
        pointsPremium = pointsPremium + 1
    if pre.sperm_freezing_faqs:
        pointsPremium = pointsPremium + 1

    if pre.surrogacy:
        pointsPremium = pointsPremium + 1
    if pre.surrogacy_cost:
        pointsPremium = pointsPremium + 1
    if pre.surrogacy_faqs:
        pointsPremium = pointsPremium + 1

    ### Clinic's Conditions = 2
    if pre.single_woman_treatment == True or pre.reciprocal_treatment == True or pre.hiv_patients_treatment == True or pre.sex_selection == True:
        pointsPremium = pointsPremium + 1
    if pre.accepts_patients_from_abroad == True:
        pointsPremium = pointsPremium + 1

    ### Clinic's Languages NEW = 2
    if pre.clinicEnglish is not None:
        pointsPremium = pointsPremium + 1
    if pre.clinicSpanish is not None or pre.clinicPortuguese is not None or pre.clinicRussian is not None or pre.clinicGerman is not None or pre.clinicChinese is not None:
        pointsPremium = pointsPremium + 1

    ### Clinic's Basic Information = 3
    if pre.clinicTitle:
        pointsPremium = pointsPremium + 1
    if pre.description:
        pointsPremium = pointsPremium + 1
    if pre.treatmentLimitations:
        pointsPremium = pointsPremium + 1

    ### Clinic's Images = 9
    if pre.clinic_pro_logo_pic:
        pointsPremium = pointsPremium + 3
    if pre.clinic_pro_photo_1:
        pointsPremium = pointsPremium + 1
    if pre.clinic_pro_photo_2:
        pointsPremium = pointsPremium + 1
    if pre.clinic_pro_photo_3:
        pointsPremium = pointsPremium + 1
    if pre.clinic_pro_photo_4:
        pointsPremium = pointsPremium + 1
    if pre.clinic_pro_photo_5:
        pointsPremium = pointsPremium + 1
    if pre.clinic_pro_photo_6:
        pointsPremium = pointsPremium + 1

    ### Clinic's Contact Information = 5
    if pre.contact_url:
        pointsPremium = pointsPremium + 1
    if pre.contact_phone:
        pointsPremium = pointsPremium + 1
    if pre.contact_email:
        pointsPremium = pointsPremium + 1
    if pre.query_email:
        pointsPremium = pointsPremium + 1
    if pre.fertilitycommunity_email:
        pointsPremium = pointsPremium + 1

    ### Clinic's Social Media = 6
    if pre.clinicFacebook:
        pointsPremium = pointsPremium + 1
    if pre.clinicInstagram:
        pointsPremium = pointsPremium + 1
    if pre.clinicTwitter:
        pointsPremium = pointsPremium + 1
    if pre.clinicYoutube:
        pointsPremium = pointsPremium + 1
    if pre.clinicLinkedIn:
        pointsPremium = pointsPremium + 1
    if pre.clinicPinterest:
        pointsPremium = pointsPremium + 1

    ### Clinic's team
    if pre.team1pic:
        pointsPremium = pointsPremium + 1
    if pre.team1position:
        pointsPremium = pointsPremium + 1
    if pre.team2pic:
        pointsPremium = pointsPremium + 1
    if pre.team2position:
        pointsPremium = pointsPremium + 1
    if pre.team3pic:
        pointsPremium = pointsPremium + 1
    if pre.team3position:
        pointsPremium = pointsPremium + 1

    ### Clinic's Independent Reviews = 4
    if pre.clinicGoogleReviews:
        pointsPremium = pointsPremium + 1
    if pre.clinicTrustPilotID:
        pointsPremium = pointsPremium + 1

    ### Clinic's Live Chat = 3
    if pre.clinicLiveChatChoice:
        pointsPremium = pointsPremium + 1

    ### Clinic's Packages = 12
    if pre.packageClinicCounterNumber == 0:
        pointsPremium = pointsPremium + 0
    elif pre.packageClinicCounterNumber == 1:
        pointsPremium = pointsPremium + 1
    elif pre.packageClinicCounterNumber == 2:
        pointsPremium = pointsPremium + 2
    elif pre.packageClinicCounterNumber == 3:
        pointsPremium = pointsPremium + 4
    elif pre.packageClinicCounterNumber == 4:
        pointsPremium = pointsPremium + 6
    elif pre.packageClinicCounterNumber == 5:
        pointsPremium = pointsPremium + 8
    elif pre.packageClinicCounterNumber == 6:
        pointsPremium = pointsPremium + 10
    else:
        pointsPremium = pointsPremium + 0

    ### Clinic's Guest Blogs = 5
    if pre.guestBlogCounterNumber == 0:
        pointsPremium = pointsPremium + 0
    elif pre.guestBlogCounterNumber == 1:
        pointsPremium = pointsPremium + 1
    elif pre.guestBlogCounterNumber == 2:
        pointsPremium = pointsPremium + 3
    elif pre.guestBlogCounterNumber == 3:
        pointsPremium = pointsPremium + 4
    elif pre.guestBlogCounterNumber == 4:
        pointsPremium = pointsPremium + 5
    elif pre.guestBlogCounterNumber == 5:
        pointsPremium = pointsPremium + 6

    pre.digitalTransparencyIndex = pointsPremium
    pre.save()
