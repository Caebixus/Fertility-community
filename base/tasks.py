from __future__ import absolute_import, unicode_literals
from celery import task

from django.utils import timezone
from datetime import timedelta

from clinic.models import BasicClinic

import logging
logger = logging.getLogger(__name__)

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
django.setup()

from .costs_tasks import tasks_country_average_treatment_costs

import requests
from base.models import CurrenciesExchangeRates


@task()
def calculate_dti():
    clinics = BasicClinic.objects.filter(is_published=True)
    basic = clinics.exclude(pro_is_published=True, ppq_is_published=True)
    for bas in basic:
        bas.digitalTransparencyIndex = 0
        pointsBasic = 0
        # Pricing = 10
        if bas.is_claimed:
            pointsBasic = pointsBasic + 4

        # Pricing = 15
        if bas.ivf_treatment:
            pointsBasic = pointsBasic + 1
        if bas.ivf_treatment_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.ivf_treatment_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.mild_ivf_treatment:
            pointsBasic = pointsBasic + 1
        if bas.mild_ivf_treatment_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.mild_ivf_treatment_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.ovarian_ivf_treatment:
            pointsBasic = pointsBasic + 1
        if bas.ovarian_ivf_treatment_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.ovarian_ivf_treatment_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.iui_treatment:
            pointsBasic = pointsBasic + 1
        if bas.iui_treatment_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.iui_treatment_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.icsi_treatment:
            pointsBasic = pointsBasic + 1
        if bas.icsi_treatment_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.icsi_treatment_faqs is not None:
            pointsBasic = pointsBasic + 1

        # Pricing = 18
        if bas.egg_donor_recipients:
            pointsBasic = pointsBasic + 1
        if bas.egg_donor_recipients_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.egg_donor_recipients_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.known_egg_donor_recipients:
            pointsBasic = pointsBasic + 1
        if bas.known_egg_donor_recipients_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.known_egg_donor_recipients_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.embryo_donor_recipients:
            pointsBasic = pointsBasic + 1
        if bas.embryo_donor_recipients_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.embryo_donor_recipients_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.known_embryo_donor_recipients:
            pointsBasic = pointsBasic + 1
        if bas.known_embryo_donor_recipients_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.known_embryo_donor_recipients_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.sperm_donor_recipients:
            pointsBasic = pointsBasic + 1
        if bas.sperm_donor_recipients_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.sperm_donor_recipients_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.known_sperm_donor_recipients:
            pointsBasic = pointsBasic + 1
        if bas.known_sperm_donor_recipients_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.known_sperm_donor_recipients_faqs is not None:
            pointsBasic = pointsBasic + 1

        # Pricing = 12
        if bas.egg_freezing:
            pointsBasic = pointsBasic + 1
        if bas.egg_freezing_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.egg_freezing_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.embryo_freezing:
            pointsBasic = pointsBasic + 1
        if bas.embryo_freezing_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.embryo_freezing_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.sperm_freezing:
            pointsBasic = pointsBasic + 1
        if bas.sperm_freezing_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.sperm_freezing_faqs is not None:
            pointsBasic = pointsBasic + 1

        if bas.surrogacy:
            pointsBasic = pointsBasic + 1
        if bas.surrogacy_cost is not None:
            pointsBasic = pointsBasic + 1
        if bas.surrogacy_faqs is not None:
            pointsBasic = pointsBasic + 1

        # Clinic's Payment Information = 1
        if bas.payment_type_cash or bas.payment_type_major_credit_cards or bas.payment_type_debit_cards or bas.payment_type_check or bas.payment_type_cryptocurrency or bas.payment_type_wire_transfer:
            pointsBasic = pointsBasic + 1

        # Clinic's Conditions = 2
        if bas.single_woman_treatment or bas.reciprocal_treatment or bas.hiv_patients_treatment or bas.sex_selection:
            pointsBasic = pointsBasic + 1
        if bas.accepts_patients_from_abroad:
            pointsBasic = pointsBasic + 1

        # Clinic's Languages NEW = 2
        if bas.clinicEnglish is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicSpanish is not None or bas.clinicPortuguese is not None or bas.clinicRussian is not None or bas.clinicGerman is not None or bas.clinicChinese is not None:
            pointsBasic = pointsBasic + 1

        # Clinic's Basic Information = 1
        if bas.clinicTitle is not None:
            pointsBasic = pointsBasic + 1
        if bas.description is not None:
            pointsBasic = pointsBasic + 1
        if bas.treatmentLimitations is not None:
            pointsBasic = pointsBasic + 1

        # Clinic's Images = 9
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

        # Clinic's Contact Information = 5
        if bas.contact_url is not None:
            pointsBasic = pointsBasic + 1
        if bas.contact_phone is not None:
            pointsBasic = pointsBasic + 1
        if bas.contact_email is not None:
            pointsBasic = pointsBasic + 1
        if bas.query_email is not None:
            pointsBasic = pointsBasic + 1
        if bas.fertilitycommunity_email is not None:
            pointsBasic = pointsBasic + 1

        # Clinic's Social Media = 6
        if bas.clinicFacebook is not None or bas.clinicInstagram is not None:
            pointsBasic = pointsBasic + 3
        if bas.clinicTwitter is not None or bas.clinicYoutube is not None or bas.clinicLinkedIn is not None or bas.clinicPinterest is not None:
            pointsBasic = pointsBasic + 2

        bas.digitalTransparencyIndex = pointsBasic
        bas.save()

    profesional = clinics.filter(pro_is_published=True).exclude(ppq_is_published=True)
    for pro in profesional:
        pro.digitalTransparencyIndex = 0
        pointsPro = 0
        # Pricing = 10
        if pro.is_claimed:
            pointsPro = pointsPro + 4

        # Pricing = 15
        if pro.ivf_treatment:
            pointsPro = pointsPro + 1
        if pro.ivf_treatment_cost is not None:
            pointsPro = pointsPro + 1
        if pro.ivf_treatment_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.mild_ivf_treatment:
            pointsPro = pointsPro + 1
        if pro.mild_ivf_treatment_cost is not None:
            pointsPro = pointsPro + 1
        if pro.mild_ivf_treatment_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.ovarian_ivf_treatment:
            pointsPro = pointsPro + 1
        if pro.ovarian_ivf_treatment_cost is not None:
            pointsPro = pointsPro + 1
        if pro.ovarian_ivf_treatment_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.iui_treatment:
            pointsPro = pointsPro + 1
        if pro.iui_treatment_cost is not None:
            pointsPro = pointsPro + 1
        if pro.iui_treatment_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.icsi_treatment:
            pointsPro = pointsPro + 1
        if pro.icsi_treatment_cost is not None:
            pointsPro = pointsPro + 1
        if pro.icsi_treatment_faqs is not None:
            pointsPro = pointsPro + 1

        # Pricing = 18
        if pro.egg_donor_recipients:
            pointsPro = pointsPro + 1
        if pro.egg_donor_recipients_cost is not None:
            pointsPro = pointsPro + 1
        if pro.egg_donor_recipients_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.known_egg_donor_recipients:
            pointsPro = pointsPro + 1
        if pro.known_egg_donor_recipients_cost is not None:
            pointsPro = pointsPro + 1
        if pro.known_egg_donor_recipients_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.embryo_donor_recipients:
            pointsPro = pointsPro + 1
        if pro.embryo_donor_recipients_cost is not None:
            pointsPro = pointsPro + 1
        if pro.embryo_donor_recipients_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.known_embryo_donor_recipients:
            pointsPro = pointsPro + 1
        if pro.known_embryo_donor_recipients_cost is not None:
            pointsPro = pointsPro + 1
        if pro.known_embryo_donor_recipients_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.sperm_donor_recipients:
            pointsPro = pointsPro + 1
        if pro.sperm_donor_recipients_cost is not None:
            pointsPro = pointsPro + 1
        if pro.sperm_donor_recipients_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.known_sperm_donor_recipients:
            pointsPro = pointsPro + 1
        if pro.known_sperm_donor_recipients_cost is not None:
            pointsPro = pointsPro + 1
        if pro.known_sperm_donor_recipients_faqs is not None:
            pointsPro = pointsPro + 1

        # Pricing = 12
        if pro.egg_freezing:
            pointsPro = pointsPro + 1
        if pro.egg_freezing_cost is not None:
            pointsPro = pointsPro + 1
        if pro.egg_freezing_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.embryo_freezing:
            pointsPro = pointsPro + 1
        if pro.embryo_freezing_cost is not None:
            pointsPro = pointsPro + 1
        if pro.embryo_freezing_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.sperm_freezing:
            pointsPro = pointsPro + 1
        if pro.sperm_freezing_cost is not None:
            pointsPro = pointsPro + 1
        if pro.sperm_freezing_faqs is not None:
            pointsPro = pointsPro + 1

        if pro.surrogacy:
            pointsPro = pointsPro + 1
        if pro.surrogacy_cost is not None:
            pointsPro = pointsPro + 1
        if pro.surrogacy_faqs is not None:
            pointsPro = pointsPro + 1

        # Clinic's Payment Information = 1
        if pro.payment_type_cash or pro.payment_type_major_credit_cards or pro.payment_type_debit_cards or pro.payment_type_check or pro.payment_type_cryptocurrency or pro.payment_type_wire_transfer:
            pointsPro = pointsPro + 1

        # Clinic's Conditions = 2
        if pro.single_woman_treatment or pro.reciprocal_treatment or pro.hiv_patients_treatment or pro.sex_selection:
            pointsPro = pointsPro + 1
        if pro.accepts_patients_from_abroad:
            pointsPro = pointsPro + 1

        # Clinic's Languages NEW = 2
        if pro.clinicEnglish is not None:
            pointsPro = pointsPro + 1
        if pro.clinicSpanish is not None or pro.clinicPortuguese is not None or pro.clinicRussian is not None or pro.clinicGerman is not None or pro.clinicChinese is not None:
            pointsPro = pointsPro + 1

        # Clinic's Basic Information = 1
        if pro.clinicTitle is not None:
            pointsPro = pointsPro + 1
        if pro.description is not None:
            pointsPro = pointsPro + 1
        if pro.treatmentLimitations is not None:
            pointsPro = pointsPro + 1

        # Clinic's Images = 9
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

        # Clinic's Contact Information = 5
        if pro.contact_url is not None:
            pointsPro = pointsPro + 1
        if pro.contact_phone is not None:
            pointsPro = pointsPro + 1
        if pro.contact_email is not None:
            pointsPro = pointsPro + 1
        if pro.query_email is not None:
            pointsPro = pointsPro + 1
        if pro.fertilitycommunity_email is not None:
            pointsPro = pointsPro + 1

        # Clinic's Social Media = 6
        if pro.clinicFacebook is not None or pro.clinicInstagram is not None:
            pointsPro = pointsPro + 3
        if pro.clinicTwitter is not None or pro.clinicYoutube is not None or pro.clinicLinkedIn is not None or pro.clinicPinterest is not None:
            pointsPro = pointsPro + 2

        # Clinic's team
        if pro.team1pic:
            pointsPro = pointsPro + 1
        if pro.team1position is not None:
            pointsPro = pointsPro + 1
        if pro.team2pic:
            pointsPro = pointsPro + 1
        if pro.team2position is not None:
            pointsPro = pointsPro + 1
        if pro.team3pic:
            pointsPro = pointsPro + 1
        if pro.team3position is not None:
            pointsPro = pointsPro + 1

        # Clinic's Independent Reviews
        if pro.clinicGoogleReviews is not None:
            pointsPro = pointsPro + 1
        if pro.clinicTrustPilotID is not None:
            pointsPro = pointsPro + 1

        # Clinic's Live Chat
        if pro.clinicLiveChatChoice is not None:
            pointsPro = pointsPro + 1

        # Clinic's Packages
        if pro.packageClinicCounterNumber == 0:
            pointsPro = pointsPro + 0
        elif pro.packageClinicCounterNumber == 1:
            pointsPro = pointsPro + 1
        elif pro.packageClinicCounterNumber == 2:
            pointsPro = pointsPro + 2
        else:
            pointsPro = pointsPro + 0

        # Clinic's Guest Blogs
        if pro.guestBlogCounterNumber == 0:
            pointsPro = pointsPro + 0
        elif pro.guestBlogCounterNumber == 1:
            pointsPro = pointsPro + 1
        else:
            pointsPro = pointsPro + 0

        pro.digitalTransparencyIndex = pointsPro
        pro.save()

    premium = clinics.filter(ppq_is_published=True).exclude(pro_is_published=True)
    for pre in premium:
        pre.digitalTransparencyIndex = 0
        pointsPremium = 0
        if pre.is_claimed:
            pointsPremium = pointsPremium + 4

        # Pricing = 15
        if pre.ivf_treatment:
            pointsPremium = pointsPremium + 1
        if pre.ivf_treatment_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.ivf_treatment_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.mild_ivf_treatment:
            pointsPremium = pointsPremium + 1
        if pre.mild_ivf_treatment_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.mild_ivf_treatment_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.ovarian_ivf_treatment:
            pointsPremium = pointsPremium + 1
        if pre.ovarian_ivf_treatment_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.ovarian_ivf_treatment_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.iui_treatment:
            pointsPremium = pointsPremium + 1
        if pre.iui_treatment_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.iui_treatment_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.icsi_treatment:
            pointsPremium = pointsPremium + 1
        if pre.icsi_treatment_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.icsi_treatment_faqs is not None:
            pointsPremium = pointsPremium + 1

        # Pricing = 18
        if pre.egg_donor_recipients:
            pointsPremium = pointsPremium + 1
        if pre.egg_donor_recipients_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.egg_donor_recipients_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.known_egg_donor_recipients:
            pointsPremium = pointsPremium + 1
        if pre.known_egg_donor_recipients_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.known_egg_donor_recipients_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.embryo_donor_recipients:
            pointsPremium = pointsPremium + 1
        if pre.embryo_donor_recipients_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.embryo_donor_recipients_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.known_embryo_donor_recipients:
            pointsPremium = pointsPremium + 1
        if pre.known_embryo_donor_recipients_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.known_embryo_donor_recipients_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.sperm_donor_recipients:
            pointsPremium = pointsPremium + 1
        if pre.sperm_donor_recipients_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.sperm_donor_recipients_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.known_sperm_donor_recipients:
            pointsPremium = pointsPremium + 1
        if pre.known_sperm_donor_recipients_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.known_sperm_donor_recipients_faqs is not None:
            pointsPremium = pointsPremium + 1

        # Pricing = 12
        if pre.egg_freezing:
            pointsPremium = pointsPremium + 1
        if pre.egg_freezing_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.egg_freezing_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.embryo_freezing:
            pointsPremium = pointsPremium + 1
        if pre.embryo_freezing_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.embryo_freezing_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.sperm_freezing:
            pointsPremium = pointsPremium + 1
        if pre.sperm_freezing_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.sperm_freezing_faqs is not None:
            pointsPremium = pointsPremium + 1

        if pre.surrogacy:
            pointsPremium = pointsPremium + 1
        if pre.surrogacy_cost is not None:
            pointsPremium = pointsPremium + 1
        if pre.surrogacy_faqs is not None:
            pointsPremium = pointsPremium + 1

        # Clinic's Payment Information = 1
        if pre.payment_type_cash or pre.payment_type_major_credit_cards or pre.payment_type_debit_cards or pre.payment_type_check or pre.payment_type_cryptocurrency or pre.payment_type_wire_transfer:
            pointsPremium = pointsPremium + 1

        # Clinic's Conditions = 2
        if pre.single_woman_treatment or pre.reciprocal_treatment or pre.hiv_patients_treatment or pre.sex_selection:
            pointsPremium = pointsPremium + 1
        if pre.accepts_patients_from_abroad:
            pointsPremium = pointsPremium + 1

        # Clinic's Languages NEW = 2
        if pre.clinicEnglish is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicSpanish is not None or pre.clinicPortuguese is not None or pre.clinicRussian is not None or pre.clinicGerman is not None or pre.clinicChinese is not None:
            pointsPremium = pointsPremium + 1

        # Clinic's Basic Information = 3
        if pre.clinicTitle is not None:
            pointsPremium = pointsPremium + 1
        if pre.description is not None:
            pointsPremium = pointsPremium + 1
        if pre.treatmentLimitations is not None:
            pointsPremium = pointsPremium + 1

        # Clinic's Images = 9
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

        # Clinic's Contact Information = 5
        if pre.contact_url is not None:
            pointsPremium = pointsPremium + 1
        if pre.contact_phone is not None:
            pointsPremium = pointsPremium + 1
        if pre.contact_email is not None:
            pointsPremium = pointsPremium + 1
        if pre.query_email is not None:
            pointsPremium = pointsPremium + 1
        if pre.fertilitycommunity_email is not None:
            pointsPremium = pointsPremium + 1

        # Clinic's Social Media = 6
        if pre.clinicFacebook is not None or pre.clinicInstagram is not None:
            pointsPremium = pointsPremium + 3
        if pre.clinicTwitter is not None or pre.clinicYoutube is not None or pre.clinicLinkedIn is not None or pre.clinicPinterest is not None:
            pointsPremium = pointsPremium + 2

        # Clinic's team
        if pre.team1pic:
            pointsPremium = pointsPremium + 1
        if pre.team1position is not None:
            pointsPremium = pointsPremium + 1
        if pre.team2pic:
            pointsPremium = pointsPremium + 1
        if pre.team2position is not None:
            pointsPremium = pointsPremium + 1
        if pre.team3pic:
            pointsPremium = pointsPremium + 1
        if pre.team3position is not None:
            pointsPremium = pointsPremium + 1

        # Clinic's Independent Reviews = 4
        if pre.clinicGoogleReviews is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicTrustPilotID is not None:
            pointsPremium = pointsPremium + 1

        # Clinic's Live Chat = 3
        if pre.clinicLiveChatChoice is not None:
            pointsPremium = pointsPremium + 1

        # Clinic's Packages = 12
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

        # Clinic's Guest Blogs = 5
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


