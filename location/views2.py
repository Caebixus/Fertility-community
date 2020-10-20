from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Avg, Max, Min



def locationsTexasRegions(request):
    queryset_list_texas = BasicClinic.objects.filter(clinicRegion__iexact='Texas')
    my_total_count_texas = queryset_list_texas.count()
    countIVFclinics = queryset_list_texas.filter(ovarian_ivf_treatment=True).count()
    countIUIclinics = queryset_list_texas.filter(iui_treatment=True).count()
    countEGGclinics = queryset_list_texas.filter(egg_donor_recipients=True).count()
    #---- ----- ---- ---- ---- ---- ---- ---- ----

    texasMinIVF = queryset_list_texas.aggregate(Min('ovarian_ivf_treatment_cost'))
    texasMaxIVF = queryset_list_texas.aggregate(Max('ovarian_ivf_treatment_cost'))
    texasIVF = queryset_list_texas.aggregate(average=Avg('ovarian_ivf_treatment_cost'))

    dallas = queryset_list_texas.filter(clinicCity__iexact='Dallas')
    dallasIVFCount = dallas.filter(ovarian_ivf_treatment=True).count()
    dallasIVF = BasicClinic.objects.filter(clinicCity__iexact='Dallas').aggregate(average=Avg('ovarian_ivf_treatment_cost'))

    houston = queryset_list_texas.filter(clinicCity__iexact='Houston')
    houstonIVFCount = houston.filter(ovarian_ivf_treatment=True).count()
    houstonIVF = BasicClinic.objects.filter(clinicCity__iexact='Houston').aggregate(average=Avg('ovarian_ivf_treatment_cost'))

    austin = queryset_list_texas.filter(clinicCity__iexact='Austin')
    austinIVFCount = austin.filter(ovarian_ivf_treatment=True).count()
    austinIVF = BasicClinic.objects.filter(clinicCity__iexact='Austin').aggregate(average=Avg('ovarian_ivf_treatment_cost'))

    sanantonio = queryset_list_texas.filter(clinicCity__iexact='San Antonio')
    sanantonioIVFCount = sanantonio.filter(ovarian_ivf_treatment=True).count()
    sanantonioIVF = BasicClinic.objects.filter(clinicCity__iexact='San Antonio').aggregate(average=Avg('ovarian_ivf_treatment_cost'))

    #---- ----- ---- ---- ---- ---- ---- ---- ----
    texasMinIUI = queryset_list_texas.aggregate(Min('iui_treatment_cost'))
    texasMaxIUI = queryset_list_texas.aggregate(Max('iui_treatment_cost'))
    texasIUI = queryset_list_texas.aggregate(average=Avg('iui_treatment_cost'))

    dallasIUICount = dallas.filter(iui_treatment=True).count()
    dallasIUI = BasicClinic.objects.filter(clinicCity__iexact='Dallas').aggregate(average=Avg('iui_treatment_cost'))

    houstonIUICount = houston.filter(iui_treatment=True).count()
    houstonIUI = BasicClinic.objects.filter(clinicCity__iexact='Houston').aggregate(average=Avg('iui_treatment_cost'))

    austinIUICount = austin.filter(iui_treatment=True).count()
    austinIUI = BasicClinic.objects.filter(clinicCity__iexact='Austin').aggregate(average=Avg('iui_treatment_cost'))

    sanantonioIUICount = sanantonio.filter(iui_treatment=True).count()
    sanantonioIUI = BasicClinic.objects.filter(clinicCity__iexact='San Antonio').aggregate(average=Avg('iui_treatment_cost'))

    #---- ----- ---- ---- ---- ---- ---- ---- ----
    texasMinEGG = queryset_list_texas.aggregate(Min('egg_donor_recipients_cost'))
    texasMaxEGG = queryset_list_texas.aggregate(Max('egg_donor_recipients_cost'))
    texasEGG = queryset_list_texas.aggregate(average=Avg('egg_donor_recipients_cost'))

    dallasEGGCount = dallas.filter(egg_donor_recipients=True).count()
    dallasEGG = BasicClinic.objects.filter(clinicCity__iexact='Dallas').aggregate(average=Avg('egg_donor_recipients_cost'))

    houstonEGGCount = houston.filter(egg_donor_recipients=True).count()
    houstonEGG = BasicClinic.objects.filter(clinicCity__iexact='Houston').aggregate(average=Avg('egg_donor_recipients_cost'))

    austinEGGCount = austin.filter(egg_donor_recipients=True).count()
    austinEGG = BasicClinic.objects.filter(clinicCity__iexact='Austin').aggregate(average=Avg('egg_donor_recipients_cost'))

    sanantonioEGGCount = sanantonio.filter(egg_donor_recipients=True).count()
    sanantonioEGG = BasicClinic.objects.filter(clinicCity__iexact='San Antonio').aggregate(average=Avg('egg_donor_recipients_cost'))


    context = {
        'queryset_list_texas': queryset_list_texas,
        'my_total_count_texas': my_total_count_texas,
        'countIVFclinics': countIVFclinics,
        'countIUIclinics': countIUIclinics,
        'countEGGclinics': countEGGclinics,

        'texasMinIVF': texasMinIVF,
        'texasMaxIVF': texasMaxIVF,
        'texasIVF': texasIVF,
        'texasMinIUI': texasMinIUI,
        'texasMaxIUI': texasMaxIUI,
        'texasIUI': texasIUI,
        'texasMinEGG': texasMinEGG,
        'texasMaxEGG': texasMaxEGG,
        'texasEGG': texasEGG,

        'dallas': dallas,
        'dallasIVFCount': dallasIVFCount,
        'dallasIVF': dallasIVF,
        'dallasIUICount': dallasIUICount,
        'dallasIUI': dallasIUI,
        'dallasEGGCount': dallasEGGCount,
        'dallasEGG': dallasEGG,

        'houston': houston,
        'houstonIVFCount': houstonIVFCount,
        'houstonIVF': houstonIVF,
        'houstonIUICount': houstonIUICount,
        'houstonIUI': houstonIUI,
        'houstonEGGCount': houstonEGGCount,
        'houstonEGG': houstonEGG,

        'austin': austin,
        'austinIVFCount': austinIVFCount,
        'austinIVF': austinIVF,
        'austinIUICount': austinIUICount,
        'austinIUI': austinIUI,
        'austinEGGCount': austinEGGCount,
        'austinEGG': austinEGG,

        'sanantonio': sanantonio,
        'sanantonioIVFCount': sanantonioIVFCount,
        'sanantonioIVF': sanantonioIVF,
        'sanantonioIUICount': sanantonioIUICount,
        'sanantonioIUI': sanantonioIUI,
        'sanantonioEGGCount': sanantonioEGGCount,
        'sanantonioEGG': sanantonioEGG,
    }
    return render(request, 'main/Locations/USLocations/Regions/ivf-cost-texas.html', context)
