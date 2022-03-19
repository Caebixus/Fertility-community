from django.shortcuts import render
from django import template
from clinic.models import BasicClinic
from packages.models import Package
from django.db.models import Avg
from .choices import CATEGORY_CHOICES_STATES_NORTH_AMERICA, CATEGORY_CHOICES_STATES_EUROPE, CATEGORY_CHOICES_STATES_ASIA, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_MX_CITIES, CATEGORY_CHOICES_UK_CITIES, CATEGORY_CHOICES_CZ_CITIES, CATEGORY_CHOICES_SK_CITIES, CATEGORY_CHOICES_SP_CITIES, CATEGORY_CHOICES_IN_CITIES, CATEGORY_CHOICES_GR_CITIES, CATEGORY_CHOICES_CY_CITIES, CATEGORY_CHOICES_DK_CITIES, CATEGORY_CHOICES_DE_CITIES, CATEGORY_CHOICES_LV_CITIES, CATEGORY_CHOICES_PT_CITIES, AL_CITIES, AZ_CITIES, CA_CITIES, CO_CITIES, CT_CITIES, DE_CITIES, FL_CITIES, GA_CITIES, HI_CITIES, IL_CITIES, IN_CITIES, KY_CITIES, LA_CITIES, KY_CITIES, MA_CITIES, MO_CITIES, NV_CITIES, NJ_CITIES, NY_CITIES, NC_CITIES, OH_CITIES, OK_CITIES, OR_CITIES, PA_CITIES, TN_CITIES, TX_CITIES, VA_CITIES, WA_CITIES
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def search_new(request):
    queryset_list = BasicClinic.objects.all().filter(is_published=True)

    values = request.GET
    if "States" or "Region" or "City" or "treatments" in values.keys():
        search_origin_version = True
    else:
        search_origin_version = False

    states = 'empty'
    region = 'empty'
    city = 'empty'
    treatments = 'empty'

    if 'States' in values.keys():
        states = request.GET['States']
        if states == None or states == '':
            states = 'empty'
    else:
        states = 'empty'

    if 'Region' in values.keys():
        region = request.GET['Region']
        if region == None or region == '':
            region = 'empty'
    else:
        region = 'empty'

    if 'City' in values.keys():
        city = request.GET['City']
        if city == None or city == '':
            city = 'empty'
    else:
        city = 'empty'

    if 'treatments' in values.keys():
        treatments = request.GET['treatments']
        if treatments == None or treatments == '':
            treatments = 'empty'
    else:
        treatments = 'empty'


    if states != 'empty':
        queryset_list = queryset_list.filter(clinicState__iexact=states).order_by('-digitalTransparencyIndex')

        averageIVFPrice = queryset_list.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
        averageEggPrice = queryset_list.aggregate(average=Avg('egg_donor_recipients_cost'))
        averageEmbryoPrice = queryset_list.aggregate(average=Avg('embryo_donor_recipients_cost'))
        averageSpermPrice = queryset_list.aggregate(average=Avg('sperm_donor_recipients_cost'))
        averageICSIPrice = queryset_list.aggregate(average=Avg('icsi_treatment_cost'))

        if region != 'empty':

            if city != 'empty':

                if treatments == 'Alltreatmentstrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'IVFtreatmenttrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, ivf_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'IVFtreatmentmildtrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, mild_ivf_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'IVFtreatmentovariantrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, ovarian_ivf_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'ICSItreatmenttrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, icsi_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'Eggdonationrecipientstrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, egg_donor_recipients=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'Spermdonationrecipientstrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, sperm_donor_recipients=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'Embryodonationrecipientstrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, embryo_donor_recipients=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'EggFreezingtrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, egg_freezing=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'EmbryoFreezingtrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, embryo_freezing=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'SpermFreezingtrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, sperm_freezing=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'Surrogacytrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, surrogacy=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'IUItreatmenttrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, iui_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'Singlewomantreatmenttrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, single_woman_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'ReciprocalIVFtrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city, reciprocal_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                else:
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, clinicCity__iexact=city).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

            else:
                queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            if treatments != 'empty':

                if treatments == 'Alltreatmentstrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'IVFtreatmenttrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, ivf_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'IVFtreatmentmildtrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, mild_ivf_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'IVFtreatmentovariantrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, ovarian_ivf_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'ICSItreatmenttrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, icsi_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'Eggdonationrecipientstrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, egg_donor_recipients=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'Spermdonationrecipientstrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, sperm_donor_recipients=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'Embryodonationrecipientstrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, embryo_donor_recipients=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'EggFreezingtrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, egg_freezing=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'EmbryoFreezingtrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, embryo_freezing=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'SpermFreezingtrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, sperm_freezing=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'Surrogacytrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, surrogacy=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'IUItreatmenttrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, iui_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'Singlewomantreatmenttrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, single_woman_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                elif treatments == 'ReciprocalIVFtrue':
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region, reciprocal_treatment=True).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

                else:
                    queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region).order_by('-digitalTransparencyIndex')
                    order_data = list(queryset_list)

                    my_total_count = queryset_list.count()

                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

            else:
                queryset_list = queryset_list.filter(clinicState__iexact=states, clinicRegion__iexact=region).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

        else:
            if treatments == 'Alltreatmentstrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'IVFtreatmenttrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, ivf_treatment=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'IVFtreatmentmildtrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, mild_ivf_treatment=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'IVFtreatmentovariantrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, ovarian_ivf_treatment=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'ICSItreatmenttrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, icsi_treatment=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'Eggdonationrecipientstrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, egg_donor_recipients=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'Spermdonationrecipientstrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, sperm_donor_recipients=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'Embryodonationrecipientstrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, embryo_donor_recipients=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'EggFreezingtrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, egg_freezing=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'EmbryoFreezingtrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, embryo_freezing=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'SpermFreezingtrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, sperm_freezing=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'Surrogacytrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, surrogacy=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'IUItreatmenttrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, iui_treatment=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'Singlewomantreatmenttrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, single_woman_treatment=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            elif treatments == 'ReciprocalIVFtrue':
                queryset_list = queryset_list.filter(clinicState__iexact=states, reciprocal_treatment=True).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            else:
                queryset_list = queryset_list.filter(clinicState__iexact=states).order_by('-digitalTransparencyIndex')
                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            queryset_list = queryset_list.filter(clinicState__iexact=states).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

    else:
        if treatments == 'Alltreatmentstrue':
            queryset_list = queryset_list.order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'IVFtreatmenttrue':
            queryset_list = queryset_list.filter(ivf_treatment=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'IVFtreatmentmildtrue':
            queryset_list = queryset_list.filter(mild_ivf_treatment=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'IVFtreatmentovariantrue':
            queryset_list = queryset_list.filter(ovarian_ivf_treatment=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'ICSItreatmenttrue':
            queryset_list = queryset_list.filter(icsi_treatment=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'Eggdonationrecipientstrue':
            queryset_list = queryset_list.filter(egg_donor_recipients=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'Spermdonationrecipientstrue':
            queryset_list = queryset_list.filter(sperm_donor_recipients=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'Embryodonationrecipientstrue':
            queryset_list = queryset_list.filter(embryo_donor_recipients=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'EggFreezingtrue':
            queryset_list = queryset_list.filter(egg_freezing=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'EmbryoFreezingtrue':
            queryset_list = queryset_list.filter(embryo_freezing=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'SpermFreezingtrue':
            queryset_list = queryset_list.filter(sperm_freezing=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'Surrogacytrue':
            queryset_list = queryset_list.filter(surrogacy=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'IUItreatmenttrue':
            queryset_list = queryset_list.filter(iui_treatment=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'Singlewomantreatmenttrue':
            queryset_list = queryset_list.filter(single_woman_treatment=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        elif treatments == 'ReciprocalIVFtrue':
            queryset_list = queryset_list.filter(reciprocal_treatment=True).order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        else:
            queryset_list = queryset_list.order_by('-digitalTransparencyIndex')
            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        queryset_list = queryset_list.order_by('-digitalTransparencyIndex')
        order_data = list(queryset_list)

        my_total_count = queryset_list.count()

        paginator = Paginator(order_data, 10)
        page = request.GET.get('page')
        paginationing = paginator.get_page(page)

        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'KY_CITIES': KY_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

        return render(request, 'search/search.html', context)
