from __future__ import absolute_import, unicode_literals
from celery import shared_task

import logging
logger = logging.getLogger(__name__)

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
django.setup()

import requests
from base.models import CurrenciesExchangeRates
from clinic.models import BasicClinic

@shared_task
def calculate_dti():
    basic = BasicClinic.objects.filter(is_published=True).exclude(pro_is_published = True, ppq_is_published = True)
    for bas in basic:
        pointsBasic = 0
        if bas.is_claimed == True:
            pointsBasic = pointsBasic + 7

        ### Pricing
        if bas.ivf_treatment_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.mild_ivf_treatment_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.ovarian_ivf_treatment_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.iui_treatment_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.icsi_treatment_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.egg_donor_recipients_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.embryo_donor_recipients_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.sperm_donor_recipients_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.egg_freezing_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.embryo_freezing_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.sperm_freezing_cost is not None:
            pointsBasic = pointsBasic + 2
        if bas.surrogacy_cost is not None:
            pointsBasic = pointsBasic + 2

        ### Clinic's Basic Information
        if bas.clinicTitle is not None:
            pointsBasic = pointsBasic + 1

        ### Clinic's Images
        if bas.clinic_pro_logo_pic is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinic_pro_photo_1 is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinic_pro_photo_2 is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinic_pro_photo_3 is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinic_pro_photo_4 is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinic_pro_photo_5 is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinic_pro_photo_6 is not None:
            pointsBasic = pointsBasic + 1

        ### Clinic's Contact Information
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

        ### Clinic's Languages
        if bas.clinicEnglish is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicSpanish is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicPortuguese is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicRussian is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicGerman is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicChinese is not None:
            pointsBasic = pointsBasic + 1

        ### Clinic's Social Media
        if bas.clinicFacebook is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicInstagram is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicTwitter is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicYoutube is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicLinkedIn is not None:
            pointsBasic = pointsBasic + 1
        if bas.clinicPinterest is not None:
            pointsBasic = pointsBasic + 1

        bas.digitalTransparencyIndex = pointsBasic
        bas.save()

    pro = BasicClinic.objects.filter(is_published=True, pro_is_published = True).exclude(ppq_is_published = True)
    for pro in pro:
        pointsPro = 0
        if pro.is_claimed == True:
            pointsPro = pointsPro + 7

        ### Pricing
        if pro.ivf_treatment_cost is not None:
            pointsPro = pointsPro + 2
        if pro.mild_ivf_treatment_cost is not None:
            pointsPro = pointsPro + 2
        if pro.ovarian_ivf_treatment_cost is not None:
            pointsPro = pointsPro + 2
        if pro.iui_treatment_cost is not None:
            pointsPro = pointsPro + 2
        if pro.icsi_treatment_cost is not None:
            pointsPro = pointsPro + 2
        if pro.egg_donor_recipients_cost is not None:
            pointsPro = pointsPro + 2
        if pro.embryo_donor_recipients_cost is not None:
            pointsPro = pointsPro + 2
        if pro.sperm_donor_recipients_cost is not None:
            pointsPro = pointsPro + 2
        if pro.egg_freezing_cost is not None:
            pointsPro = pointsPro + 2
        if pro.embryo_freezing_cost is not None:
            pointsPro = pointsPro + 2
        if pro.sperm_freezing_cost is not None:
            pointsPro = pointsPro + 2
        if pro.surrogacy_cost is not None:
            pointsPro = pointsPro + 2

        ### Clinic's Basic Information
        if pro.clinicTitle is not None:
            pointsPro = pointsPro + 1
        if pro.description is not None:
            pointsPro = pointsPro + 1
        if pro.treatmentLimitations is not None:
            pointsPro = pointsPro + 1

        ### Clinic's Images
        if pro.clinic_pro_logo_pic is not None:
            pointsPro = pointsPro + 1
        if pro.clinic_pro_photo_1 is not None:
            pointsPro = pointsPro + 1
        if pro.clinic_pro_photo_2 is not None:
            pointsPro = pointsPro + 1
        if pro.clinic_pro_photo_3 is not None:
            pointsPro = pointsPro + 1
        if pro.clinic_pro_photo_4 is not None:
            pointsPro = pointsPro + 1
        if pro.clinic_pro_photo_5 is not None:
            pointsPro = pointsPro + 1
        if pro.clinic_pro_photo_6 is not None:
            pointsPro = pointsPro + 1

        ### Clinic's Contact Information
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

        ### Clinic's Languages
        if pro.clinicEnglish is not None:
            pointsPro = pointsPro + 1
        if pro.clinicSpanish is not None:
            pointsPro = pointsPro + 1
        if pro.clinicPortuguese is not None:
            pointsPro = pointsPro + 1
        if pro.clinicRussian is not None:
            pointsPro = pointsPro + 1
        if pro.clinicGerman is not None:
            pointsPro = pointsPro + 1
        if pro.clinicChinese is not None:
            pointsPro = pointsPro + 1

        ### Clinic's Social Media
        if pro.clinicFacebook is not None:
            pointsPro = pointsPro + 1
        if pro.clinicInstagram is not None:
            pointsPro = pointsPro + 1
        if pro.clinicTwitter is not None:
            pointsPro = pointsPro + 1
        if pro.clinicYoutube is not None:
            pointsPro = pointsPro + 1
        if pro.clinicLinkedIn is not None:
            pointsPro = pointsPro + 1
        if pro.clinicPinterest is not None:
            pointsPro = pointsPro + 1

        ### Clinic's Team
        if pro.team1name is not None:
            pointsPro = pointsPro + 1
        if pro.team1pic is not None:
            pointsPro = pointsPro + 1
        if pro.team2name is not None:
            pointsPro = pointsPro + 1
        if pro.team2pic is not None:
            pointsPro = pointsPro + 1
        if pro.team3name is not None:
            pointsPro = pointsPro + 1
        if pro.team3pic is not None:
            pointsPro = pointsPro + 1

        ### Clinic's Independent Reviews
        if pro.clinicGoogleReviews is not None:
            pointsPro = pointsPro + 1
        if pro.clinicTrustPilotID is not None:
            pointsPro = pointsPro + 1

        ### Clinic's Live Chat
        if pro.clinicLiveChatChoice is not None:
            if pro.clinicChatraCode or pro.clinicLiveChatCode or pro.clinicOlarkCode or pro.clinicTidioCode is not None:
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

    premium = BasicClinic.objects.filter(is_published=True, ppq_is_published = True).exclude(pro_is_published = True)
    for pre in premium:
        pointsPremium = 0
        if pre.is_claimed == True:
            pointsPremium = pointsPremium + 7

        ### Pricing
        if pre.ivf_treatment_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.mild_ivf_treatment_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.ovarian_ivf_treatment_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.iui_treatment_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.icsi_treatment_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.egg_donor_recipients_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.embryo_donor_recipients_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.sperm_donor_recipients_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.egg_freezing_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.embryo_freezing_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.sperm_freezing_cost is not None:
            pointsPremium = pointsPremium + 2
        if pre.surrogacy_cost is not None:
            pointsPremium = pointsPremium + 2

        ### Clinic's Basic Information
        if pre.clinicTitle is not None:
            pointsPremium = pointsPremium + 1
        if pre.description is not None:
            pointsPremium = pointsPremium + 1
        if pre.treatmentLimitations is not None:
            pointsPremium = pointsPremium + 1

        ### Clinic's Images
        if pre.clinic_pro_logo_pic is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinic_pro_photo_1 is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinic_pro_photo_2 is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinic_pro_photo_3 is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinic_pro_photo_4 is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinic_pro_photo_5 is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinic_pro_photo_6 is not None:
            pointsPremium = pointsPremium + 1

        ### Clinic's Contact Information
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

        ### Clinic's Languages
        if pre.clinicEnglish is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicSpanish is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicPortuguese is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicRussian is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicGerman is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicChinese is not None:
            pointsPremium = pointsPremium + 1

        ### Clinic's Social Media
        if pre.clinicFacebook is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicInstagram is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicTwitter is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicYoutube is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicLinkedIn is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicPinterest is not None:
            pointsPremium = pointsPremium + 1

        ### Clinic's Team
        if pre.team1name is not None:
            pointsPremium = pointsPremium + 1
        if pre.team1pic is not None:
            pointsPremium = pointsPremium + 1
        if pre.team2name is not None:
            pointsPremium = pointsPremium + 1
        if pre.team2pic is not None:
            pointsPremium = pointsPremium + 1
        if pre.team3name is not None:
            pointsPremium = pointsPremium + 1
        if pre.team3pic is not None:
            pointsPremium = pointsPremium + 1

        ### Clinic's Independent Reviews
        if pre.clinicGoogleReviews is not None:
            pointsPremium = pointsPremium + 1
        if pre.clinicTrustPilotID is not None:
            pointsPremium = pointsPremium + 1

        ### Clinic's Live Chat
        if pre.clinicLiveChatChoice is not None:
            if pre.clinicChatraCode or pre.clinicLiveChatCode or pre.clinicOlarkCode or pre.clinicTidioCode is not None:
                pointsPremium = pointsPremium + 1

        ### Clinic's Packages
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
            pointsPremium = pointsPremium + 7
        elif pre.packageClinicCounterNumber == 6:
            pointsPremium = pointsPremium + 8
        else:
            pointsPremium = pointsPremium + 0

        ### Clinic's Guest Blogs
        if pre.guestBlogCounterNumber == 0:
            pointsPremium = pointsPremium + 0
        elif pre.guestBlogCounterNumber == 1:
            pointsPremium = pointsPremium + 1
        elif pre.guestBlogCounterNumber == 2:
            pointsPremium = pointsPremium + 2
        elif pre.guestBlogCounterNumber == 3:
            pointsPremium = pointsPremium + 3
        elif pre.guestBlogCounterNumber == 4:
            pointsPremium = pointsPremium + 4
        elif pre.guestBlogCounterNumber == 5:
            pointsPremium = pointsPremium + 5

        pre.digitalTransparencyIndex = pointsPremium
        pre.save()

@shared_task
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
