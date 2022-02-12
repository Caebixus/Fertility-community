from django.shortcuts import render
from clinic.models import BasicClinic
from .functions import country_count, region_count, procedure_country_average_value, procedure_region_average_value
from base.constant_variables import year
from location.models.country_models import *
from location.models.europe_city_models import *


def locationsUKRegions(request):
    queryset_list = BasicClinic.objects.all().exclude(is_published=False)

    pkid = 3
    best_clinics = queryset_list.filter(best_article_country_blogpost_obj=pkid).exclude(best_article_country_actual_text__isnull=True).exclude(best_article_country_actual_text__exact='')
    best_clinics_count = best_clinics.count()

    country_name = 'United Kingdom'
    my_total_clinic_count = country_count(country_name)
    clinic_count = my_total_clinic_count

    uk_average_costs_model = AverageTreatmentCostUk.objects.get(pk=1)

    queryset_list_uk_natural_ivf_val = uk_average_costs_model.natural_ivf_val
    queryset_list_uk_mild_ivf_val = uk_average_costs_model.mild_ivf_val
    queryset_list_uk_standard_ivf_val = uk_average_costs_model.standard_ivf_val
    queryset_list_uk_egg_ivf_val = uk_average_costs_model.egg_ivf_val
    queryset_list_uk_known_egg_ivf_val = uk_average_costs_model.known_egg_ivf_val
    queryset_list_uk_shared_egg_ivf_val = uk_average_costs_model.shared_egg_ivf_val
    queryset_list_uk_embryo_ivf_val = uk_average_costs_model.embryo_ivf_val
    queryset_list_uk_known_embryo_ivf_val = uk_average_costs_model.known_embryo_ivf_val
    queryset_list_uk_sperm_ivf_val = uk_average_costs_model.sperm_ivf_val
    queryset_list_uk_known_sperm_ivf_val = uk_average_costs_model.known_sperm_ivf_val
    queryset_list_uk_icsi_val = uk_average_costs_model.icsi_val
    queryset_list_uk_iui_val = uk_average_costs_model.iui_val

    queryset_list_uk = BasicClinic.objects.all().exclude(is_published=False).filter(clinicState__iexact='United Kingdom')

    queryset_list_aberdeen = queryset_list_uk.filter(clinicRegion__iexact='Aberdeen')
    my_total_clinic_count_aberdeen = queryset_list_aberdeen.count()
    aberdeen_average_costs_model = Aberdeen.objects.get(pk=1)
    queryset_list_aberdeen_ivf_val = aberdeen_average_costs_model.standard_ivf_val
    queryset_list_aberdeen_egg_val = aberdeen_average_costs_model.egg_ivf_val
    queryset_list_aberdeen_embryo_val = aberdeen_average_costs_model.embryo_ivf_val
    queryset_list_aberdeen_sperm_val = aberdeen_average_costs_model.sperm_ivf_val
    queryset_list_aberdeen_icsi_val = aberdeen_average_costs_model.icsi_val
    queryset_list_aberdeen_iui_val = aberdeen_average_costs_model.iui_val

    queryset_list_bath = queryset_list_uk.filter(clinicRegion__iexact='Bath')
    my_total_clinic_count_bath = queryset_list_bath.count()
    bath_average_costs_model = Bath.objects.get(pk=1)
    queryset_list_bath_ivf_val = bath_average_costs_model.standard_ivf_val
    queryset_list_bath_egg_val = bath_average_costs_model.egg_ivf_val
    queryset_list_bath_embryo_val = bath_average_costs_model.embryo_ivf_val
    queryset_list_bath_sperm_val = bath_average_costs_model.sperm_ivf_val
    queryset_list_bath_icsi_val = bath_average_costs_model.icsi_val
    queryset_list_bath_iui_val = bath_average_costs_model.iui_val

    queryset_list_belfast = queryset_list_uk.filter(clinicRegion__iexact='Belfast')
    my_total_clinic_count_belfast = queryset_list_belfast.count()
    belfast_average_costs_model = Belfast.objects.get(pk=1)
    queryset_list_belfast_ivf_val = belfast_average_costs_model.standard_ivf_val
    queryset_list_belfast_egg_val = belfast_average_costs_model.egg_ivf_val
    queryset_list_belfast_embryo_val = belfast_average_costs_model.embryo_ivf_val
    queryset_list_belfast_sperm_val = belfast_average_costs_model.sperm_ivf_val
    queryset_list_belfast_icsi_val = belfast_average_costs_model.icsi_val
    queryset_list_belfast_iui_val = belfast_average_costs_model.iui_val

    queryset_list_birmingham = queryset_list_uk.filter(clinicRegion__iexact='Birmingham')
    my_total_clinic_count_birmingham = queryset_list_birmingham.count()
    birmingham_average_costs_model = Birmingham.objects.get(pk=1)
    queryset_list_birmingham_ivf_val = birmingham_average_costs_model.standard_ivf_val
    queryset_list_birmingham_egg_val = birmingham_average_costs_model.egg_ivf_val
    queryset_list_birmingham_embryo_val = birmingham_average_costs_model.embryo_ivf_val
    queryset_list_birmingham_sperm_val = birmingham_average_costs_model.sperm_ivf_val
    queryset_list_birmingham_icsi_val = birmingham_average_costs_model.icsi_val
    queryset_list_birmingham_iui_val = birmingham_average_costs_model.iui_val

    queryset_list_bournemouth = queryset_list_uk.filter(clinicRegion__iexact='Bournemouth')
    my_total_clinic_count_bournemouth = queryset_list_bournemouth.count()
    bournemouth_average_costs_model = Bournemouth.objects.get(pk=1)
    queryset_list_bournemouth_ivf_val = bournemouth_average_costs_model.standard_ivf_val
    queryset_list_bournemouth_egg_val = bournemouth_average_costs_model.egg_ivf_val
    queryset_list_bournemouth_embryo_val = bournemouth_average_costs_model.embryo_ivf_val
    queryset_list_bournemouth_sperm_val = bournemouth_average_costs_model.sperm_ivf_val
    queryset_list_bournemouth_icsi_val = bournemouth_average_costs_model.icsi_val
    queryset_list_bournemouth_iui_val = bournemouth_average_costs_model.iui_val

    queryset_list_brighton = queryset_list_uk.filter(clinicRegion__iexact='Brighton')
    my_total_clinic_count_brighton = queryset_list_brighton.count()
    brighton_average_costs_model = Brighton.objects.get(pk=1)
    queryset_list_brighton_ivf_val = brighton_average_costs_model.standard_ivf_val
    queryset_list_brighton_egg_val = brighton_average_costs_model.egg_ivf_val
    queryset_list_brighton_embryo_val = brighton_average_costs_model.embryo_ivf_val
    queryset_list_brighton_sperm_val = brighton_average_costs_model.sperm_ivf_val
    queryset_list_brighton_icsi_val = brighton_average_costs_model.icsi_val
    queryset_list_brighton_iui_val = brighton_average_costs_model.iui_val

    queryset_list_bristol = queryset_list_uk.filter(clinicRegion__iexact='Bristol')
    my_total_clinic_count_bristol = queryset_list_bristol.count()
    bristol_average_costs_model = Bristol.objects.get(pk=1)
    queryset_list_bristol_ivf_val = bristol_average_costs_model.standard_ivf_val
    queryset_list_bristol_egg_val = bristol_average_costs_model.egg_ivf_val
    queryset_list_bristol_embryo_val = bristol_average_costs_model.embryo_ivf_val
    queryset_list_bristol_sperm_val = bristol_average_costs_model.sperm_ivf_val
    queryset_list_bristol_icsi_val = bristol_average_costs_model.icsi_val
    queryset_list_bristol_iui_val = bristol_average_costs_model.iui_val

    queryset_list_cambridge = queryset_list_uk.filter(clinicRegion__iexact='Cambridge')
    my_total_clinic_count_cambridge = queryset_list_cambridge.count()
    cambridge_average_costs_model = Cambridge.objects.get(pk=1)
    queryset_list_cambridge_ivf_val = cambridge_average_costs_model.standard_ivf_val
    queryset_list_cambridge_egg_val = cambridge_average_costs_model.egg_ivf_val
    queryset_list_cambridge_embryo_val = cambridge_average_costs_model.embryo_ivf_val
    queryset_list_cambridge_sperm_val = cambridge_average_costs_model.sperm_ivf_val
    queryset_list_cambridge_icsi_val = cambridge_average_costs_model.icsi_val
    queryset_list_cambridge_iui_val = cambridge_average_costs_model.iui_val

    queryset_list_cardiff = queryset_list_uk.filter(clinicRegion__iexact='Cardiff')
    my_total_clinic_count_cardiff = queryset_list_cardiff.count()
    cardiff_average_costs_model = Cardiff.objects.get(pk=1)
    queryset_list_cardiff_ivf_val = cardiff_average_costs_model.standard_ivf_val
    queryset_list_cardiff_egg_val = cardiff_average_costs_model.egg_ivf_val
    queryset_list_cardiff_embryo_val = cardiff_average_costs_model.embryo_ivf_val
    queryset_list_cardiff_sperm_val = cardiff_average_costs_model.sperm_ivf_val
    queryset_list_cardiff_icsi_val = cardiff_average_costs_model.icsi_val
    queryset_list_cardiff_iui_val = cardiff_average_costs_model.iui_val

    queryset_list_colchester = queryset_list_uk.filter(clinicRegion__iexact='Colchester')
    my_total_clinic_count_colchester = queryset_list_colchester.count()
    colchester_average_costs_model = Colchester.objects.get(pk=1)
    queryset_list_colchester_ivf_val = colchester_average_costs_model.standard_ivf_val
    queryset_list_colchester_egg_val = colchester_average_costs_model.egg_ivf_val
    queryset_list_colchester_embryo_val = colchester_average_costs_model.embryo_ivf_val
    queryset_list_colchester_sperm_val = colchester_average_costs_model.sperm_ivf_val
    queryset_list_colchester_icsi_val = colchester_average_costs_model.icsi_val
    queryset_list_colchester_iui_val = colchester_average_costs_model.iui_val

    queryset_list_derby = queryset_list_uk.filter(clinicRegion__iexact='Derby')
    my_total_clinic_count_derby = queryset_list_derby.count()
    derby_average_costs_model = Derby.objects.get(pk=1)
    queryset_list_derby_ivf_val = derby_average_costs_model.standard_ivf_val
    queryset_list_derby_egg_val = derby_average_costs_model.egg_ivf_val
    queryset_list_derby_embryo_val = derby_average_costs_model.embryo_ivf_val
    queryset_list_derby_sperm_val = derby_average_costs_model.sperm_ivf_val
    queryset_list_derby_icsi_val = derby_average_costs_model.icsi_val
    queryset_list_derby_iui_val = derby_average_costs_model.iui_val

    queryset_list_exeter = queryset_list_uk.filter(clinicRegion__iexact='Exeter')
    my_total_clinic_count_exeter = queryset_list_exeter.count()
    exeter_average_costs_model = Exeter.objects.get(pk=1)
    queryset_list_exeter_ivf_val = exeter_average_costs_model.standard_ivf_val
    queryset_list_exeter_egg_val = exeter_average_costs_model.egg_ivf_val
    queryset_list_exeter_embryo_val = exeter_average_costs_model.embryo_ivf_val
    queryset_list_exeter_sperm_val = exeter_average_costs_model.sperm_ivf_val
    queryset_list_exeter_icsi_val = exeter_average_costs_model.icsi_val
    queryset_list_exeter_iui_val = exeter_average_costs_model.iui_val

    queryset_list_glasgow = queryset_list_uk.filter(clinicRegion__iexact='Glasgow')
    my_total_clinic_count_glasgow = queryset_list_glasgow.count()
    glasgow_average_costs_model = Glasgow.objects.get(pk=1)
    queryset_list_glasgow_ivf_val = glasgow_average_costs_model.standard_ivf_val
    queryset_list_glasgow_egg_val = glasgow_average_costs_model.egg_ivf_val
    queryset_list_glasgow_embryo_val = glasgow_average_costs_model.embryo_ivf_val
    queryset_list_glasgow_sperm_val = glasgow_average_costs_model.sperm_ivf_val
    queryset_list_glasgow_icsi_val = glasgow_average_costs_model.icsi_val
    queryset_list_glasgow_iui_val = glasgow_average_costs_model.iui_val

    queryset_list_hull = queryset_list_uk.filter(clinicRegion__iexact='Hull')
    my_total_clinic_count_hull = queryset_list_hull.count()
    hull_average_costs_model = Hull.objects.get(pk=1)
    queryset_list_hull_ivf_val = hull_average_costs_model.standard_ivf_val
    queryset_list_hull_egg_val = hull_average_costs_model.egg_ivf_val
    queryset_list_hull_embryo_val = hull_average_costs_model.embryo_ivf_val
    queryset_list_hull_sperm_val = hull_average_costs_model.sperm_ivf_val
    queryset_list_hull_icsi_val = hull_average_costs_model.icsi_val
    queryset_list_hull_iui_val = hull_average_costs_model.iui_val

    queryset_list_chelmsford = queryset_list_uk.filter(clinicRegion__iexact='Chelmsford')
    my_total_clinic_count_chelmsford = queryset_list_chelmsford.count()
    chelmsford_average_costs_model = Chelmsford.objects.get(pk=1)
    queryset_list_chelmsford_ivf_val = chelmsford_average_costs_model.standard_ivf_val
    queryset_list_chelmsford_egg_val = chelmsford_average_costs_model.egg_ivf_val
    queryset_list_chelmsford_embryo_val = chelmsford_average_costs_model.embryo_ivf_val
    queryset_list_chelmsford_sperm_val = chelmsford_average_costs_model.sperm_ivf_val
    queryset_list_chelmsford_icsi_val = chelmsford_average_costs_model.icsi_val
    queryset_list_chelmsford_iui_val = chelmsford_average_costs_model.iui_val

    queryset_list_leeds = queryset_list_uk.filter(clinicRegion__iexact='Leeds')
    my_total_clinic_count_leeds = queryset_list_leeds.count()
    leeds_average_costs_model = Leeds.objects.get(pk=1)
    queryset_list_leeds_ivf_val = leeds_average_costs_model.standard_ivf_val
    queryset_list_leeds_egg_val = leeds_average_costs_model.egg_ivf_val
    queryset_list_leeds_embryo_val = leeds_average_costs_model.embryo_ivf_val
    queryset_list_leeds_sperm_val = leeds_average_costs_model.sperm_ivf_val
    queryset_list_leeds_icsi_val = leeds_average_costs_model.icsi_val
    queryset_list_leeds_iui_val = leeds_average_costs_model.iui_val

    queryset_list_leicester = queryset_list_uk.filter(clinicRegion__iexact='Leicester')
    my_total_clinic_count_leicester = queryset_list_leicester.count()
    leicester_average_costs_model = Leicester.objects.get(pk=1)
    queryset_list_leicester_ivf_val = leicester_average_costs_model.standard_ivf_val
    queryset_list_leicester_egg_val = leicester_average_costs_model.egg_ivf_val
    queryset_list_leicester_embryo_val = leicester_average_costs_model.embryo_ivf_val
    queryset_list_leicester_sperm_val = leicester_average_costs_model.sperm_ivf_val
    queryset_list_leicester_icsi_val = leicester_average_costs_model.icsi_val
    queryset_list_leicester_iui_val = leicester_average_costs_model.iui_val

    queryset_list_liverpool = queryset_list_uk.filter(clinicRegion__iexact='Liverpool')
    my_total_clinic_count_liverpool = queryset_list_liverpool.count()
    liverpool_average_costs_model = Liverpool.objects.get(pk=1)
    queryset_list_liverpool_ivf_val = liverpool_average_costs_model.standard_ivf_val
    queryset_list_liverpool_egg_val = liverpool_average_costs_model.egg_ivf_val
    queryset_list_liverpool_embryo_val = liverpool_average_costs_model.embryo_ivf_val
    queryset_list_liverpool_sperm_val = liverpool_average_costs_model.sperm_ivf_val
    queryset_list_liverpool_icsi_val = liverpool_average_costs_model.icsi_val
    queryset_list_liverpool_iui_val = liverpool_average_costs_model.iui_val

    queryset_list_london = queryset_list_uk.filter(clinicRegion__iexact='London')
    my_total_clinic_count_london = queryset_list_london.count()
    london_average_costs_model = London.objects.get(pk=1)
    queryset_list_london_ivf_val = london_average_costs_model.standard_ivf_val
    queryset_list_london_egg_val = london_average_costs_model.egg_ivf_val
    queryset_list_london_embryo_val = london_average_costs_model.embryo_ivf_val
    queryset_list_london_sperm_val = london_average_costs_model.sperm_ivf_val
    queryset_list_london_icsi_val = london_average_costs_model.icsi_val
    queryset_list_london_iui_val = london_average_costs_model.iui_val

    queryset_list_manchester = queryset_list_uk.filter(clinicRegion__iexact='Manchester')
    my_total_clinic_count_manchester = queryset_list_manchester.count()
    manchester_average_costs_model = Manchester.objects.get(pk=1)
    queryset_list_manchester_ivf_val = manchester_average_costs_model.standard_ivf_val
    queryset_list_manchester_egg_val = manchester_average_costs_model.egg_ivf_val
    queryset_list_manchester_embryo_val = manchester_average_costs_model.embryo_ivf_val
    queryset_list_manchester_sperm_val = manchester_average_costs_model.sperm_ivf_val
    queryset_list_manchester_icsi_val = manchester_average_costs_model.icsi_val
    queryset_list_manchester_iui_val = manchester_average_costs_model.iui_val

    queryset_list_middlesbrough = queryset_list_uk.filter(clinicRegion__iexact='Middlesbrough')
    my_total_clinic_count_middlesbrough = queryset_list_middlesbrough.count()
    middlesbrough_average_costs_model = Middlesbrough.objects.get(pk=1)
    queryset_list_middlesbrough_ivf_val = middlesbrough_average_costs_model.standard_ivf_val
    queryset_list_middlesbrough_egg_val = middlesbrough_average_costs_model.egg_ivf_val
    queryset_list_middlesbrough_embryo_val = middlesbrough_average_costs_model.embryo_ivf_val
    queryset_list_middlesbrough_sperm_val = middlesbrough_average_costs_model.sperm_ivf_val
    queryset_list_middlesbrough_icsi_val = middlesbrough_average_costs_model.icsi_val
    queryset_list_middlesbrough_iui_val = middlesbrough_average_costs_model.iui_val

    queryset_list_newcastle = queryset_list_uk.filter(clinicRegion__iexact='Newcastle')
    my_total_clinic_count_newcastle = queryset_list_newcastle.count()
    newcastle_average_costs_model = Newcastle.objects.get(pk=1)
    queryset_list_newcastle_ivf_val = newcastle_average_costs_model.standard_ivf_val
    queryset_list_newcastle_egg_val = newcastle_average_costs_model.egg_ivf_val
    queryset_list_newcastle_embryo_val = newcastle_average_costs_model.embryo_ivf_val
    queryset_list_newcastle_sperm_val = newcastle_average_costs_model.sperm_ivf_val
    queryset_list_newcastle_icsi_val = newcastle_average_costs_model.icsi_val
    queryset_list_newcastle_iui_val = newcastle_average_costs_model.iui_val

    queryset_list_norwich = queryset_list_uk.filter(clinicRegion__iexact='Norwich')
    my_total_clinic_count_norwich = queryset_list_norwich.count()
    norwich_average_costs_model = Norwich.objects.get(pk=1)
    queryset_list_norwich_ivf_val = norwich_average_costs_model.standard_ivf_val
    queryset_list_norwich_egg_val = norwich_average_costs_model.egg_ivf_val
    queryset_list_norwich_embryo_val = norwich_average_costs_model.embryo_ivf_val
    queryset_list_norwich_sperm_val = norwich_average_costs_model.sperm_ivf_val
    queryset_list_norwich_icsi_val = norwich_average_costs_model.icsi_val
    queryset_list_norwich_iui_val = norwich_average_costs_model.iui_val

    queryset_list_nottingham = queryset_list_uk.filter(clinicRegion__iexact='Nottingham')
    my_total_clinic_count_nottingham = queryset_list_nottingham.count()
    nottingham_average_costs_model = Nottingham.objects.get(pk=1)
    queryset_list_nottingham_ivf_val = nottingham_average_costs_model.standard_ivf_val
    queryset_list_nottingham_egg_val = nottingham_average_costs_model.egg_ivf_val
    queryset_list_nottingham_embryo_val = nottingham_average_costs_model.embryo_ivf_val
    queryset_list_nottingham_sperm_val = nottingham_average_costs_model.sperm_ivf_val
    queryset_list_nottingham_icsi_val = nottingham_average_costs_model.icsi_val
    queryset_list_nottingham_iui_val = nottingham_average_costs_model.iui_val

    queryset_list_oxford = queryset_list_uk.filter(clinicRegion__iexact='Oxford')
    my_total_clinic_count_oxford = queryset_list_oxford.count()
    oxford_average_costs_model = Oxford.objects.get(pk=1)
    queryset_list_oxford_ivf_val = oxford_average_costs_model.standard_ivf_val
    queryset_list_oxford_egg_val = oxford_average_costs_model.egg_ivf_val
    queryset_list_oxford_embryo_val = oxford_average_costs_model.embryo_ivf_val
    queryset_list_oxford_sperm_val = oxford_average_costs_model.sperm_ivf_val
    queryset_list_oxford_icsi_val = oxford_average_costs_model.icsi_val
    queryset_list_oxford_iui_val = oxford_average_costs_model.iui_val

    queryset_list_peterborough = queryset_list_uk.filter(clinicRegion__iexact='Peterborough')
    my_total_clinic_count_peterborough = queryset_list_peterborough.count()
    peterborough_average_costs_model = Peterborough.objects.get(pk=1)
    queryset_list_peterborough_ivf_val = peterborough_average_costs_model.standard_ivf_val
    queryset_list_peterborough_egg_val = peterborough_average_costs_model.egg_ivf_val
    queryset_list_peterborough_embryo_val = peterborough_average_costs_model.embryo_ivf_val
    queryset_list_peterborough_sperm_val = peterborough_average_costs_model.sperm_ivf_val
    queryset_list_peterborough_icsi_val = peterborough_average_costs_model.icsi_val
    queryset_list_peterborough_iui_val = peterborough_average_costs_model.iui_val

    queryset_list_plymouth = queryset_list_uk.filter(clinicRegion__iexact='Plymouth')
    my_total_clinic_count_plymouth = queryset_list_plymouth.count()
    plymouth_average_costs_model = Plymouth.objects.get(pk=1)
    queryset_list_plymouth_ivf_val = plymouth_average_costs_model.standard_ivf_val
    queryset_list_plymouth_egg_val = plymouth_average_costs_model.egg_ivf_val
    queryset_list_plymouth_embryo_val = plymouth_average_costs_model.embryo_ivf_val
    queryset_list_plymouth_sperm_val = plymouth_average_costs_model.sperm_ivf_val
    queryset_list_plymouth_icsi_val = plymouth_average_costs_model.icsi_val
    queryset_list_plymouth_iui_val = plymouth_average_costs_model.iui_val

    queryset_list_portsmouth = queryset_list_uk.filter(clinicRegion__iexact='Portsmouth')
    my_total_clinic_count_portsmouth = queryset_list_portsmouth.count()
    portsmouth_average_costs_model = Portsmouth.objects.get(pk=1)
    queryset_list_portsmouth_ivf_val = portsmouth_average_costs_model.standard_ivf_val
    queryset_list_portsmouth_egg_val = portsmouth_average_costs_model.egg_ivf_val
    queryset_list_portsmouth_embryo_val = portsmouth_average_costs_model.embryo_ivf_val
    queryset_list_portsmouth_sperm_val = portsmouth_average_costs_model.sperm_ivf_val
    queryset_list_portsmouth_icsi_val = portsmouth_average_costs_model.icsi_val
    queryset_list_portsmouth_iui_val = portsmouth_average_costs_model.iui_val

    queryset_list_salisbury = queryset_list_uk.filter(clinicRegion__iexact='Salisbury')
    my_total_clinic_count_salisbury = queryset_list_salisbury.count()
    salisbury_average_costs_model = Salisbury.objects.get(pk=1)
    queryset_list_salisbury_ivf_val = salisbury_average_costs_model.standard_ivf_val
    queryset_list_salisbury_egg_val = salisbury_average_costs_model.egg_ivf_val
    queryset_list_salisbury_embryo_val = salisbury_average_costs_model.embryo_ivf_val
    queryset_list_salisbury_sperm_val = salisbury_average_costs_model.sperm_ivf_val
    queryset_list_salisbury_icsi_val = salisbury_average_costs_model.icsi_val
    queryset_list_salisbury_iui_val = salisbury_average_costs_model.iui_val

    queryset_list_sheffield = queryset_list_uk.filter(clinicRegion__iexact='Sheffield')
    my_total_clinic_count_sheffield = queryset_list_sheffield.count()
    sheffield_average_costs_model = Sheffield.objects.get(pk=1)
    queryset_list_sheffield_ivf_val = sheffield_average_costs_model.standard_ivf_val
    queryset_list_sheffield_egg_val = sheffield_average_costs_model.egg_ivf_val
    queryset_list_sheffield_embryo_val = sheffield_average_costs_model.embryo_ivf_val
    queryset_list_sheffield_sperm_val = sheffield_average_costs_model.sperm_ivf_val
    queryset_list_sheffield_icsi_val = sheffield_average_costs_model.icsi_val
    queryset_list_sheffield_iui_val = sheffield_average_costs_model.iui_val

    queryset_list_southampton = queryset_list_uk.filter(clinicRegion__iexact='Southampton')
    my_total_clinic_count_southampton = queryset_list_southampton.count()
    southampton_average_costs_model = Southampton.objects.get(pk=1)
    queryset_list_southampton_ivf_val = southampton_average_costs_model.standard_ivf_val
    queryset_list_southampton_egg_val = southampton_average_costs_model.egg_ivf_val
    queryset_list_southampton_embryo_val = southampton_average_costs_model.embryo_ivf_val
    queryset_list_southampton_sperm_val = southampton_average_costs_model.sperm_ivf_val
    queryset_list_southampton_icsi_val = southampton_average_costs_model.icsi_val
    queryset_list_southampton_iui_val = southampton_average_costs_model.iui_val

    queryset_list_swansea = queryset_list_uk.filter(clinicRegion__iexact='Swansea')
    my_total_clinic_count_swansea = queryset_list_swansea.count()
    swansea_average_costs_model = Swansea.objects.get(pk=1)
    queryset_list_swansea_ivf_val = swansea_average_costs_model.standard_ivf_val
    queryset_list_swansea_egg_val = swansea_average_costs_model.egg_ivf_val
    queryset_list_swansea_embryo_val = swansea_average_costs_model.embryo_ivf_val
    queryset_list_swansea_sperm_val = swansea_average_costs_model.sperm_ivf_val
    queryset_list_swansea_icsi_val = swansea_average_costs_model.icsi_val
    queryset_list_swansea_iui_val = swansea_average_costs_model.iui_val

    context = {
        'year': year,
        'best_clinics_count': best_clinics_count,
        'my_total_clinic_count': my_total_clinic_count,

        'queryset_list_uk_natural_ivf_val': queryset_list_uk_natural_ivf_val,
        'queryset_list_uk_mild_ivf_val': queryset_list_uk_mild_ivf_val,
        'queryset_list_uk_standard_ivf_val': queryset_list_uk_standard_ivf_val,
        'queryset_list_uk_egg_ivf_val': queryset_list_uk_egg_ivf_val,
        'queryset_list_uk_known_egg_ivf_val': queryset_list_uk_known_egg_ivf_val,
        'queryset_list_uk_shared_egg_ivf_val': queryset_list_uk_shared_egg_ivf_val,
        'queryset_list_uk_embryo_ivf_val': queryset_list_uk_embryo_ivf_val,
        'queryset_list_uk_known_embryo_ivf_val': queryset_list_uk_known_embryo_ivf_val,
        'queryset_list_uk_sperm_ivf_val': queryset_list_uk_sperm_ivf_val,
        'queryset_list_uk_known_sperm_ivf_val': queryset_list_uk_known_sperm_ivf_val,
        'queryset_list_uk_icsi_val': queryset_list_uk_icsi_val,
        'queryset_list_uk_iui_val': queryset_list_uk_iui_val,

        'my_total_clinic_count_aberdeen': my_total_clinic_count_aberdeen,
        'queryset_list_aberdeen_ivf_val': queryset_list_aberdeen_ivf_val,
        'queryset_list_aberdeen_egg_val': queryset_list_aberdeen_egg_val,
        'queryset_list_aberdeen_embryo_val': queryset_list_aberdeen_embryo_val,
        'queryset_list_aberdeen_sperm_val': queryset_list_aberdeen_sperm_val,
        'queryset_list_aberdeen_icsi_val': queryset_list_aberdeen_icsi_val,
        'queryset_list_aberdeen_iui_val': queryset_list_aberdeen_iui_val,

        'my_total_clinic_count_bath': my_total_clinic_count_bath,
        'queryset_list_bath_ivf_val': queryset_list_bath_ivf_val,
        'queryset_list_bath_egg_val': queryset_list_bath_egg_val,
        'queryset_list_bath_embryo_val': queryset_list_bath_embryo_val,
        'queryset_list_bath_sperm_val': queryset_list_bath_sperm_val,
        'queryset_list_bath_icsi_val': queryset_list_bath_icsi_val,
        'queryset_list_bath_iui_val': queryset_list_bath_iui_val,

        'my_total_clinic_count_belfast': my_total_clinic_count_belfast,
        'queryset_list_belfast_ivf_val': queryset_list_belfast_ivf_val,
        'queryset_list_belfast_egg_val': queryset_list_belfast_egg_val,
        'queryset_list_belfast_embryo_val': queryset_list_belfast_embryo_val,
        'queryset_list_belfast_sperm_val': queryset_list_belfast_sperm_val,
        'queryset_list_belfast_icsi_val': queryset_list_belfast_icsi_val,
        'queryset_list_belfast_iui_val': queryset_list_belfast_iui_val,

        'my_total_clinic_count_birmingham': my_total_clinic_count_birmingham,
        'queryset_list_birmingham_ivf_val': queryset_list_birmingham_ivf_val,
        'queryset_list_birmingham_egg_val': queryset_list_birmingham_egg_val,
        'queryset_list_birmingham_embryo_val': queryset_list_birmingham_embryo_val,
        'queryset_list_birmingham_sperm_val': queryset_list_birmingham_sperm_val,
        'queryset_list_birmingham_icsi_val': queryset_list_birmingham_icsi_val,
        'queryset_list_birmingham_iui_val': queryset_list_birmingham_iui_val,

        'my_total_clinic_count_bournemouth': my_total_clinic_count_bournemouth,
        'queryset_list_bournemouth_ivf_val': queryset_list_bournemouth_ivf_val,
        'queryset_list_bournemouth_egg_val': queryset_list_bournemouth_egg_val,
        'queryset_list_bournemouth_embryo_val': queryset_list_bournemouth_embryo_val,
        'queryset_list_bournemouth_sperm_val': queryset_list_bournemouth_sperm_val,
        'queryset_list_bournemouth_icsi_val': queryset_list_bournemouth_icsi_val,
        'queryset_list_bournemouth_iui_val': queryset_list_bournemouth_iui_val,

        'my_total_clinic_count_brighton': my_total_clinic_count_brighton,
        'queryset_list_brighton_ivf_val': queryset_list_brighton_ivf_val,
        'queryset_list_brighton_egg_val': queryset_list_brighton_egg_val,
        'queryset_list_brighton_embryo_val': queryset_list_brighton_embryo_val,
        'queryset_list_brighton_sperm_val': queryset_list_brighton_sperm_val,
        'queryset_list_brighton_icsi_val': queryset_list_brighton_icsi_val,
        'queryset_list_brighton_iui_val': queryset_list_brighton_iui_val,

        'my_total_clinic_count_bristol': my_total_clinic_count_bristol,
        'queryset_list_bristol_ivf_val': queryset_list_bristol_ivf_val,
        'queryset_list_bristol_egg_val': queryset_list_bristol_egg_val,
        'queryset_list_bristol_embryo_val': queryset_list_bristol_embryo_val,
        'queryset_list_bristol_sperm_val': queryset_list_bristol_sperm_val,
        'queryset_list_bristol_icsi_val': queryset_list_bristol_icsi_val,
        'queryset_list_bristol_iui_val': queryset_list_bristol_iui_val,

        'my_total_clinic_count_cambridge': my_total_clinic_count_cambridge,
        'queryset_list_cambridge_ivf_val': queryset_list_cambridge_ivf_val,
        'queryset_list_cambridge_egg_val': queryset_list_cambridge_egg_val,
        'queryset_list_cambridge_embryo_val': queryset_list_cambridge_embryo_val,
        'queryset_list_cambridge_sperm_val': queryset_list_cambridge_sperm_val,
        'queryset_list_cambridge_icsi_val': queryset_list_cambridge_icsi_val,
        'queryset_list_cambridge_iui_val': queryset_list_cambridge_iui_val,

        'my_total_clinic_count_cardiff': my_total_clinic_count_cardiff,
        'queryset_list_cardiff_ivf_val': queryset_list_cardiff_ivf_val,
        'queryset_list_cardiff_egg_val': queryset_list_cardiff_egg_val,
        'queryset_list_cardiff_embryo_val': queryset_list_cardiff_embryo_val,
        'queryset_list_cardiff_sperm_val': queryset_list_cardiff_sperm_val,
        'queryset_list_cardiff_icsi_val': queryset_list_cardiff_icsi_val,
        'queryset_list_cardiff_iui_val': queryset_list_cardiff_iui_val,

        'my_total_clinic_count_colchester': my_total_clinic_count_colchester,
        'queryset_list_colchester_ivf_val': queryset_list_colchester_ivf_val,
        'queryset_list_colchester_egg_val': queryset_list_colchester_egg_val,
        'queryset_list_colchester_embryo_val': queryset_list_colchester_embryo_val,
        'queryset_list_colchester_sperm_val': queryset_list_colchester_sperm_val,
        'queryset_list_colchester_icsi_val': queryset_list_colchester_icsi_val,
        'queryset_list_colchester_iui_val': queryset_list_colchester_iui_val,

        'my_total_clinic_count_derby': my_total_clinic_count_derby,
        'queryset_list_derby_ivf_val': queryset_list_derby_ivf_val,
        'queryset_list_derby_egg_val': queryset_list_derby_egg_val,
        'queryset_list_derby_embryo_val': queryset_list_derby_embryo_val,
        'queryset_list_derby_sperm_val': queryset_list_derby_sperm_val,
        'queryset_list_derby_icsi_val': queryset_list_derby_icsi_val,
        'queryset_list_derby_iui_val': queryset_list_derby_iui_val,

        'my_total_clinic_count_exeter': my_total_clinic_count_exeter,
        'queryset_list_exeter_ivf_val': queryset_list_exeter_ivf_val,
        'queryset_list_exeter_egg_val': queryset_list_exeter_egg_val,
        'queryset_list_exeter_embryo_val': queryset_list_exeter_embryo_val,
        'queryset_list_exeter_sperm_val': queryset_list_exeter_sperm_val,
        'queryset_list_exeter_icsi_val': queryset_list_exeter_icsi_val,
        'queryset_list_exeter_iui_val': queryset_list_exeter_iui_val,

        'my_total_clinic_count_glasgow': my_total_clinic_count_glasgow,
        'queryset_list_glasgow_ivf_val': queryset_list_glasgow_ivf_val,
        'queryset_list_glasgow_egg_val': queryset_list_glasgow_egg_val,
        'queryset_list_glasgow_embryo_val': queryset_list_glasgow_embryo_val,
        'queryset_list_glasgow_sperm_val': queryset_list_glasgow_sperm_val,
        'queryset_list_glasgow_icsi_val': queryset_list_glasgow_icsi_val,
        'queryset_list_glasgow_iui_val': queryset_list_glasgow_iui_val,

        'my_total_clinic_count_hull': my_total_clinic_count_hull,
        'queryset_list_hull_ivf_val': queryset_list_hull_ivf_val,
        'queryset_list_hull_egg_val': queryset_list_hull_egg_val,
        'queryset_list_hull_embryo_val': queryset_list_hull_embryo_val,
        'queryset_list_hull_sperm_val': queryset_list_hull_sperm_val,
        'queryset_list_hull_icsi_val': queryset_list_hull_icsi_val,
        'queryset_list_hull_iui_val': queryset_list_hull_iui_val,

        'my_total_clinic_count_chelmsford': my_total_clinic_count_chelmsford,
        'queryset_list_chelmsford_ivf_val': queryset_list_chelmsford_ivf_val,
        'queryset_list_chelmsford_egg_val': queryset_list_chelmsford_egg_val,
        'queryset_list_chelmsford_embryo_val': queryset_list_chelmsford_embryo_val,
        'queryset_list_chelmsford_sperm_val': queryset_list_chelmsford_sperm_val,
        'queryset_list_chelmsford_icsi_val': queryset_list_chelmsford_icsi_val,
        'queryset_list_chelmsford_iui_val': queryset_list_chelmsford_iui_val,

        'my_total_clinic_count_leeds': my_total_clinic_count_leeds,
        'queryset_list_leeds_ivf_val': queryset_list_leeds_ivf_val,
        'queryset_list_leeds_egg_val': queryset_list_leeds_egg_val,
        'queryset_list_leeds_embryo_val': queryset_list_leeds_embryo_val,
        'queryset_list_leeds_sperm_val': queryset_list_leeds_sperm_val,
        'queryset_list_leeds_icsi_val': queryset_list_leeds_icsi_val,
        'queryset_list_leeds_iui_val': queryset_list_leeds_iui_val,

        'my_total_clinic_count_leicester': my_total_clinic_count_leicester,
        'queryset_list_leicester_ivf_val': queryset_list_leicester_ivf_val,
        'queryset_list_leicester_egg_val': queryset_list_leicester_egg_val,
        'queryset_list_leicester_embryo_val': queryset_list_leicester_embryo_val,
        'queryset_list_leicester_sperm_val': queryset_list_leicester_sperm_val,
        'queryset_list_leicester_icsi_val': queryset_list_leicester_icsi_val,
        'queryset_list_leicester_iui_val': queryset_list_leicester_iui_val,

        'my_total_clinic_count_liverpool': my_total_clinic_count_liverpool,
        'queryset_list_liverpool_ivf_val': queryset_list_liverpool_ivf_val,
        'queryset_list_liverpool_egg_val': queryset_list_liverpool_egg_val,
        'queryset_list_liverpool_embryo_val': queryset_list_liverpool_embryo_val,
        'queryset_list_liverpool_sperm_val': queryset_list_liverpool_sperm_val,
        'queryset_list_liverpool_icsi_val': queryset_list_liverpool_icsi_val,
        'queryset_list_liverpool_iui_val': queryset_list_liverpool_iui_val,

        'my_total_clinic_count_london': my_total_clinic_count_london,
        'queryset_list_london_ivf_val': queryset_list_london_ivf_val,
        'queryset_list_london_egg_val': queryset_list_london_egg_val,
        'queryset_list_london_embryo_val': queryset_list_london_embryo_val,
        'queryset_list_london_sperm_val': queryset_list_london_sperm_val,
        'queryset_list_london_icsi_val': queryset_list_london_icsi_val,
        'queryset_list_london_iui_val': queryset_list_london_iui_val,

        'my_total_clinic_count_manchester': my_total_clinic_count_manchester,
        'queryset_list_manchester_ivf_val': queryset_list_manchester_ivf_val,
        'queryset_list_manchester_egg_val': queryset_list_manchester_egg_val,
        'queryset_list_manchester_embryo_val': queryset_list_manchester_embryo_val,
        'queryset_list_manchester_sperm_val': queryset_list_manchester_sperm_val,
        'queryset_list_manchester_icsi_val': queryset_list_manchester_icsi_val,
        'queryset_list_manchester_iui_val': queryset_list_manchester_iui_val,

        'my_total_clinic_count_middlesbrough': my_total_clinic_count_middlesbrough,
        'queryset_list_middlesbrough_ivf_val': queryset_list_middlesbrough_ivf_val,
        'queryset_list_middlesbrough_egg_val': queryset_list_middlesbrough_egg_val,
        'queryset_list_middlesbrough_embryo_val': queryset_list_middlesbrough_embryo_val,
        'queryset_list_middlesbrough_sperm_val': queryset_list_middlesbrough_sperm_val,
        'queryset_list_middlesbrough_icsi_val': queryset_list_middlesbrough_icsi_val,
        'queryset_list_middlesbrough_iui_val': queryset_list_middlesbrough_iui_val,

        'my_total_clinic_count_newcastle': my_total_clinic_count_newcastle,
        'queryset_list_newcastle_ivf_val': queryset_list_newcastle_ivf_val,
        'queryset_list_newcastle_egg_val': queryset_list_newcastle_egg_val,
        'queryset_list_newcastle_embryo_val': queryset_list_newcastle_embryo_val,
        'queryset_list_newcastle_sperm_val': queryset_list_newcastle_sperm_val,
        'queryset_list_newcastle_icsi_val': queryset_list_newcastle_icsi_val,
        'queryset_list_newcastle_iui_val': queryset_list_newcastle_iui_val,

        'my_total_clinic_count_norwich': my_total_clinic_count_norwich,
        'queryset_list_norwich_ivf_val': queryset_list_norwich_ivf_val,
        'queryset_list_norwich_egg_val': queryset_list_norwich_egg_val,
        'queryset_list_norwich_embryo_val': queryset_list_norwich_embryo_val,
        'queryset_list_norwich_sperm_val': queryset_list_norwich_sperm_val,
        'queryset_list_norwich_icsi_val': queryset_list_norwich_icsi_val,
        'queryset_list_norwich_iui_val': queryset_list_norwich_iui_val,

        'my_total_clinic_count_nottingham': my_total_clinic_count_nottingham,
        'queryset_list_nottingham_ivf_val': queryset_list_nottingham_ivf_val,
        'queryset_list_nottingham_egg_val': queryset_list_nottingham_egg_val,
        'queryset_list_nottingham_embryo_val': queryset_list_nottingham_embryo_val,
        'queryset_list_nottingham_sperm_val': queryset_list_nottingham_sperm_val,
        'queryset_list_nottingham_icsi_val': queryset_list_nottingham_icsi_val,
        'queryset_list_nottingham_iui_val': queryset_list_nottingham_iui_val,

        'my_total_clinic_count_oxford': my_total_clinic_count_oxford,
        'queryset_list_oxford_ivf_val': queryset_list_oxford_ivf_val,
        'queryset_list_oxford_egg_val': queryset_list_oxford_egg_val,
        'queryset_list_oxford_embryo_val': queryset_list_oxford_embryo_val,
        'queryset_list_oxford_sperm_val': queryset_list_oxford_sperm_val,
        'queryset_list_oxford_icsi_val': queryset_list_oxford_icsi_val,
        'queryset_list_oxford_iui_val': queryset_list_oxford_iui_val,

        'my_total_clinic_count_peterborough': my_total_clinic_count_peterborough,
        'queryset_list_peterborough_ivf_val': queryset_list_peterborough_ivf_val,
        'queryset_list_peterborough_egg_val': queryset_list_peterborough_egg_val,
        'queryset_list_peterborough_embryo_val': queryset_list_peterborough_embryo_val,
        'queryset_list_peterborough_sperm_val': queryset_list_peterborough_sperm_val,
        'queryset_list_peterborough_icsi_val': queryset_list_peterborough_icsi_val,
        'queryset_list_peterborough_iui_val': queryset_list_peterborough_iui_val,

        'my_total_clinic_count_plymouth': my_total_clinic_count_plymouth,
        'queryset_list_plymouth_ivf_val': queryset_list_plymouth_ivf_val,
        'queryset_list_plymouth_egg_val': queryset_list_plymouth_egg_val,
        'queryset_list_plymouth_embryo_val': queryset_list_plymouth_embryo_val,
        'queryset_list_plymouth_sperm_val': queryset_list_plymouth_sperm_val,
        'queryset_list_plymouth_icsi_val': queryset_list_plymouth_icsi_val,
        'queryset_list_plymouth_iui_val': queryset_list_plymouth_iui_val,

        'my_total_clinic_count_portsmouth': my_total_clinic_count_portsmouth,
        'queryset_list_portsmouth_ivf_val': queryset_list_portsmouth_ivf_val,
        'queryset_list_portsmouth_egg_val': queryset_list_portsmouth_egg_val,
        'queryset_list_portsmouth_embryo_val': queryset_list_portsmouth_embryo_val,
        'queryset_list_portsmouth_sperm_val': queryset_list_portsmouth_sperm_val,
        'queryset_list_portsmouth_icsi_val': queryset_list_portsmouth_icsi_val,
        'queryset_list_portsmouth_iui_val': queryset_list_portsmouth_iui_val,

        'my_total_clinic_count_salisbury': my_total_clinic_count_salisbury,
        'queryset_list_salisbury_ivf_val': queryset_list_salisbury_ivf_val,
        'queryset_list_salisbury_egg_val': queryset_list_salisbury_egg_val,
        'queryset_list_salisbury_embryo_val': queryset_list_salisbury_embryo_val,
        'queryset_list_salisbury_sperm_val': queryset_list_salisbury_sperm_val,
        'queryset_list_salisbury_icsi_val': queryset_list_salisbury_icsi_val,
        'queryset_list_salisbury_iui_val': queryset_list_salisbury_iui_val,

        'my_total_clinic_count_sheffield': my_total_clinic_count_sheffield,
        'queryset_list_sheffield_ivf_val': queryset_list_sheffield_ivf_val,
        'queryset_list_sheffield_egg_val': queryset_list_sheffield_egg_val,
        'queryset_list_sheffield_embryo_val': queryset_list_sheffield_embryo_val,
        'queryset_list_sheffield_sperm_val': queryset_list_sheffield_sperm_val,
        'queryset_list_sheffield_icsi_val': queryset_list_sheffield_icsi_val,
        'queryset_list_sheffield_iui_val': queryset_list_sheffield_iui_val,

        'my_total_clinic_count_southampton': my_total_clinic_count_southampton,
        'queryset_list_southampton_ivf_val': queryset_list_southampton_ivf_val,
        'queryset_list_southampton_egg_val': queryset_list_southampton_egg_val,
        'queryset_list_southampton_embryo_val': queryset_list_southampton_embryo_val,
        'queryset_list_southampton_sperm_val': queryset_list_southampton_sperm_val,
        'queryset_list_southampton_icsi_val': queryset_list_southampton_icsi_val,
        'queryset_list_southampton_iui_val': queryset_list_southampton_iui_val,

        'my_total_clinic_count_swansea': my_total_clinic_count_swansea,
        'queryset_list_swansea_ivf_val': queryset_list_swansea_ivf_val,
        'queryset_list_swansea_egg_val': queryset_list_swansea_egg_val,
        'queryset_list_swansea_embryo_val': queryset_list_swansea_embryo_val,
        'queryset_list_swansea_sperm_val': queryset_list_swansea_sperm_val,
        'queryset_list_swansea_icsi_val': queryset_list_swansea_icsi_val,
        'queryset_list_swansea_iui_val': queryset_list_swansea_iui_val,
        }

    return render(request, 'main/Locations/UKLocations/uk-regions-ivf.html', context)

