from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from clinic.models import BasicClinic
from location.models.country_models import *

year = 2022

def locationsStandardIVF(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    queryset_list_us = queryset_list.filter(clinicState__iexact='United States')
    my_total_clinic_count_us = queryset_list_us.count()

    us_average_costs_model = AverageTreatmentCostUsa.objects.get(pk=1)

    us_ovarian_ivf_treatment_cost = us_average_costs_model.standard_ivf_val
    us_egg_donor_recipients_cost = us_average_costs_model.egg_ivf_val
    us_embryo_donor_recipients_cost = us_average_costs_model.embryo_ivf_val
    us_sperm_donor_recipients_cost = us_average_costs_model.sperm_ivf_val
    us_icsi_treatment_cost = us_average_costs_model.icsi_val
    us_iui_treatment_cost = us_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_uk = queryset_list.filter(clinicState__iexact='United Kingdom')
    my_total_clinic_count_uk = queryset_list_uk.count()

    uk_average_costs_model = AverageTreatmentCostUk.objects.get(pk=1)

    uk_ovarian_ivf_treatment_cost = uk_average_costs_model.standard_ivf_val
    uk_egg_donor_recipients_cost = uk_average_costs_model.egg_ivf_val
    uk_embryo_donor_recipients_cost = uk_average_costs_model.embryo_ivf_val
    uk_sperm_donor_recipients_cost = uk_average_costs_model.sperm_ivf_val
    uk_icsi_treatment_cost = uk_average_costs_model.icsi_val
    uk_iui_treatment_cost = uk_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_cz = queryset_list.filter(clinicState__iexact='Czech Republic')
    my_total_clinic_count_cz = queryset_list_cz.count()

    cz_average_costs_model = AverageTreatmentCostCzech.objects.get(pk=1)

    cz_ovarian_ivf_treatment_cost = cz_average_costs_model.standard_ivf_val
    cz_egg_donor_recipients_cost = cz_average_costs_model.egg_ivf_val
    cz_embryo_donor_recipients_cost = cz_average_costs_model.embryo_ivf_val
    cz_sperm_donor_recipients_cost = cz_average_costs_model.sperm_ivf_val
    cz_icsi_treatment_cost = cz_average_costs_model.icsi_val
    cz_iui_treatment_cost = cz_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_sk = queryset_list.filter(clinicState__iexact='Slovakia')
    my_total_clinic_count_sk = queryset_list_sk.count()

    sk_average_costs_model = AverageTreatmentCostSlovakia.objects.get(pk=1)

    sk_ovarian_ivf_treatment_cost = sk_average_costs_model.standard_ivf_val
    sk_egg_donor_recipients_cost = sk_average_costs_model.egg_ivf_val
    sk_embryo_donor_recipients_cost = sk_average_costs_model.embryo_ivf_val
    sk_sperm_donor_recipients_cost = sk_average_costs_model.sperm_ivf_val
    sk_icsi_treatment_cost = sk_average_costs_model.icsi_val
    sk_iui_treatment_cost = sk_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_dk = queryset_list.filter(clinicState__iexact='Denmark')
    my_total_clinic_count_dk = queryset_list_dk.count()

    dk_average_costs_model = AverageTreatmentCostDenmark.objects.get(pk=1)

    dk_ovarian_ivf_treatment_cost = dk_average_costs_model.standard_ivf_val
    dk_egg_donor_recipients_cost = dk_average_costs_model.egg_ivf_val
    dk_embryo_donor_recipients_cost = dk_average_costs_model.embryo_ivf_val
    dk_sperm_donor_recipients_cost = dk_average_costs_model.sperm_ivf_val
    dk_icsi_treatment_cost = dk_average_costs_model.icsi_val
    dk_iui_treatment_cost = dk_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_sp = queryset_list.filter(clinicState__iexact='Spain')
    my_total_clinic_count_sp = queryset_list_sp.count()

    sp_average_costs_model = AverageTreatmentCostSpain.objects.get(pk=1)

    sp_ovarian_ivf_treatment_cost = sp_average_costs_model.standard_ivf_val
    sp_egg_donor_recipients_cost = sp_average_costs_model.egg_ivf_val
    sp_embryo_donor_recipients_cost = sp_average_costs_model.embryo_ivf_val
    sp_sperm_donor_recipients_cost = sp_average_costs_model.sperm_ivf_val
    sp_icsi_treatment_cost = sp_average_costs_model.icsi_val
    sp_iui_treatment_cost = sp_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_in = queryset_list.filter(clinicState__iexact='India')
    my_total_clinic_count_in = queryset_list_in.count()

    in_average_costs_model = AverageTreatmentCostIndia.objects.get(pk=1)

    in_ovarian_ivf_treatment_cost = in_average_costs_model.standard_ivf_val
    in_egg_donor_recipients_cost = in_average_costs_model.egg_ivf_val
    in_embryo_donor_recipients_cost = in_average_costs_model.embryo_ivf_val
    in_sperm_donor_recipients_cost = in_average_costs_model.sperm_ivf_val
    in_icsi_treatment_cost = in_average_costs_model.icsi_val
    in_iui_treatment_cost = in_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_gr = queryset_list.filter(clinicState__iexact='Greece')
    my_total_clinic_count_gr = queryset_list_gr.count()

    gr_average_costs_model = AverageTreatmentCostGreece.objects.get(pk=1)

    gr_ovarian_ivf_treatment_cost = gr_average_costs_model.standard_ivf_val
    gr_egg_donor_recipients_cost = gr_average_costs_model.egg_ivf_val
    gr_embryo_donor_recipients_cost = gr_average_costs_model.embryo_ivf_val
    gr_sperm_donor_recipients_cost = gr_average_costs_model.sperm_ivf_val
    gr_icsi_treatment_cost = gr_average_costs_model.icsi_val
    gr_iui_treatment_cost = gr_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_cy = queryset_list.filter(clinicState__iexact='Cyprus')
    my_total_clinic_count_cy = queryset_list_cy.count()

    cy_average_costs_model = AverageTreatmentCostCyprus.objects.get(pk=1)

    cy_ovarian_ivf_treatment_cost = cy_average_costs_model.standard_ivf_val
    cy_egg_donor_recipients_cost = cy_average_costs_model.egg_ivf_val
    cy_embryo_donor_recipients_cost = cy_average_costs_model.embryo_ivf_val
    cy_sperm_donor_recipients_cost = cy_average_costs_model.sperm_ivf_val
    cy_icsi_treatment_cost = cy_average_costs_model.icsi_val
    cy_iui_treatment_cost = cy_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_de = queryset_list.filter(clinicState__iexact='Germany')
    my_total_clinic_count_de = queryset_list_de.count()

    de_average_costs_model = AverageTreatmentCostGermany.objects.get(pk=1)

    de_ovarian_ivf_treatment_cost = de_average_costs_model.standard_ivf_val
    de_egg_donor_recipients_cost = de_average_costs_model.egg_ivf_val
    de_embryo_donor_recipients_cost = de_average_costs_model.embryo_ivf_val
    de_sperm_donor_recipients_cost = de_average_costs_model.sperm_ivf_val
    de_icsi_treatment_cost = de_average_costs_model.icsi_val
    de_iui_treatment_cost = de_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_pt = queryset_list.filter(clinicState__iexact='Portugal')
    my_total_clinic_count_pt = queryset_list_pt.count()

    pt_average_costs_model = AverageTreatmentCostPortugal.objects.get(pk=1)

    pt_ovarian_ivf_treatment_cost = pt_average_costs_model.standard_ivf_val
    pt_egg_donor_recipients_cost = pt_average_costs_model.egg_ivf_val
    pt_embryo_donor_recipients_cost = pt_average_costs_model.embryo_ivf_val
    pt_sperm_donor_recipients_cost = pt_average_costs_model.sperm_ivf_val
    pt_icsi_treatment_cost = pt_average_costs_model.icsi_val
    pt_iui_treatment_cost = pt_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_lv = queryset_list.filter(clinicState__iexact='Latvia')
    my_total_clinic_count_lv = queryset_list_lv.count()

    lv_average_costs_model = AverageTreatmentCostLatvia.objects.get(pk=1)

    lv_ovarian_ivf_treatment_cost = lv_average_costs_model.standard_ivf_val
    lv_egg_donor_recipients_cost = lv_average_costs_model.egg_ivf_val
    lv_embryo_donor_recipients_cost = lv_average_costs_model.embryo_ivf_val
    lv_sperm_donor_recipients_cost = lv_average_costs_model.sperm_ivf_val
    lv_icsi_treatment_cost = lv_average_costs_model.icsi_val
    lv_iui_treatment_cost = lv_average_costs_model.iui_val

    # ---------------------------------------------------------------------------------
    queryset_list_mx = queryset_list.filter(clinicState__iexact='Mexico')
    my_total_clinic_count_mx = queryset_list_mx.count()

    mx_average_costs_model = AverageTreatmentCostMexico.objects.get(pk=1)

    mx_ovarian_ivf_treatment_cost = mx_average_costs_model.standard_ivf_val
    mx_egg_donor_recipients_cost = mx_average_costs_model.egg_ivf_val
    mx_embryo_donor_recipients_cost = mx_average_costs_model.embryo_ivf_val
    mx_sperm_donor_recipients_cost = mx_average_costs_model.sperm_ivf_val
    mx_icsi_treatment_cost = mx_average_costs_model.icsi_val
    mx_iui_treatment_cost = mx_average_costs_model.iui_val



    context = {
        'year': year,

        'my_total_clinic_count_us': my_total_clinic_count_us,

        'queryset_list_us_standard_ivf_val': us_ovarian_ivf_treatment_cost,
        'queryset_list_us_egg_ivf_val': us_egg_donor_recipients_cost,
        'queryset_list_us_embryo_ivf_val': us_embryo_donor_recipients_cost,
        'queryset_list_us_sperm_ivf_val': us_sperm_donor_recipients_cost,
        'queryset_list_us_icsi_val': us_icsi_treatment_cost,
        'queryset_list_us_iui_val': us_iui_treatment_cost,

        'my_total_clinic_count_uk': my_total_clinic_count_uk,
        'queryset_list_uk_standard_ivf_val': uk_ovarian_ivf_treatment_cost,
        'queryset_list_uk_egg_ivf_val': uk_egg_donor_recipients_cost,
        'queryset_list_uk_embryo_ivf_val': uk_embryo_donor_recipients_cost,
        'queryset_list_uk_sperm_ivf_val': uk_sperm_donor_recipients_cost,
        'queryset_list_uk_icsi_val': uk_icsi_treatment_cost,
        'queryset_list_uk_iui_val': uk_iui_treatment_cost,

        'my_total_clinic_count_cz': my_total_clinic_count_cz,
        'queryset_list_cz_standard_ivf_val': cz_ovarian_ivf_treatment_cost,
        'queryset_list_cz_egg_ivf_val': cz_egg_donor_recipients_cost,
        'queryset_list_cz_embryo_ivf_val': cz_embryo_donor_recipients_cost,
        'queryset_list_cz_sperm_ivf_val': cz_sperm_donor_recipients_cost,
        'queryset_list_cz_icsi_val': cz_icsi_treatment_cost,
        'queryset_list_cz_iui_val': cz_iui_treatment_cost,

        'my_total_clinic_count_sk': my_total_clinic_count_sk,
        'queryset_list_sk_standard_ivf_val': sk_ovarian_ivf_treatment_cost,
        'queryset_list_sk_egg_ivf_val': sk_egg_donor_recipients_cost,
        'queryset_list_sk_embryo_ivf_val': sk_embryo_donor_recipients_cost,
        'queryset_list_sk_sperm_ivf_val': sk_sperm_donor_recipients_cost,
        'queryset_list_sk_icsi_val': sk_icsi_treatment_cost,
        'queryset_list_sk_iui_val': sk_iui_treatment_cost,

        'my_total_clinic_count_dk': my_total_clinic_count_dk,
        'queryset_list_dk_standard_ivf_val': dk_ovarian_ivf_treatment_cost,
        'queryset_list_dk_egg_ivf_val': dk_egg_donor_recipients_cost,
        'queryset_list_dk_embryo_ivf_val': dk_embryo_donor_recipients_cost,
        'queryset_list_dk_sperm_ivf_val': dk_sperm_donor_recipients_cost,
        'queryset_list_dk_icsi_val': dk_icsi_treatment_cost,
        'queryset_list_dk_iui_val': dk_iui_treatment_cost,

        'my_total_clinic_count_sp': my_total_clinic_count_sp,
        'queryset_list_sp_standard_ivf_val': sp_ovarian_ivf_treatment_cost,
        'queryset_list_sp_egg_ivf_val': sp_egg_donor_recipients_cost,
        'queryset_list_sp_embryo_ivf_val': sp_embryo_donor_recipients_cost,
        'queryset_list_sp_sperm_ivf_val': sp_sperm_donor_recipients_cost,
        'queryset_list_sp_icsi_val': sp_icsi_treatment_cost,
        'queryset_list_sp_iui_val': sp_iui_treatment_cost,

        'my_total_clinic_count_in': my_total_clinic_count_in,
        'queryset_list_in_standard_ivf_val': in_ovarian_ivf_treatment_cost,
        'queryset_list_in_egg_ivf_val': in_egg_donor_recipients_cost,
        'queryset_list_in_embryo_ivf_val': in_embryo_donor_recipients_cost,
        'queryset_list_in_sperm_ivf_val': in_sperm_donor_recipients_cost,
        'queryset_list_in_icsi_val': in_icsi_treatment_cost,
        'queryset_list_in_iui_val': in_iui_treatment_cost,

        'my_total_clinic_count_gr': my_total_clinic_count_gr,
        'queryset_list_gr_standard_ivf_val': gr_ovarian_ivf_treatment_cost,
        'queryset_list_gr_egg_ivf_val': gr_egg_donor_recipients_cost,
        'queryset_list_gr_embryo_ivf_val': gr_embryo_donor_recipients_cost,
        'queryset_list_gr_sperm_ivf_val': gr_sperm_donor_recipients_cost,
        'queryset_list_gr_icsi_val': gr_icsi_treatment_cost,
        'queryset_list_gr_iui_val': gr_iui_treatment_cost,

        'my_total_clinic_count_cy': my_total_clinic_count_cy,
        'queryset_list_cy_standard_ivf_val': cy_ovarian_ivf_treatment_cost,
        'queryset_list_cy_egg_ivf_val': cy_egg_donor_recipients_cost,
        'queryset_list_cy_embryo_ivf_val': cy_embryo_donor_recipients_cost,
        'queryset_list_cy_sperm_ivf_val': cy_sperm_donor_recipients_cost,
        'queryset_list_cy_icsi_val': cy_icsi_treatment_cost,
        'queryset_list_cy_iui_val': cy_iui_treatment_cost,

        'my_total_clinic_count_de': my_total_clinic_count_de,
        'queryset_list_de_standard_ivf_val': de_ovarian_ivf_treatment_cost,
        'queryset_list_de_egg_ivf_val': de_egg_donor_recipients_cost,
        'queryset_list_de_embryo_ivf_val': de_embryo_donor_recipients_cost,
        'queryset_list_de_sperm_ivf_val': de_sperm_donor_recipients_cost,
        'queryset_list_de_icsi_val': de_icsi_treatment_cost,
        'queryset_list_de_iui_val': de_iui_treatment_cost,

        'my_total_clinic_count_pt': my_total_clinic_count_pt,
        'queryset_list_pt_standard_ivf_val': pt_ovarian_ivf_treatment_cost,
        'queryset_list_pt_egg_ivf_val': pt_egg_donor_recipients_cost,
        'queryset_list_pt_embryo_ivf_val': pt_embryo_donor_recipients_cost,
        'queryset_list_pt_sperm_ivf_val': pt_sperm_donor_recipients_cost,
        'queryset_list_pt_icsi_val': pt_icsi_treatment_cost,
        'queryset_list_pt_iui_val': pt_iui_treatment_cost,

        'my_total_clinic_count_lv': my_total_clinic_count_lv,
        'queryset_list_lv_standard_ivf_val': lv_ovarian_ivf_treatment_cost,
        'queryset_list_lv_egg_ivf_val': lv_egg_donor_recipients_cost,
        'queryset_list_lv_embryo_ivf_val': lv_embryo_donor_recipients_cost,
        'queryset_list_lv_sperm_ivf_val': lv_sperm_donor_recipients_cost,
        'queryset_list_lv_icsi_val': lv_icsi_treatment_cost,
        'queryset_list_lv_iui_val': lv_iui_treatment_cost,

        'my_total_clinic_count_mx': my_total_clinic_count_mx,
        'queryset_list_mx_standard_ivf_val': mx_ovarian_ivf_treatment_cost,
        'queryset_list_mx_egg_ivf_val': mx_egg_donor_recipients_cost,
        'queryset_list_mx_embryo_ivf_val': mx_embryo_donor_recipients_cost,
        'queryset_list_mx_sperm_ivf_val': mx_sperm_donor_recipients_cost,
        'queryset_list_mx_icsi_val': mx_icsi_treatment_cost,
        'queryset_list_mx_iui_val': mx_iui_treatment_cost,
        }

    return render(request, 'main/Locations/Main/locations-standard-ivf.html', context)


# --------------------------------------->>>>>>>> Redirects
def locationsIVFwithEggDonation(request):
    return HttpResponsePermanentRedirect(reverse('locations'))

def locationsIVFwithEmbryoDonation(request):
    return HttpResponsePermanentRedirect(reverse('locations'))

def locationsIUI(request):
    return HttpResponsePermanentRedirect(reverse('locations'))
