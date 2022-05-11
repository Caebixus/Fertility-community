def calculate_dti_single(instance):
    instance.digitalTransparencyIndex = 0
    pointsBasic = 0
    # Pricing = 10
    if instance.is_claimed:
        pointsBasic = pointsBasic + 4

    # Pricing = 15
    if instance.ivf_treatment:
        pointsBasic = pointsBasic + 1
    if instance.ivf_treatment_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.ivf_treatment_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.mild_ivf_treatment:
        pointsBasic = pointsBasic + 1
    if instance.mild_ivf_treatment_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.mild_ivf_treatment_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.ovarian_ivf_treatment:
        pointsBasic = pointsBasic + 1
    if instance.ovarian_ivf_treatment_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.ovarian_ivf_treatment_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.iui_treatment:
        pointsBasic = pointsBasic + 1
    if instance.iui_treatment_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.iui_treatment_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.icsi_treatment:
        pointsBasic = pointsBasic + 1
    if instance.icsi_treatment_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.icsi_treatment_faqs is not None:
        pointsBasic = pointsBasic + 1

    # Pricing = 18
    if instance.egg_donor_recipients:
        pointsBasic = pointsBasic + 1
    if instance.egg_donor_recipients_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.egg_donor_recipients_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.known_egg_donor_recipients:
        pointsBasic = pointsBasic + 1
    if instance.known_egg_donor_recipients_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.known_egg_donor_recipients_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.embryo_donor_recipients:
        pointsBasic = pointsBasic + 1
    if instance.embryo_donor_recipients_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.embryo_donor_recipients_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.known_embryo_donor_recipients:
        pointsBasic = pointsBasic + 1
    if instance.known_embryo_donor_recipients_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.known_embryo_donor_recipients_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.sperm_donor_recipients:
        pointsBasic = pointsBasic + 1
    if instance.sperm_donor_recipients_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.sperm_donor_recipients_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.known_sperm_donor_recipients:
        pointsBasic = pointsBasic + 1
    if instance.known_sperm_donor_recipients_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.known_sperm_donor_recipients_faqs is not None:
        pointsBasic = pointsBasic + 1

    # Pricing = 12
    if instance.egg_freezing:
        pointsBasic = pointsBasic + 1
    if instance.egg_freezing_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.egg_freezing_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.embryo_freezing:
        pointsBasic = pointsBasic + 1
    if instance.embryo_freezing_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.embryo_freezing_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.sperm_freezing:
        pointsBasic = pointsBasic + 1
    if instance.sperm_freezing_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.sperm_freezing_faqs is not None:
        pointsBasic = pointsBasic + 1

    if instance.surrogacy:
        pointsBasic = pointsBasic + 1
    if instance.surrogacy_cost is not None:
        pointsBasic = pointsBasic + 1
    if instance.surrogacy_faqs is not None:
        pointsBasic = pointsBasic + 1

    # Clinic's Payment Information = 1
    if instance.payment_type_cash or instance.payment_type_major_credit_cards or instance.payment_type_debit_cards or instance.payment_type_check or instance.payment_type_cryptocurrency or instance.payment_type_wire_transfer:
        pointsBasic = pointsBasic + 1

    # Clinic's Conditions = 2
    if instance.single_woman_treatment or instance.reciprocal_treatment or instance.hiv_patients_treatment or instance.sex_selection:
        pointsBasic = pointsBasic + 1
    if instance.accepts_patients_from_abroad:
        pointsBasic = pointsBasic + 1

    # Clinic's Languages NEW = 2
    if instance.clinicEnglish is not None:
        pointsBasic = pointsBasic + 1
    if instance.clinicSpanish is not None or instance.clinicPortuguese is not None or instance.clinicRussian is not None or instance.clinicGerman is not None or instance.clinicChinese is not None:
        pointsBasic = pointsBasic + 1

    # Clinic's Basic Information = 1
    if instance.clinicTitle != None:
        pointsBasic = pointsBasic + 1
    if instance.description:
        pointsBasic = pointsBasic + 1
    if instance.treatmentLimitations:
        pointsBasic = pointsBasic + 1

    # Clinic's Images = 9
    if instance.clinic_pro_logo_pic:
        pointsBasic = pointsBasic + 3
    if instance.clinic_pro_photo_1:
        pointsBasic = pointsBasic + 1
    if instance.clinic_pro_photo_2:
        pointsBasic = pointsBasic + 1
    if instance.clinic_pro_photo_3:
        pointsBasic = pointsBasic + 1
    if instance.clinic_pro_photo_4:
        pointsBasic = pointsBasic + 1
    if instance.clinic_pro_photo_5:
        pointsBasic = pointsBasic + 1
    if instance.clinic_pro_photo_6:
        pointsBasic = pointsBasic + 1

    # Clinic's Contact Information = 5
    if instance.contact_url is not None:
        pointsBasic = pointsBasic + 1
    if instance.contact_phone is not None:
        pointsBasic = pointsBasic + 1
    if instance.contact_email is not None:
        pointsBasic = pointsBasic + 1
    if instance.query_email is not None:
        pointsBasic = pointsBasic + 1
    if instance.fertilitycommunity_email is not None:
        pointsBasic = pointsBasic + 1

    # Clinic's Social Media = 6
    if instance.clinicFacebook is not None or instance.clinicInstagram is not None:
        pointsBasic = pointsBasic + 3
    if instance.clinicTwitter is not None or instance.clinicYoutube is not None or instance.clinicLinkedIn is not None or instance.clinicPinterest is not None:
        pointsBasic = pointsBasic + 2

    # --- Check if PRO or PREMIUM:
    if instance.pro_is_published==True and instance.ppq_is_published==False:
        # Clinic's Independent Reviews
        if instance.clinicGoogleReviews is not None:
            pointsBasic = pointsBasic + 1
        if instance.clinicTrustPilotID is not None:
            pointsBasic = pointsBasic + 1

        # Clinic's Live Chat
        if instance.clinicLiveChatChoice is not None:
            pointsBasic = pointsBasic + 1

        # Clinic's Packages
        if instance.packageClinicCounterNumber == 0:
            pointsBasic = pointsBasic + 0
        elif instance.packageClinicCounterNumber == 1:
            pointsBasic = pointsBasic + 1
        elif instance.packageClinicCounterNumber == 2:
            pointsBasic = pointsBasic + 2
        else:
            pointsBasic = pointsBasic + 0

        # Clinic's Guest Blogs
        if instance.guestBlogCounterNumber == 0:
            pointsBasic = pointsBasic + 0
        elif instance.guestBlogCounterNumber == 1:
            pointsBasic = pointsBasic + 1
        else:
            pointsBasic = pointsBasic + 0


    elif instance.pro_is_published==False and instance.ppq_is_published==True:
        # Clinic's Independent Reviews = 4
        if instance.clinicGoogleReviews is not None:
            pointsBasic = pointsBasic + 1
        if instance.clinicTrustPilotID is not None:
            pointsBasic = pointsBasic + 1

        # Clinic's Live Chat = 3
        if instance.clinicLiveChatChoice is not None:
            pointsBasic = pointsBasic + 1

        # Clinic's Packages = 12
        if instance.packageClinicCounterNumber == 0:
            pointsBasic = pointsBasic + 0
        elif instance.packageClinicCounterNumber == 1:
            pointsBasic = pointsBasic + 1
        elif instance.packageClinicCounterNumber == 2:
            pointsBasic = pointsBasic + 2
        elif instance.packageClinicCounterNumber == 3:
            pointsBasic = pointsBasic + 4
        elif instance.packageClinicCounterNumber == 4:
            pointsBasic = pointsBasic + 6
        elif instance.packageClinicCounterNumber == 5:
            pointsBasic = pointsBasic + 8
        elif instance.packageClinicCounterNumber == 6:
            pointsBasic = pointsBasic + 10
        else:
            pointsBasic = pointsBasic + 0

        # Clinic's Guest Blogs = 5
        if instance.guestBlogCounterNumber == 0:
            pointsBasic = pointsBasic + 0
        elif instance.guestBlogCounterNumber == 1:
            pointsBasic = pointsBasic + 1
        elif instance.guestBlogCounterNumber == 2:
            pointsBasic = pointsBasic + 3
        elif instance.guestBlogCounterNumber == 3:
            pointsBasic = pointsBasic + 4
        elif instance.guestBlogCounterNumber == 4:
            pointsBasic = pointsBasic + 5
        elif instance.guestBlogCounterNumber == 5:
            pointsBasic = pointsBasic + 6

    else:
        pass

    instance.digitalTransparencyIndex = pointsBasic