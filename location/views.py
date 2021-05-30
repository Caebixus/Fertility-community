from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from itertools import chain
from .currencies import gbpToEur, gbpToUsd, gbpToInr, usdToGbp, usdToEur, usdToInr, eurToGbp, eurToUsd, eurToInr, inrToGbp, inrToEur, inrToUsd, mxnToGbp, mxnToEur, mxnToUsd
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def locationsStandardIVF(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    queryset_list_us = queryset_list.filter(clinicState__iexact='United States')
    my_total_clinic_count_us = queryset_list_us.count()

    queryset_list_us_ivf = queryset_list_us.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_us_ivf.items():
        queryset_list_us_ivf_val = val

    queryset_list_us_egg = queryset_list_us.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_us_egg.items():
        queryset_list_us_egg_val = val

    queryset_list_us_embryo = queryset_list_us.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_us_embryo.items():
        queryset_list_us_embryo_val = val

    queryset_list_us_sperm = queryset_list_us.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_us_sperm.items():
        queryset_list_us_sperm_val = val

    queryset_list_us_icsi = queryset_list_us.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_us_icsi.items():
        queryset_list_us_icsi_val = val

    queryset_list_us_iui = queryset_list_us.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_us_iui.items():
        queryset_list_us_iui_val = val

#-------------------------------------------------------------------------------

    queryset_list_uk = queryset_list.filter(clinicState__iexact='United Kingdom')
    my_total_clinic_count_uk = queryset_list_uk.count()
    queryset_list_uk_ivf = queryset_list_uk.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_uk_ivf.items():
        queryset_list_uk_ivf_val = val

    queryset_list_uk_egg = queryset_list_uk.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_uk_egg.items():
        queryset_list_uk_egg_val = val

    queryset_list_uk_embryo = queryset_list_uk.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_uk_embryo.items():
        queryset_list_uk_embryo_val = val

    queryset_list_uk_sperm = queryset_list_uk.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_uk_sperm.items():
        queryset_list_uk_sperm_val = val

    queryset_list_uk_icsi = queryset_list_uk.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_uk_icsi.items():
        queryset_list_uk_icsi_val = val

    queryset_list_uk_iui = queryset_list_uk.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_uk_iui.items():
        queryset_list_uk_iui_val = val

#-------------------------------------------------------------------------------

    queryset_list_cz = queryset_list.filter(clinicState__iexact='Czech Republic')
    my_total_clinic_count_cz = queryset_list_cz.count()
    queryset_list_cz_ivf = queryset_list_cz.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_cz_ivf.items():
        queryset_list_cz_ivf_val = val

    queryset_list_cz_egg = queryset_list_cz.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_cz_egg.items():
        queryset_list_cz_egg_val = val

    queryset_list_cz_embryo = queryset_list_cz.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_cz_embryo.items():
        queryset_list_cz_embryo_val = val

    queryset_list_cz_sperm = queryset_list_cz.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_cz_sperm.items():
        queryset_list_cz_sperm_val = val

    queryset_list_cz_icsi = queryset_list_cz.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_cz_icsi.items():
        queryset_list_cz_icsi_val = val

    queryset_list_cz_iui = queryset_list_cz.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_cz_iui.items():
        queryset_list_cz_iui_val = val

#-------------------------------------------------------------------------------

    queryset_list_sp = queryset_list.filter(clinicState__iexact='Spain')
    my_total_clinic_count_sp = queryset_list_sp.count()
    queryset_list_sp_ivf = queryset_list_sp.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_sp_ivf.items():
        queryset_list_sp_ivf_val = val

    queryset_list_sp_egg = queryset_list_sp.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_sp_egg.items():
        queryset_list_sp_egg_val = val

    queryset_list_sp_embryo = queryset_list_sp.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_sp_embryo.items():
        queryset_list_sp_embryo_val = val

    queryset_list_sp_sperm = queryset_list_sp.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_sp_sperm.items():
        queryset_list_sp_sperm_val = val

    queryset_list_sp_icsi = queryset_list_sp.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_sp_icsi.items():
        queryset_list_sp_icsi_val = val

    queryset_list_sp_iui = queryset_list_sp.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_sp_iui.items():
        queryset_list_sp_iui_val = val

#-------------------------------------------------------------------------------

    queryset_list_in = queryset_list.filter(clinicState__iexact='India')
    my_total_clinic_count_in = queryset_list_in.count()
    queryset_list_in_ivf = queryset_list_in.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_in_ivf.items():
        queryset_list_in_ivf_val = val

    queryset_list_in_egg = queryset_list_in.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_in_egg.items():
        queryset_list_in_egg_val = val

    queryset_list_in_embryo = queryset_list_in.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_in_embryo.items():
        queryset_list_in_embryo_val = val

    queryset_list_in_sperm = queryset_list_in.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_in_sperm.items():
        queryset_list_in_sperm_val = val

    queryset_list_in_icsi = queryset_list_in.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_in_icsi.items():
        queryset_list_in_icsi_val = val

    queryset_list_in_iui = queryset_list_in.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_in_iui.items():
        queryset_list_in_iui_val = val

#-------------------------------------------------------------------------------

    queryset_list_gr = queryset_list.filter(clinicState__iexact='Greece')
    my_total_clinic_count_gr = queryset_list_gr.count()
    queryset_list_gr_ivf = queryset_list_gr.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_gr_ivf.items():
        queryset_list_gr_ivf_val = val

    queryset_list_gr_egg = queryset_list_gr.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_gr_egg.items():
        queryset_list_gr_egg_val = val

    queryset_list_gr_embryo = queryset_list_gr.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_gr_embryo.items():
        queryset_list_gr_embryo_val = val

    queryset_list_gr_sperm = queryset_list_gr.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_gr_sperm.items():
        queryset_list_gr_sperm_val = val

    queryset_list_gr_icsi = queryset_list_gr.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_gr_icsi.items():
        queryset_list_gr_icsi_val = val

    queryset_list_gr_iui = queryset_list_gr.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_gr_iui.items():
        queryset_list_gr_iui_val = val

#-------------------------------------------------------------------------------

    queryset_list_cy = queryset_list.filter(clinicState__iexact='Cyprus')
    my_total_clinic_count_cy = queryset_list_cy.count()
    queryset_list_cy_ivf = queryset_list_cy.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_cy_ivf.items():
        queryset_list_cy_ivf_val = val

    queryset_list_cy_egg = queryset_list_cy.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_cy_egg.items():
        queryset_list_cy_egg_val = val

    queryset_list_cy_embryo = queryset_list_cy.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_cy_embryo.items():
        queryset_list_cy_embryo_val = val

    queryset_list_cy_sperm = queryset_list_cy.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_cy_sperm.items():
        queryset_list_cy_sperm_val = val

    queryset_list_cy_icsi = queryset_list_cy.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_cy_icsi.items():
        queryset_list_cy_icsi_val = val

    queryset_list_cy_iui = queryset_list_cy.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_cy_iui.items():
        queryset_list_cy_iui_val = val

#-------------------------------------------------------------------------------

    queryset_list_mx = queryset_list.filter(clinicState__iexact='Mexico')
    my_total_clinic_count_mx = queryset_list_mx.count()
    queryset_list_mx_ivf = queryset_list_mx.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    for key,val in queryset_list_mx_ivf.items():
        queryset_list_mx_ivf_val = val

    queryset_list_mx_egg = queryset_list_mx.aggregate(average=Avg('egg_donor_recipients_cost'))
    for key,val in queryset_list_mx_egg.items():
        queryset_list_mx_egg_val = val

    queryset_list_mx_embryo = queryset_list_mx.aggregate(average=Avg('embryo_donor_recipients_cost'))
    for key,val in queryset_list_mx_embryo.items():
        queryset_list_mx_embryo_val = val

    queryset_list_mx_sperm = queryset_list_mx.aggregate(average=Avg('sperm_donor_recipients_cost'))
    for key,val in queryset_list_mx_sperm.items():
        queryset_list_mx_sperm_val = val

    queryset_list_mx_icsi = queryset_list_mx.aggregate(average=Avg('icsi_treatment_cost'))
    for key,val in queryset_list_mx_icsi.items():
        queryset_list_mx_icsi_val = val

    queryset_list_mx_iui = queryset_list_mx.aggregate(average=Avg('iui_treatment_cost'))
    for key,val in queryset_list_mx_iui.items():
        queryset_list_mx_iui_val = val

    context = {
        'my_total_clinic_count_us': my_total_clinic_count_us,
        'queryset_list_us_ivf_val': queryset_list_us_ivf_val,
        'queryset_list_us_egg_val': queryset_list_us_egg_val,
        'queryset_list_us_embryo_val': queryset_list_us_embryo_val,
        'queryset_list_us_sperm_val': queryset_list_us_sperm_val,
        'queryset_list_us_icsi_val': queryset_list_us_icsi_val,
        'queryset_list_us_iui_val': queryset_list_us_iui_val,

        'my_total_clinic_count_uk': my_total_clinic_count_uk,
        'queryset_list_uk_ivf_val': queryset_list_uk_ivf_val,
        'queryset_list_uk_egg_val': queryset_list_uk_egg_val,
        'queryset_list_uk_embryo_val': queryset_list_uk_embryo_val,
        'queryset_list_uk_sperm_val': queryset_list_uk_sperm_val,
        'queryset_list_uk_icsi_val': queryset_list_uk_icsi_val,
        'queryset_list_uk_iui_val': queryset_list_uk_iui_val,

        'my_total_clinic_count_cz': my_total_clinic_count_cz,
        'queryset_list_cz_ivf_val': queryset_list_cz_ivf_val,
        'queryset_list_cz_egg_val': queryset_list_cz_egg_val,
        'queryset_list_cz_embryo_val': queryset_list_cz_embryo_val,
        'queryset_list_cz_sperm_val': queryset_list_cz_sperm_val,
        'queryset_list_cz_icsi_val': queryset_list_cz_icsi_val,
        'queryset_list_cz_iui_val': queryset_list_cz_iui_val,

        'my_total_clinic_count_sp': my_total_clinic_count_sp,
        'queryset_list_sp_ivf_val': queryset_list_sp_ivf_val,
        'queryset_list_sp_egg_val': queryset_list_sp_egg_val,
        'queryset_list_sp_embryo_val': queryset_list_sp_embryo_val,
        'queryset_list_sp_sperm_val': queryset_list_sp_sperm_val,
        'queryset_list_sp_icsi_val': queryset_list_sp_icsi_val,
        'queryset_list_sp_iui_val': queryset_list_sp_iui_val,

        'my_total_clinic_count_in': my_total_clinic_count_in,
        'queryset_list_in_ivf_val': queryset_list_in_ivf_val,
        'queryset_list_in_egg_val': queryset_list_in_egg_val,
        'queryset_list_in_embryo_val': queryset_list_in_embryo_val,
        'queryset_list_in_sperm_val': queryset_list_in_sperm_val,
        'queryset_list_in_icsi_val': queryset_list_in_icsi_val,
        'queryset_list_in_iui_val': queryset_list_in_iui_val,

        'my_total_clinic_count_gr': my_total_clinic_count_gr,
        'queryset_list_gr_ivf_val': queryset_list_gr_ivf_val,
        'queryset_list_gr_egg_val': queryset_list_gr_egg_val,
        'queryset_list_gr_embryo_val': queryset_list_gr_embryo_val,
        'queryset_list_gr_sperm_val': queryset_list_gr_sperm_val,
        'queryset_list_gr_icsi_val': queryset_list_gr_icsi_val,
        'queryset_list_gr_iui_val': queryset_list_gr_iui_val,

        'my_total_clinic_count_cy': my_total_clinic_count_cy,
        'queryset_list_cy_ivf_val': queryset_list_cy_ivf_val,
        'queryset_list_cy_egg_val': queryset_list_cy_egg_val,
        'queryset_list_cy_embryo_val': queryset_list_cy_embryo_val,
        'queryset_list_cy_sperm_val': queryset_list_cy_sperm_val,
        'queryset_list_cy_icsi_val': queryset_list_cy_icsi_val,
        'queryset_list_cy_iui_val': queryset_list_cy_iui_val,

        'my_total_clinic_count_mx': my_total_clinic_count_mx,
        'queryset_list_mx_ivf_val': queryset_list_mx_ivf_val,
        'queryset_list_mx_egg_val': queryset_list_mx_egg_val,
        'queryset_list_mx_embryo_val': queryset_list_mx_embryo_val,
        'queryset_list_mx_sperm_val': queryset_list_mx_sperm_val,
        'queryset_list_mx_icsi_val': queryset_list_mx_icsi_val,
        'queryset_list_mx_iui_val': queryset_list_mx_iui_val,
        }

    return render(request, 'main/Locations/locations-standard-ivf.html', context)


# --------------------------------------->>>>>>>> Redirects
def locationsIVFwithEggDonation(request):
    return HttpResponsePermanentRedirect(reverse('locationsStandardIVF'))

def locationsIVFwithEmbryoDonation(request):
    return HttpResponsePermanentRedirect(reverse('locationsStandardIVF'))

def locationsIUI(request):
    return HttpResponsePermanentRedirect(reverse('locationsStandardIVF'))
