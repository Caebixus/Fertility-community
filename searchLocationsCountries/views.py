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

    #SP CITIES
    texasclinics = BasicClinic.objects.filter(clinicRegion__iexact='Texas').exclude(is_published=False)
    texasclinics = texasclinics.count()

    newyorkclinics = BasicClinic.objects.filter(clinicRegion__iexact='New York').exclude(is_published=False)
    newyorkclinics = newyorkclinics.count()

    floridaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Florida').exclude(is_published=False)
    floridaclinics = floridaclinics.count()

    newjerseyclinics = BasicClinic.objects.filter(clinicRegion__iexact='New Jersey').exclude(is_published=False)
    newjerseyclinics = newjerseyclinics.count()

    illinoisclinics = BasicClinic.objects.filter(clinicRegion__iexact='Illinois').exclude(is_published=False)
    illinoisclinics = illinoisclinics.count()

    pennsylvaniaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Pennsylvania').exclude(is_published=False)
    pennsylvaniaclinics = pennsylvaniaclinics.count()

    michiganclinics = BasicClinic.objects.filter(clinicRegion__iexact='Michigan').exclude(is_published=False)
    michiganclinics = michiganclinics.count()

    georgiaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Georgia').exclude(is_published=False)
    georgiaclinics = georgiaclinics.count()

    arizonaclinics = BasicClinic.objects.filter(clinicRegion__iexact='Arizona').exclude(is_published=False)
    arizonaclinics = arizonaclinics.count()

    massachusettsclinics = BasicClinic.objects.filter(clinicRegion__iexact='Massachusetts').exclude(is_published=False)
    massachusettsclinics = massachusettsclinics.count()

    washingtonclinics = BasicClinic.objects.filter(clinicRegion__iexact='Washington').exclude(is_published=False)
    washingtonclinics = washingtonclinics.count()

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
        'texasclinics': texasclinics,
        'newyorkclinics': newyorkclinics,
        'floridaclinics': floridaclinics,
        'newjerseyclinics': newjerseyclinics,
        'illinoisclinics': illinoisclinics,
        'pennsylvaniaclinics': pennsylvaniaclinics,
        'michiganclinics': michiganclinics,
        'georgiaclinics': georgiaclinics,
        'arizonaclinics': arizonaclinics,
        'massachusettsclinics': massachusettsclinics,
        'washingtonclinics': washingtonclinics,
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

    #UK CITIES
    londonclinics = BasicClinic.objects.filter(clinicCity__iexact='London').exclude(is_published=False)
    londonclinics = londonclinics.count()

    bristolclinics = BasicClinic.objects.filter(clinicCity__iexact='Bristol').exclude(is_published=False)
    bristolclinics = bristolclinics.count()

    leedsclinics = BasicClinic.objects.filter(clinicCity__iexact='Leeds').exclude(is_published=False)
    leedsclinics = leedsclinics.count()

    nottinghamclinics = BasicClinic.objects.filter(clinicCity__iexact='Nottingham').exclude(is_published=False)
    nottinghamclinics = nottinghamclinics.count()

    birminghamclinics = BasicClinic.objects.filter(clinicCity__iexact='Birmingham').exclude(is_published=False)
    birminghamclinics = birminghamclinics.count()

    exeterclinics = BasicClinic.objects.filter(clinicCity__iexact='Exeter').exclude(is_published=False)
    exeterclinics = exeterclinics.count()

    liverpoolclinics = BasicClinic.objects.filter(clinicCity__iexact='Liverpool').exclude(is_published=False)
    liverpoolclinics = liverpoolclinics.count()

    portsmouthclinics = BasicClinic.objects.filter(clinicCity__iexact='Portsmouth').exclude(is_published=False)
    portsmouthclinics = portsmouthclinics.count()

    bournemouthclinics = BasicClinic.objects.filter(clinicCity__iexact='Bournemouth').exclude(is_published=False)
    bournemouthclinics = bournemouthclinics.count()

    glasgowclinics = BasicClinic.objects.filter(clinicCity__iexact='Glasgow').exclude(is_published=False)
    glasgowclinics = glasgowclinics.count()

    manchesterclinics = BasicClinic.objects.filter(clinicCity__iexact='Manchester').exclude(is_published=False)
    manchesterclinics = manchesterclinics.count()

    sheffieldclinics = BasicClinic.objects.filter(clinicCity__iexact='Sheffield').exclude(is_published=False)
    sheffieldclinics = sheffieldclinics.count()

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
        'londonclinics': londonclinics,
        'bristolclinics': bristolclinics,
        'leedsclinics': leedsclinics,
        'nottinghamclinics': nottinghamclinics,
        'birminghamclinics': birminghamclinics,
        'exeterclinics': exeterclinics,
        'liverpoolclinics': liverpoolclinics,
        'portsmouthclinics': portsmouthclinics,
        'bournemouthclinics': bournemouthclinics,
        'glasgowclinics': glasgowclinics,
        'manchesterclinics': manchesterclinics,
        'sheffieldclinics': sheffieldclinics,
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

    #SP CITIES
    alicanteclinics = BasicClinic.objects.filter(clinicCity__iexact='Alicante').exclude(is_published=False)
    alicanteclinics = alicanteclinics.count()

    barcelonaclinics = BasicClinic.objects.filter(clinicCity__iexact='Barcelona').exclude(is_published=False)
    barcelonaclinics = barcelonaclinics.count()

    madridclinics = BasicClinic.objects.filter(clinicCity__iexact='Madrid').exclude(is_published=False)
    madridclinics = madridclinics.count()

    malagaclinics = BasicClinic.objects.filter(clinicCity__iexact='Malaga').exclude(is_published=False)
    malagaclinics = malagaclinics.count()

    sevilleclinics = BasicClinic.objects.filter(clinicCity__iexact='Seville').exclude(is_published=False)
    sevilleclinics = sevilleclinics.count()

    valenciaclinics = BasicClinic.objects.filter(clinicCity__iexact='Valencia').exclude(is_published=False)
    valenciaclinics = valenciaclinics.count()

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
        'alicanteclinics': alicanteclinics,
        'barcelonaclinics': barcelonaclinics,
        'madridclinics': madridclinics,
        'malagaclinics': malagaclinics,
        'sevilleclinics': sevilleclinics,
        'valenciaclinics': valenciaclinics,
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

    #IN CITIES
    hyderabadclinics = BasicClinic.objects.filter(clinicCity__iexact='Hyderabad').exclude(is_published=False)
    hyderabadclinics = hyderabadclinics.count()

    newdelhiclinics = BasicClinic.objects.filter(clinicCity__iexact='New Delhi').exclude(is_published=False)
    newdelhiclinics = newdelhiclinics.count()

    gachibowliclinics = BasicClinic.objects.filter(clinicCity__iexact='Gachibowli').exclude(is_published=False)
    gachibowliclinics = gachibowliclinics.count()

    bangaloreclinics = BasicClinic.objects.filter(clinicCity__iexact='Bangalore').exclude(is_published=False)
    bangaloreclinics = bangaloreclinics.count()

    chennaiclinics = BasicClinic.objects.filter(clinicCity__iexact='Chennai').exclude(is_published=False)
    chennaiclinics = chennaiclinics.count()

    vandodaraclinics = BasicClinic.objects.filter(clinicCity__iexact='Vandodara').exclude(is_published=False)
    vandodaraclinics = vandodaraclinics.count()

    madhapurclinics = BasicClinic.objects.filter(clinicCity__iexact='Madhapur').exclude(is_published=False)
    madhapurclinics = madhapurclinics.count()

    gwaliorclinics = BasicClinic.objects.filter(clinicCity__iexact='Gwalior').exclude(is_published=False)
    gwaliorclinics = gwaliorclinics.count()

    mumbaiclinics = BasicClinic.objects.filter(clinicCity__iexact='Mumbai').exclude(is_published=False)
    mumbaiclinics = mumbaiclinics.count()

    faridabadclinics = BasicClinic.objects.filter(clinicCity__iexact='Faridabad').exclude(is_published=False)
    faridabadclinics = faridabadclinics.count()

    kolkataclinics = BasicClinic.objects.filter(clinicCity__iexact='Kolkata').exclude(is_published=False)
    kolkataclinics = kolkataclinics.count()

    rohtakclinics = BasicClinic.objects.filter(clinicCity__iexact='Rohtak').exclude(is_published=False)
    rohtakclinics = rohtakclinics.count()   

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
        'hyderabadclinics': hyderabadclinics,
        'newdelhiclinics': newdelhiclinics,
        'gachibowliclinics': gachibowliclinics,
        'bangaloreclinics': bangaloreclinics,
        'chennaiclinics': chennaiclinics,
        'vandodaraclinics': vandodaraclinics,
        'madhapurclinics': madhapurclinics,
        'gwaliorclinics': gwaliorclinics,
        'mumbaiclinics': mumbaiclinics,
        'faridabadclinics': faridabadclinics,
        'kolkataclinics': kolkataclinics,
        'rohtakclinics': rohtakclinics,
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

    #GR CITIES
    athensclinics = BasicClinic.objects.filter(clinicCity__iexact='Athens').exclude(is_published=False)
    athensclinics = athensclinics.count()

    thessalonikiclinics = BasicClinic.objects.filter(clinicCity__iexact='Thessaloniki').exclude(is_published=False)
    thessalonikiclinics = thessalonikiclinics.count()

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
        'athensclinics': athensclinics,
        'thessalonikiclinics': thessalonikiclinics,
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

    #CZ CITIES
    pragueclinics = BasicClinic.objects.filter(clinicCity__iexact='Prague').exclude(is_published=False)
    pragueclinics = pragueclinics.count()

    brnoclinics = BasicClinic.objects.filter(clinicCity__iexact='Brno').exclude(is_published=False)
    brnoclinics = brnoclinics.count()

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
        'pragueclinics': pragueclinics,
        'brnoclinics': brnoclinics,
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

    #CY CITIES
    girneclinics = BasicClinic.objects.filter(clinicCity__iexact='Girne').exclude(is_published=False)
    girneclinics = girneclinics.count()

    nicosiaclinics = BasicClinic.objects.filter(clinicCity__iexact='Nicosia').exclude(is_published=False)
    nicosiaclinics = nicosiaclinics.count()

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
        'nicosiaclinics': nicosiaclinics,
        }

    return render(request, 'locations-states/Cyprus/fertility-clinic-cyprus.html', context)
