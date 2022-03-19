from django.shortcuts import render
from django import template
from clinic.models import BasicClinic
from packages.models import Package
from django.db.models import Avg
from .choices import CATEGORY_CHOICES_STATES_NORTH_AMERICA, CATEGORY_CHOICES_STATES_EUROPE, CATEGORY_CHOICES_STATES_ASIA, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_MX_CITIES, CATEGORY_CHOICES_UK_CITIES, CATEGORY_CHOICES_CZ_CITIES, CATEGORY_CHOICES_SK_CITIES, CATEGORY_CHOICES_SP_CITIES, CATEGORY_CHOICES_IN_CITIES, CATEGORY_CHOICES_GR_CITIES, CATEGORY_CHOICES_CY_CITIES, CATEGORY_CHOICES_DK_CITIES, CATEGORY_CHOICES_DE_CITIES, CATEGORY_CHOICES_LV_CITIES, CATEGORY_CHOICES_PT_CITIES, AL_CITIES, AZ_CITIES, CA_CITIES, CO_CITIES, CT_CITIES, DE_CITIES, FL_CITIES, GA_CITIES, HI_CITIES, IL_CITIES, IN_CITIES, KY_CITIES, LA_CITIES, KY_CITIES, MA_CITIES, MO_CITIES, NV_CITIES, NJ_CITIES, NY_CITIES, NC_CITIES, OH_CITIES, OK_CITIES, OR_CITIES, PA_CITIES, TN_CITIES, TX_CITIES, VA_CITIES, WA_CITIES
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def search(request):
    queryset_list = BasicClinic.objects.all()
    if 'States' in request.GET:

        states = request.GET['States']

        elif states == 'MX':

            queryset_list = queryset_list.filter(is_published=True).filter(clinicState__iexact='Mexico').order_by('-digitalTransparencyIndex')

            my_total_count = queryset_list.filter(clinicState__iexact='Mexico')
            my_total_count = my_total_count.filter(is_published=True)

            averageIVFPrice = queryset_list.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
            averageEggPrice = queryset_list.aggregate(average=Avg('egg_donor_recipients_cost'))
            averageEmbryoPrice = queryset_list.aggregate(average=Avg('embryo_donor_recipients_cost'))
            averageSpermPrice = queryset_list.aggregate(average=Avg('sperm_donor_recipients_cost'))
            averageICSIPrice = queryset_list.aggregate(average=Avg('icsi_treatment_cost'))

            if 'Region' in request.GET:
                region = request.GET['Region']

                if region == 'Cancún':
                    queryset_list = queryset_list.filter(clinicCity__iexact='Cancún')

                    my_total_count = my_total_count.filter(clinicCity__iexact='Cancún')
                    my_total_count = my_total_count.count()

                    if 'treatments' in request.GET:
                        treatments = request.GET['treatments']

                        if treatments == 'Alltreatmentstrue':
                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IVFtreatmenttrue':
                            queryset_list = queryset_list.filter(ivf_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IVFtreatmentmildtrue':
                            queryset_list = queryset_list.filter(mild_ivf_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IVFtreatmentovariantrue':
                            queryset_list = queryset_list.filter(ovarian_ivf_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'ICSItreatmenttrue':
                            queryset_list = queryset_list.filter(icsi_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Eggdonationrecipientstrue':
                            queryset_list = queryset_list.filter(egg_donor_recipients=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Spermdonationrecipientstrue':
                            queryset_list = queryset_list.filter(sperm_donor_recipients=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Embryodonationrecipientstrue':
                            queryset_list = queryset_list.filter(embryo_donor_recipients=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'EggFreezingtrue':
                            queryset_list = queryset_list.filter(egg_freezing=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'EmbryoFreezingtrue':
                            queryset_list = queryset_list.filter(embryo_freezing=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'SpermFreezingtrue':
                            queryset_list = queryset_list.filter(sperm_freezing=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Surrogacytrue':
                            queryset_list = queryset_list.filter(surrogacy=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IUItreatmenttrue':
                            queryset_list = queryset_list.filter(iui_treatment=True)
                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Singlewomantreatmenttrue':
                            queryset_list = queryset_list.filter(single_woman_treatment=True)
                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'ReciprocalIVFtrue':
                            queryset_list = queryset_list.filter(reciprocal_treatment=True)
                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        else:
                            order_data = list(queryset_list)

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                    else:
                        order_data = list(queryset_list)

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                elif region == 'Mexico City':
                    queryset_list = queryset_list.filter(clinicCity__iexact='Mexico City')

                    my_total_count = my_total_count.filter(clinicCity__iexact='Mexico City')
                    my_total_count = my_total_count.count()

                    if 'treatments' in request.GET:
                        treatments = request.GET['treatments']

                        if treatments == 'Alltreatmentstrue':
                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IVFtreatmenttrue':
                            queryset_list = queryset_list.filter(ivf_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IVFtreatmentmildtrue':
                            queryset_list = queryset_list.filter(mild_ivf_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IVFtreatmentovariantrue':
                            queryset_list = queryset_list.filter(ovarian_ivf_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'ICSItreatmenttrue':
                            queryset_list = queryset_list.filter(icsi_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Eggdonationrecipientstrue':
                            queryset_list = queryset_list.filter(egg_donor_recipients=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Spermdonationrecipientstrue':
                            queryset_list = queryset_list.filter(sperm_donor_recipients=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Embryodonationrecipientstrue':
                            queryset_list = queryset_list.filter(embryo_donor_recipients=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'EggFreezingtrue':
                            queryset_list = queryset_list.filter(egg_freezing=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'EmbryoFreezingtrue':
                            queryset_list = queryset_list.filter(embryo_freezing=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'SpermFreezingtrue':
                            queryset_list = queryset_list.filter(sperm_freezing=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Surrogacytrue':
                            queryset_list = queryset_list.filter(surrogacy=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IUItreatmenttrue':
                            queryset_list = queryset_list.filter(iui_treatment=True)
                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Singlewomantreatmenttrue':
                            queryset_list = queryset_list.filter(single_woman_treatment=True)
                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'ReciprocalIVFtrue':
                            queryset_list = queryset_list.filter(reciprocal_treatment=True)
                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        else:
                            order_data = list(queryset_list)

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                    else:
                        order_data = list(queryset_list)

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                else:
                    if 'treatments' in request.GET:
                        treatments = request.GET['treatments']

                        if treatments == 'Alltreatmentstrue':
                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IVFtreatmenttrue':
                            queryset_list = queryset_list.filter(ivf_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IVFtreatmentmildtrue':
                            queryset_list = queryset_list.filter(mild_ivf_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IVFtreatmentovariantrue':

                            queryset_list = queryset_list.filter(ovarian_ivf_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'ICSItreatmenttrue':
                            queryset_list = queryset_list.filter(icsi_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Eggdonationrecipientstrue':
                            queryset_list = queryset_list.filter(egg_donor_recipients=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Spermdonationrecipientstrue':
                            queryset_list = queryset_list.filter(sperm_donor_recipients=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Embryodonationrecipientstrue':
                            queryset_list = queryset_list.filter(embryo_donor_recipients=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'EggFreezingtrue':
                            queryset_list = queryset_list.filter(egg_freezing=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'EmbryoFreezingtrue':
                            queryset_list = queryset_list.filter(embryo_freezing=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'SpermFreezingtrue':
                            queryset_list = queryset_list.filter(sperm_freezing=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Surrogacytrue':
                            queryset_list = queryset_list.filter(surrogacy=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IUItreatmenttrue':
                            queryset_list = queryset_list.filter(iui_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'Singlewomantreatmenttrue':
                            queryset_list = queryset_list.filter(single_woman_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        elif treatments == 'ReciprocalIVFtrue':
                            queryset_list = queryset_list.filter(reciprocal_treatment=True)

                            order_data = list(queryset_list)

                            my_total_count = queryset_list.count()

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                        else:
                            order_data = list(queryset_list)

                            paginator = Paginator(order_data, 10)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                            return render(request, 'search/search.html', context)

                    my_total_count = my_total_count.filter(clinicState__iexact='Cyprus')
                    my_total_count = my_total_count.count()

                    order_data = list(queryset_list)


                    paginator = Paginator(order_data, 10)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                    return render(request, 'search/search.html', context)

            else:
                if 'treatments' in request.GET:

                    treatments = request.GET['treatments']
                    if treatments == 'Alltreatmentstrue':
                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'IVFtreatmenttrue':
                        queryset_list = queryset_list.filter(ivf_treatment=True)


                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'IVFtreatmentmildtrue':

                        queryset_list = queryset_list.filter(mild_ivf_treatment=True)


                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'IVFtreatmentovariantrue':
                        queryset_list = queryset_list.filter(ovarian_ivf_treatment=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'ICSItreatmenttrue':
                        queryset_list = queryset_list.filter(icsi_treatment=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'Eggdonationrecipientstrue':
                        queryset_list = queryset_list.filter(egg_donor_recipients=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'Spermdonationrecipientstrue':
                        queryset_list = queryset_list.filter(sperm_donor_recipients=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'Embryodonationrecipientstrue':
                        queryset_list = queryset_list.filter(embryo_donor_recipients=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'EggFreezingtrue':
                        queryset_list = queryset_list.filter(egg_freezing=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'EmbryoFreezingtrue':
                        queryset_list = queryset_list.filter(embryo_freezing=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'SpermFreezingtrue':
                        queryset_list = queryset_list.filter(sperm_freezing=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'Surrogacytrue':
                        queryset_list = queryset_list.filter(surrogacy=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'IUItreatmenttrue':
                        queryset_list = queryset_list.filter(iui_treatment=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'Singlewomantreatmenttrue':
                        queryset_list = queryset_list.filter(single_woman_treatment=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    elif treatments == 'ReciprocalIVFtrue':
                        queryset_list = queryset_list.filter(reciprocal_treatment=True)

                        order_data = list(queryset_list)

                        my_total_count = queryset_list.count()

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)

                    else:
                        order_data = list(queryset_list)

                        paginator = Paginator(order_data, 10)
                        page = request.GET.get('page')
                        paginationing = paginator.get_page(page)

                        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                        return render(request, 'search/search.html', context)
                queryset_list = queryset_list.filter(clinicState__iexact='Mexico')

                order_data = list(queryset_list)

                my_total_count = queryset_list.count()

                paginator = Paginator(order_data, 10)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

                return render(request, 'search/search.html', context)

            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

        else:

            queryset_list = queryset_list.filter(is_published=True).order_by('-digitalTransparencyIndex')

            averageIVFPrice = queryset_list.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
            averageEggPrice = queryset_list.aggregate(average=Avg('egg_donor_recipients_cost'))
            averageEmbryoPrice = queryset_list.aggregate(average=Avg('embryo_donor_recipients_cost'))
            averageSpermPrice = queryset_list.aggregate(average=Avg('sperm_donor_recipients_cost'))
            averageICSIPrice = queryset_list.aggregate(average=Avg('icsi_treatment_cost'))

            order_data = list(queryset_list)

            my_total_count = queryset_list.count()

            paginator = Paginator(order_data, 10)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

            return render(request, 'search/search.html', context)

    else:

        queryset_list = queryset_list.filter(is_published=True).order_by('-digitalTransparencyIndex')

        averageIVFPrice = queryset_list.aggregate(average=Avg('ovarian_ivf_treatment_cost'))
        averageEggPrice = queryset_list.aggregate(average=Avg('egg_donor_recipients_cost'))
        averageEmbryoPrice = queryset_list.aggregate(average=Avg('embryo_donor_recipients_cost'))
        averageSpermPrice = queryset_list.aggregate(average=Avg('sperm_donor_recipients_cost'))
        averageICSIPrice = queryset_list.aggregate(average=Avg('icsi_treatment_cost'))

        order_data = list(queryset_list)

        my_total_count = queryset_list.count()

        paginator = Paginator(order_data, 10)
        page = request.GET.get('page')
        paginationing = paginator.get_page(page)

        context = {'order_data': paginationing, 'paginationing': paginationing, 'averageIVFPrice': averageIVFPrice, 'averageEggPrice': averageEggPrice, 'averageEmbryoPrice': averageEmbryoPrice, 'averageSpermPrice': averageSpermPrice, 'averageICSIPrice': averageICSIPrice,  'CATEGORY_CHOICES_STATES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_EUROPE': CATEGORY_CHOICES_STATES_EUROPE, 'CATEGORY_CHOICES_STATES_ASIA': CATEGORY_CHOICES_STATES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_DE_CITIES': CATEGORY_CHOICES_DE_CITIES, 'CATEGORY_CHOICES_LV_CITIES': CATEGORY_CHOICES_LV_CITIES, 'CATEGORY_CHOICES_PT_CITIES': CATEGORY_CHOICES_PT_CITIES, 'CATEGORY_CHOICES_MX_CITIES': CATEGORY_CHOICES_MX_CITIES, 'my_total_count': my_total_count, 'values': request.GET,}

        return render(request, 'search/search.html', context)
