from django.shortcuts import render
from django.core.paginator import Paginator
from django import template
from clinic.models import BasicClinic
from django.db.models import Avg
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES, CATEGORY_CHOICES_CZ_CITIES, CATEGORY_CHOICES_SP_CITIES, CATEGORY_CHOICES_IN_CITIES, CATEGORY_CHOICES_GR_CITIES, CATEGORY_CHOICES_CY_CITIES
from itertools import chain
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
# ----------------------------------------------------------------------------
def fertilityClinicUSA(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicState__iexact='United States')
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United States').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicState__iexact='United States')
    pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='United States')
    ppq_queryset_list = ppq_queryset_list.filter(clinicState__iexact='United States')

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
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

    return render(request, 'locations-states/USA/fertility-clinic-usa.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicUK(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='United Kingdom').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicState__iexact='United Kingdom')
    pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='United Kingdom')
    ppq_queryset_list = ppq_queryset_list.filter(clinicState__iexact='United Kingdom')

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
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
        'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-states/UK/fertility-clinic-uk.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicSpain(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicState__iexact='Spain')
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Spain').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicState__iexact='Spain')
    pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='Spain')
    ppq_queryset_list = ppq_queryset_list.filter(clinicState__iexact='Spain')

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
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
        'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-states/Spain/fertility-clinic-spain.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicIndia(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicState__iexact='India')
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='India').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicState__iexact='India')
    pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='India')
    ppq_queryset_list = ppq_queryset_list.filter(clinicState__iexact='India')

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
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
        'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-states/India/fertility-clinic-india.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicGreece(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicState__iexact='Greece')
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Greece').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicState__iexact='Greece')
    pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='Greece')
    ppq_queryset_list = ppq_queryset_list.filter(clinicState__iexact='Greece')

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
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
        'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-states/Greece/fertility-clinic-greece.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicCzech(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicState__iexact='Czech Republic')
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Czech Republic').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicState__iexact='Czech Republic')
    pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='Czech Republic')
    ppq_queryset_list = ppq_queryset_list.filter(clinicState__iexact='Czech Republic')

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
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
        'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-states/CZ/fertility-clinic-czech-republic.html', context)

# ----------------------------------------------------------------------------
def fertilityClinicCyprus(request):
    queryset_list = BasicClinic.objects.all()
    queryset_list = queryset_list.filter(is_published=True).exclude(pro_is_published=True).exclude(ppq_is_published=True)

    pro_queryset_list = BasicClinic.objects.all()
    pro_queryset_list = pro_queryset_list.filter(pro_is_published=True).exclude(ppq_is_published=True)

    ppq_queryset_list = BasicClinic.objects.all()
    ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

    my_total_count = BasicClinic.objects.filter(clinicState__iexact='Cyprus')
    my_total_count = my_total_count.filter(is_published=True)

    averageIVFPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('ovarian_ivf_treatment_cost'))
    averageEggPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('egg_donor_recipients_cost'))
    averageEmbryoPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('embryo_donor_recipients_cost'))
    averageSpermPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('sperm_donor_recipients_cost'))
    averageICSIPrice = BasicClinic.objects.filter(clinicState__iexact='Cyprus').aggregate(average=Avg('icsi_treatment_cost'))

    queryset_list = queryset_list.filter(clinicState__iexact='Cyprus')
    pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='Cyprus')
    ppq_queryset_list = ppq_queryset_list.filter(clinicState__iexact='Cyprus')

    queryset_list = queryset_list.order_by('?')
    pro_queryset_list = pro_queryset_list.order_by('?')
    ppq_queryset_list = ppq_queryset_list.order_by('?')

    order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

    my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

    paginator = Paginator(order_data, 30)
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
        'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES,
        'my_total_count': my_total_count,
        }

    return render(request, 'locations-states/Cyprus/fertility-clinic-cyprus.html', context)
