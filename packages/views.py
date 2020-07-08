from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION
from .choices import CATEGORY_PACKAGE
from django import template
from contact.forms import WebsiteForm
from django.core.mail import send_mail
from django.contrib import messages, auth
from clinic.models import BasicClinic
from .models import Packages


def packages(request):
    listing = Packages.objects.all()

    context = {
        'listing': listing,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_PACKAGE': CATEGORY_PACKAGE,
        'values': request.GET,
    }

    return render(request, 'packages/packages.html', context)

def searchpackages(request):
    if 'States' in request.GET:
        states = request.GET['States']

        if states == 'US':
            pro_queryset_list = Packages.objects.all()
            pro_queryset_list = pro_queryset_list.filter(pro_is_published=True)
            pro_queryset_list = pro_queryset_list.filter(ppq_is_published=False)

            ppq_queryset_list = Packages.objects.all()
            ppq_queryset_list = ppq_queryset_list.filter(pro_is_published=True)
            ppq_queryset_list = ppq_queryset_list.filter(ppq_is_published=True)

            my_total_count = Packages.objects.all()
            my_total_count = my_total_count.filter(pro_is_published=True)

            if 'Region' in request.GET:
                region = request.GET['Region']

                pro_queryset_list = pro_queryset_list.filter(clinicState__iexact='United States')
                ppq_queryset_list = ppq_queryset_list.filter(clinicState__iexact='United States')

                if region == 'AL':
                    pro_queryset_list = pro_queryset_list.filter(clinicRegion__iexact='Alabama')
                    ppq_queryset_list = ppq_queryset_list.filter(clinicRegion__iexact='Alabama')

                    my_total_count = my_total_count.filter(clinicRegion__iexact='Alabama')
                    my_total_count = my_total_count.count()

                    pro_queryset_list = pro_queryset_list.order_by('?')
                    ppq_queryset_list = ppq_queryset_list.order_by('?')

                    if 'treatments' in request.GET:
                        treatments = request.GET['treatments']

                        if treatments == 'Alltreatmentstrue':

                            order_data = list(ppq_queryset_list) + list(pro_queryset_list)

                            my_total_count = pro_queryset_list.count() + ppq_queryset_list.count()

                            paginator = Paginator(order_data, 12)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {
                                'listing': queryset_list,
                                'pro_listings': pro_queryset_list,
                                'order_data': paginationing,
                                'paginationing': paginationing,
                                'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                                'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
                                'CATEGORY_PACKAGE': CATEGORY_PACKAGE,
                                'my_total_count': my_total_count,
                                'values': request.GET,
                                }

                            return render(request, 'search/search.html', context)

                        elif treatments == 'IVFtreatmenttrue':

                            queryset_list = queryset_list.filter(ivf_treatment=True)
                            pro_queryset_list = pro_queryset_list.filter(ivf_treatment=True)
                            order_data = list(ppq_queryset_list) + list(pro_queryset_list) + list(queryset_list)

                            my_total_count = queryset_list.count() + pro_queryset_list.count() + ppq_queryset_list.count()

                            paginator = Paginator(order_data, 12)
                            page = request.GET.get('page')
                            paginationing = paginator.get_page(page)

                            context = {
                                'listing': queryset_list,
                                'pro_listings': pro_queryset_list,
                                'order_data': paginationing,
                                'paginationing': paginationing,
                                'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
                                'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
                                'CATEGORY_PACKAGE': CATEGORY_PACKAGE,
                                'my_total_count': my_total_count,
                                'values': request.GET,
                                }

                            return render(request, 'search/search.html', context)


    context = {
        'listing': listing,
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES,
        'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION,
        'CATEGORY_PACKAGE': CATEGORY_PACKAGE,
        'values': request.GET,
    }

    return render(request, 'packages/searching.html', context)
