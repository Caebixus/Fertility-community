from django.shortcuts import render
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from search.choices import CATEGORY_CHOICES_STATES
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.

def fertilityClinicLondon(request):
    listings = BasicClinic.objects.all()

    queryset_list = BasicClinic.objects.order_by('?')
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)
    queryset_list = queryset_list.filter(clinicCity__iexact='London')

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='London')


    averageIVFPrice = BasicClinic.objects.filter(clinicCity__iexact='London').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicCity__iexact='London').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicCity__iexact='London').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicCity__iexact='London').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicCity__iexact='London').aggregate(average=Avg('icsi_treatment_cost'))

    context = {
        'listings': queryset_list,
        'pro_listings': pro_queryset_list,
        'averageIVFPrice': averageIVFPrice,
        'averageEggPrice': averageEggPrice,
        'averageEmbryoPrice': averageEmbryoPrice,
        'averageSpermPrice': averageSpermPrice,
        'averageICSIPrice': averageICSIPrice,
    }

    return render(request, 'locations-cities/UK/fertility-clinic-london.html', context)

def fertilityClinicManchester(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)
    queryset_list = queryset_list.filter(clinicCity__iexact='London')

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)
    pro_queryset_list = pro_queryset_list.filter(clinicCity__iexact='London')

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)
    my_total_count = my_total_count.filter(clinicCity__iexact='London')
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

    return render(request, 'locations-cities/UK/fertility-clinic-manchester.html', context)