@task()
def currencies_rate_update():

    response = requests.get(f'http://api.currencylayer.com/live?access_key=c36176bb29d50514cb4c0181503a4fb9&currencies=EUR,CZK,GBP, MXN, INR, CAD')
    data = response.json()
    new_usd_to_czk_exchange = data['quotes']['USDCZK']
    new_usd_to_eur_exchange = data['quotes']['USDEUR']
    new_usd_to_gbp_exchange = data['quotes']['USDGBP']
    new_usd_to_mxn_exchange = data['quotes']['USDMXN']
    new_usd_to_inr_exchange = data['quotes']['USDINR']
    new_usd_to_cad_exchange = data['quotes']['USDCAD']


    rate = CurrenciesExchangeRates.objects.get(pk=1)
    rate.usd_to_czk_exchange = new_usd_to_czk_exchange
    rate.usd_to_eur_exchange = new_usd_to_eur_exchange
    rate.usd_to_gbp_exchange = new_usd_to_gbp_exchange
    rate.usd_to_mxn_exchange = new_usd_to_mxn_exchange
    rate.usd_to_inr_exchange = new_usd_to_inr_exchange
    rate.usd_to_cad_exchange = new_usd_to_cad_exchange
    rate.save()


@task()
def calculate_active_clinic():
    last_month = timezone.now() - timedelta(days=30)
    last_3_months = timezone.now() - timedelta(days=90)
    last_6_months = timezone.now() - timedelta(days=180)
    clinics = BasicClinic.objects.filter(is_published=True, is_claimed=True)
    for clinic in clinics:
        if clinic.clinicOwner.last_login > last_month:
            clinic.active_30 = True
            clinic.save()
        else:
            clinic.active_30 = False
            clinic.save()
        if clinic.clinicOwner.last_login > last_3_months:
            clinic.active_90 = True
            clinic.save()
        else:
            clinic.active_90 = False
            clinic.save()
        if clinic.clinicOwner.last_login > last_6_months:
            clinic.active_180 = True
            clinic.save()
        else:
            clinic.active_180 = False
            clinic.save()


@task()
calculate_average_country_costs()

# @task()
# def calculate_package_number
#     todayDate = timezone.now()
#     pro_clinics = BasicClinic.objects.filter(is_published=True, ppq_is_published=True).exclude(pro_is_published=True)
#     for clinic in pro_clinics:
#         notactivelisting = Package.objects.filter(package_end_list_date__lte=todayDate)
#         notactivelisting = notactivelisting.filter(packageclinic_id=clinic)
#         clinic.packageClinicCounterNumber = 0 ?
#
#
#     ppq_clinics = BasicClinic.objects.filter(is_published=True, pro_is_published=True).exclude(ppq_is_published=True)
#     for clinic in ppq_clinics: