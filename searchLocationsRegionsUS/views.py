from django.shortcuts import render
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def fertilityClinicsCalifornia(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicRegion__iexact='California').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicRegion__iexact='California').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicRegion__iexact='California').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicRegion__iexact='California').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicRegion__iexact='California').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='California')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='California')
    my_total_count = my_total_count.filter(clinicRegion__iexact='California')
    my_total_count = my_total_count.count()

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
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-regions-US/fertility-clinics-california.html', context)
