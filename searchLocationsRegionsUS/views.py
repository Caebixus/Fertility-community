from django.shortcuts import render
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# ----------------------------------------------------------------------------
def fertilityClinicsAlabama(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Alabama')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Alabama')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Alabama')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-alabama.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsAlaska(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Alaska')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Alaska')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Alaska')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-alaska.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsArizona(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Arizona')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Arizona')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Arizona')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-arizona.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsArkansas(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Arkansas')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Arkansas')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Arkansas')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-arkansas.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsCalifornia(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='California')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='California')
    my_total_count = my_total_count.filter(clinicRegion__iexact='California')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

# ----------------------------------------------------------------------------
def fertilityClinicsColorado(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Colorado')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Colorado')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Colorado')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-colorado.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsConnecticut(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Connecticut')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Connecticut')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Connecticut')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-connecticut.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsDelaware(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Delaware')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Delaware')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Delaware')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-delaware.html', context)

    # ----------------------------------------------------------------------------
def fertilityClinicsFlorida(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Florida')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Florida')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Florida')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-florida.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsGeorgia(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Georgia')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Georgia')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Georgia')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-georgia.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsHawaii(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Hawaii')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Hawaii')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Hawaii')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-hawaii.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsIdaho(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Idaho')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Idaho')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Idaho')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-idaho.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsIllinois(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Illinois')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Illinois')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Illinois')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-illinois.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsIndiana(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Indiana')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Indiana')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Indiana')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-indiana.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsIowa(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Iowa')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Iowa')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Iowa')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-iowa.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsKansas(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Kansas')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Kansas')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Kansas')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-kansas.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsKentucky(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Kentucky')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Kentucky')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Kentucky')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-kentucky.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsLouisiana(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Louisiana')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Louisiana')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Louisiana')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-louisiana.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMaine(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Maine')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Maine')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Maine')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-maine.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMaryland(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Maryland')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Maryland')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Maryland')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-maryland.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMassachusetts(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Massachusetts')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Massachusetts')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Massachusetts')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-massachusetts.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMichigan(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Michigan')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Michigan')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Michigan')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-michigan.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMinnesota(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Minnesota')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Minnesota')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Minnesota')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-minnesota.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMississippi(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Mississippi')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Mississippi')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Mississippi')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-mississippi.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMissouri(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Missouri')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Missouri')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Missouri')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-missouri.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsMontana(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Montana')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Montana')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Montana')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-montana.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNebraska(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Nebraska')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Nebraska')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Nebraska')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-nebraska.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNewHampshire(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='New Hampshire')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='New Hampshire')
    my_total_count = my_total_count.filter(clinicRegion__iexact='New Hampshire')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-new-hampshire.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNewJersey(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='New Jersey')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='New Jersey')
    my_total_count = my_total_count.filter(clinicRegion__iexact='New Jersey')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-new-jersey.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNewMexico(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='New Mexico')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='New Mexico')
    my_total_count = my_total_count.filter(clinicRegion__iexact='New Mexico')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-new-mexico.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNewYork(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='New York')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='New York')
    my_total_count = my_total_count.filter(clinicRegion__iexact='New York')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-new-york.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNorthCarolina(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='North Carolina')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='North Carolina')
    my_total_count = my_total_count.filter(clinicRegion__iexact='North Carolina')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-north-carolina.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNorthDakota(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='North Dakota')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='North Dakota')
    my_total_count = my_total_count.filter(clinicRegion__iexact='North Dakota')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-north-dakota.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsNevada(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Nevada')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Nevada')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Nevada')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-nevada.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsOhio(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Ohio')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Ohio')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Ohio')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-ohio.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsOklahoma(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Oklahoma')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Oklahoma')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Oklahoma')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-oklahoma.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsOregon(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Oregon')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Oregon')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Oregon')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-oregon.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsPennsylvania(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Pennsylvania')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Pennsylvania')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Pennsylvania')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-pennsylvania.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsPuertoRico(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Puerto Rico')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Puerto Rico')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Puerto Rico')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-puerto-rico.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsRhodeIsland(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Rhode Island')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Rhode Island')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Rhode Island')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-rhode-island.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsSouthCarolina(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='South Carolina')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='South Carolina')
    my_total_count = my_total_count.filter(clinicRegion__iexact='South Carolina')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-south-carolina.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsSouthDakota(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='South Dakota')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='South Dakota')
    my_total_count = my_total_count.filter(clinicRegion__iexact='South Dakota')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-south-dakota.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsTennessee(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Tennessee')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Tennessee')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Tennessee')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-tennessee.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsTexas(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Texas')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Texas')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Texas')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-texas.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsUtah(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Utah')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Utah')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Utah')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-utah.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsVermont(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Vermont')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Vermont')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Vermont')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-vermont.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsVirginia(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Virginia')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Virginia')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Virginia')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-virginia.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsWashington(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Washington')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Washington')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Washington')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-washington.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsWestVirginia(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Virginia')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Virginia')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Virginia')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-virginia.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsWisconsin(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Wisconsin')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Wisconsin')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Wisconsin')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-wisconsin.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsWyoming(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='Wyoming')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Wyoming')
    my_total_count = my_total_count.filter(clinicRegion__iexact='Wyoming')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-wyoming.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicsDistrictOfColumbia(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True)
    queryset_list = queryset_list.filter(pro_is_published=False)

    pro_listings = BasicClinic.objects.all()

    pro_queryset_list = BasicClinic.objects.order_by('?')
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)

    my_total_count = BasicClinic.objects.all()
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))


    queryset_list = queryset_list.filter(clinicRegion__iexact='DistrictOfColumbia')
    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='DistrictOfColumbia')
    my_total_count = my_total_count.filter(clinicRegion__iexact='DistrictOfColumbia')
    my_total_count = my_total_count.count()

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')

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

    return render(request, 'locations-regions-US/fertility-clinics-district-of-columbia.html', context)
