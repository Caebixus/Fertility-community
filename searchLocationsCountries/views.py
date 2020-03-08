from django.shortcuts import render
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from search.choices import CATEGORY_CHOICES_STATES

# Create your views here.

def fertilityClinicuk(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)
    queryset_list = queryset_list.filter(clinicState__iexact='United Kingdom')

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)
    pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='United Kingdom')

    order_data = list(pro_queryset_list) + list(queryset_list)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)
    my_total_count = my_total_count.filter(clinicState__iexact='United Kingdom')
    my_total_count = my_total_count.count()

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

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

    return render(request, 'locations-states/UK/fertility-clinic-uk.html', context)
