from django.shortcuts import render
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from .choices import CATEGORY_CHOICES_STATES
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def search(request):
    if 'States' in request.GET:

        states = request.GET['States']

        if states == 'UK':

            queryset_list = BasicClinic.objects.all()
            queryset_list = queryset_list.filter(is_published=True)
            queryset_list = queryset_list.filter(pro_is_published=False)
            queryset_list = queryset_list.filter(clinicState__iexact='United Kingdom')

            pro_listings = BasicClinic.objects.all()

            pro_queryset_list = BasicClinic.objects.order_by('?')
            pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)
            pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='United Kingdom')

            my_total_count = BasicClinic.objects.all()
            my_total_count = my_total_count.filter(is_published=True)
            my_total_count = my_total_count.filter(clinicState__iexact='United Kingdom')
            my_total_count = my_total_count.count()

            averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
            averageIVFPrice = averageIVFPrice.filter(is_published=True).aggregate(average=Avg('ivf_treatment_cost'))

            averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
            averageEggPrice = averageEggPrice.filter(is_published=True).aggregate(average=Avg('egg_donor_recipients_cost'))

            averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
            averageEmbryoPrice = averageEmbryoPrice.filter(is_published=True).aggregate(average=Avg('embryo_donor_recipients_cost'))

            averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
            averageSpermPrice = averageSpermPrice.filter(is_published=True).aggregate(average=Avg('sperm_donor_recipients_cost'))

            averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
            averageICSIPrice = averageICSIPrice.filter(is_published=True).aggregate(average=Avg('icsi_treatment_cost'))

            if 'treatments' in request.GET:

                treatments = request.GET['treatments']

                if treatments == 'Alltreatmentstrue':
                    order_data = list(pro_queryset_list) + list(queryset_list)

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'IVFtreatmenttrue':

                    queryset_list = queryset_list.filter(ivf_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(ivf_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'ICSItreatmenttrue':
                    pro_queryset_list = pro_queryset_list.filter(icsi_treatment=True)
                    queryset_list = queryset_list.filter(icsi_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Eggdonationrecipientstrue':

                    queryset_list = queryset_list.filter(egg_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(egg_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Spermdonationrecipientstrue':

                    queryset_list = queryset_list.filter(sperm_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(sperm_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Embryodonationrecipientstrue':

                    queryset_list = queryset_list.filter(embryo_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(embryo_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Fertilitypreservationtrue':

                    queryset_list = queryset_list.filter(fertility_preservation=True)
                    pro_queryset_list = pro_queryset_list.filter(fertility_preservation=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Surrogacytrue':

                    queryset_list = queryset_list.filter(surrogacy=True)
                    pro_queryset_list = pro_queryset_list.filter(surrogacy=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'IUItreatmenttrue':

                    queryset_list = queryset_list.filter(iui_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(iui_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Singlewomantreatmenttrue':

                    queryset_list = queryset_list.filter(single_woman_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(single_woman_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'ReciprocalIVFtrue':

                    queryset_list = queryset_list.filter(reciprocal_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(reciprocal_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                else:
                    order_data = list(pro_queryset_list) + list(queryset_list)

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                return render(request, 'search/search.html', context)

            else:
                order_data = list(pro_queryset_list) + list(queryset_list)

                paginator = Paginator(order_data, 12)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {
                    'listings': queryset_list,
                    'pro_listings': pro_queryset_list,
                    'order_data': paginationing,
                    'paginationing': paginationing,
                    'averageIVFPrice': averageIVFPrice,
                    'averageEggPrice': averageEggPrice,
                    'averageEmbryoPrice': averageEmbryoPrice,
                    'averageSpermPrice': averageSpermPrice,
                    'averageICSIPrice': averageICSIPrice,
                    'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                    'my_total_count': my_total_count,
                    'values': request.GET,
                    }

            return render(request, 'search/search.html', context)

        elif states == 'US':

            queryset_list = BasicClinic.objects.all()
            queryset_list = queryset_list.filter(is_published=True)
            queryset_list = queryset_list.filter(pro_is_published=False)
            queryset_list = queryset_list.filter(clinicState__iexact='United States')

            pro_listings = BasicClinic.objects.all()

            pro_queryset_list = BasicClinic.objects.order_by('?')
            pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)
            pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='United States')

            my_total_count = BasicClinic.objects.all()
            my_total_count = my_total_count.filter(is_published=True)
            my_total_count = my_total_count.filter(clinicState__iexact='United States')
            my_total_count = my_total_count.count()

            averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
            averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
            averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
            averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
            averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))

            if 'treatments' in request.GET:

                treatments = request.GET['treatments']

                if treatments == 'Alltreatmentstrue':
                    order_data = list(pro_queryset_list) + list(queryset_list)

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'IVFtreatmenttrue':
                    queryset_list = queryset_list.filter(ivf_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(ivf_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'ICSItreatmenttrue':
                    queryset_list = queryset_list.filter(icsi_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(icsi_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Eggdonationrecipientstrue':
                    queryset_list = queryset_list.filter(egg_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(egg_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Spermdonationrecipientstrue':
                    queryset_list = queryset_list.filter(sperm_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(sperm_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Embryodonationrecipientstrue':
                    queryset_list = queryset_list.filter(embryo_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(embryo_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Fertilitypreservationtrue':
                    queryset_list = queryset_list.filter(fertility_preservation=True)
                    pro_queryset_list = pro_queryset_list.filter(fertility_preservation=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Surrogacytrue':
                    queryset_list = queryset_list.filter(surrogacy=True)
                    pro_queryset_list = pro_queryset_list.filter(surrogacy=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'IUItreatmenttrue':
                    queryset_list = queryset_list.filter(iui_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(iui_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Singlewomantreatmenttrue':
                    queryset_list = queryset_list.filter(single_woman_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(single_woman_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'ReciprocalIVFtrue':
                    queryset_list = queryset_list.filter(reciprocal_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(reciprocal_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                else:
                    order_data = list(pro_queryset_list) + list(queryset_list)

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                return render(request, 'search/search.html', context)

            else:
                order_data = list(pro_queryset_list) + list(queryset_list)

                paginator = Paginator(order_data, 12)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {
                    'listings': queryset_list,
                    'pro_listings': pro_queryset_list,
                    'order_data': paginationing,
                    'paginationing': paginationing,
                    'averageIVFPrice': averageIVFPrice,
                    'averageEggPrice': averageEggPrice,
                    'averageEmbryoPrice': averageEmbryoPrice,
                    'averageSpermPrice': averageSpermPrice,
                    'averageICSIPrice': averageICSIPrice,
                    'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                    'my_total_count': my_total_count,
                    'values': request.GET,
                    }

            return render(request, 'search/search.html', context)

        elif states == 'CZ':

            queryset_list = BasicClinic.objects.order_by('?')
            queryset_list = queryset_list.filter(is_published=True)
            queryset_list = queryset_list.filter(pro_is_published=False)
            queryset_list = queryset_list.filter(clinicState__iexact='Czech Republic')

            pro_listings = BasicClinic.objects.all()

            pro_queryset_list = BasicClinic.objects.order_by('?')
            pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)
            pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='Czech Republic')

            my_total_count = BasicClinic.objects.all()
            my_total_count = my_total_count.filter(is_published=True)
            my_total_count = my_total_count.filter(clinicState__iexact='Czech Republic')
            my_total_count = my_total_count.count()

            averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('ivf_treatment_cost'))
            averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('egg_donor_recipients_cost'))
            averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('embryo_donor_recipients_cost'))
            averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('sperm_donor_recipients_cost'))
            averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('icsi_treatment_cost'))


            if 'treatments' in request.GET:

                treatments = request.GET['treatments']

                if treatments == 'Alltreatmentstrue':
                    order_data = list(pro_queryset_list) + list(queryset_list)

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'IVFtreatmenttrue':
                    queryset_list = queryset_list.filter(ivf_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(ivf_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'ICSItreatmenttrue':
                    queryset_list = queryset_list.filter(icsi_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(icsi_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Eggdonationrecipientstrue':
                    queryset_list = queryset_list.filter(egg_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(egg_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Spermdonationrecipientstrue':
                    queryset_list = queryset_list.filter(sperm_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(sperm_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Embryodonationrecipientstrue':
                    queryset_list = queryset_list.filter(embryo_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(embryo_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Fertilitypreservationtrue':
                    queryset_list = queryset_list.filter(fertility_preservation=True)
                    pro_queryset_list = pro_queryset_list.filter(fertility_preservation=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Surrogacytrue':
                    queryset_list = queryset_list.filter(surrogacy=True)
                    pro_queryset_list = pro_queryset_list.filter(surrogacy=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'IUItreatmenttrue':
                    queryset_list = queryset_list.filter(iui_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(iui_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Singlewomantreatmenttrue':
                    queryset_list = queryset_list.filter(single_woman_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(single_woman_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'ReciprocalIVFtrue':
                    queryset_list = queryset_list.filter(reciprocal_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(reciprocal_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                else:
                    order_data = list(pro_queryset_list) + list(queryset_list)

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'averageIVFPrice': averageIVFPrice,
                        'averageEggPrice': averageEggPrice,
                        'averageEmbryoPrice': averageEmbryoPrice,
                        'averageSpermPrice': averageSpermPrice,
                        'averageICSIPrice': averageICSIPrice,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                return render(request, 'search/search.html', context)

            else:
                order_data = list(pro_queryset_list) + list(queryset_list)

                paginator = Paginator(order_data, 12)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {
                    'listings': queryset_list,
                    'pro_listings': pro_queryset_list,
                    'order_data': paginationing,
                    'paginationing': paginationing,
                    'averageIVFPrice': averageIVFPrice,
                    'averageEggPrice': averageEggPrice,
                    'averageEmbryoPrice': averageEmbryoPrice,
                    'averageSpermPrice': averageSpermPrice,
                    'averageICSIPrice': averageICSIPrice,
                    'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                    'my_total_count': my_total_count,
                    'values': request.GET,
                    }

            return render(request, 'search/search.html', context)

        else:
            queryset_list = BasicClinic.objects.all()
            queryset_list = queryset_list.filter(is_published=True)
            queryset_list = queryset_list.filter(pro_is_published=False)

            my_total_count = BasicClinic.objects.all()
            my_total_count = my_total_count.filter(is_published=True)
            my_total_count = my_total_count.count()

            pro_listings = BasicClinic.objects.all()

            pro_queryset_list = BasicClinic.objects.order_by('?')
            pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

            if 'treatments' in request.GET:

                treatments = request.GET['treatments']

                if treatments == 'Alltreatmentstrue':
                    order_data = list(pro_queryset_list) + list(queryset_list)

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'IVFtreatmenttrue':
                    queryset_list = queryset_list.filter(ivf_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(ivf_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'ICSItreatmenttrue':
                    queryset_list = queryset_list.filter(icsi_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(icsi_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Eggdonationrecipientstrue':
                    queryset_list = queryset_list.filter(egg_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(egg_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Spermdonationrecipientstrue':
                    queryset_list = queryset_list.filter(sperm_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(sperm_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Embryodonationrecipientstrue':
                    queryset_list = queryset_list.filter(embryo_donor_recipients=True)
                    pro_queryset_list = pro_queryset_list.filter(embryo_donor_recipients=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Fertilitypreservationtrue':
                    queryset_list = queryset_list.filter(fertility_preservation=True)
                    pro_queryset_list = pro_queryset_list.filter(fertility_preservation=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'Surrogacytrue':
                    queryset_list = queryset_list.filter(surrogacy=True)
                    pro_queryset_list = pro_queryset_list.filter(surrogacy=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'IUItreatmenttrue':
                    queryset_list = queryset_list.filter(iui_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(iui_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }
                    return render(request, 'search/search.html', context)

                elif treatments == 'Singlewomantreatmenttrue':
                    queryset_list = queryset_list.filter(single_woman_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(single_woman_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                elif treatments == 'ReciprocalIVFtrue':
                    queryset_list = queryset_list.filter(reciprocal_treatment=True)
                    pro_queryset_list = pro_queryset_list.filter(reciprocal_treatment=True)
                    order_data = list(pro_queryset_list) + list(queryset_list)
                    my_total_count = queryset_list.count() + pro_queryset_list.count()

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                    return render(request, 'search/search.html', context)

                else:
                    order_data = list(pro_queryset_list) + list(queryset_list)

                    paginator = Paginator(order_data, 12)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'listings': queryset_list,
                        'pro_listings': pro_queryset_list,
                        'order_data': paginationing,
                        'paginationing': paginationing,
                        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                        'my_total_count': my_total_count,
                        'values': request.GET,
                        }

                return render(request, 'search/search.html', context)

    else:
        context = {
            'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
            }

        return render(request, 'search/search.html', context)
