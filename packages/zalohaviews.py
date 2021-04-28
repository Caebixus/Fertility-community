from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION
from location.currencies import gbpToEur, gbpToUsd, gbpToInr, usdToGbp, usdToEur, usdToInr, eurToGbp, eurToUsd, eurToInr, inrToGbp, inrToEur, inrToUsd
from .choices import CATEGORY_PACKAGE
from django import template
from contact.forms import WebsiteForm
from django.core.mail import send_mail
from django.contrib import messages, auth
from clinic.models import BasicClinic
from .models import Package
from datetime import datetime, timedelta
from django.utils import timezone
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_MX_CITIES, CATEGORY_CHOICES_UK_CITIES, CATEGORY_CHOICES_CZ_CITIES, CATEGORY_CHOICES_SP_CITIES, CATEGORY_CHOICES_IN_CITIES, CATEGORY_CHOICES_GR_CITIES, CATEGORY_CHOICES_CY_CITIES, AL_CITIES, AZ_CITIES, CA_CITIES, CO_CITIES, CT_CITIES, DE_CITIES, FL_CITIES, GA_CITIES, HI_CITIES, IL_CITIES, IN_CITIES, KY_CITIES, LA_CITIES, ME_CITIES, MA_CITIES, MO_CITIES, NV_CITIES, NJ_CITIES, NY_CITIES, NC_CITIES, OH_CITIES, OK_CITIES, OR_CITIES, PA_CITIES, TN_CITIES, TX_CITIES, VA_CITIES, WA_CITIES

def packagesearch(request):
    if 'States' in request.GET:
        states = request.GET['States']
        if states == 'US':
            if 'Region' in request.GET:
                region = request.GET['Region']
                if region == 'AL':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Birmingham' and region == 'AL':
                        elif city == 'Mobile' and region == 'AL':
                        else:
                    else:
                elif region == 'AK':

                elif region == 'AZ':

                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Gilbert' and region == 'AZ':
                        elif city == 'Mesa' and region == 'AZ':
                        elif city == 'Scottsdale' and region == 'AZ':
                        else:
                    else:
                elif region == 'AR':
                elif region == 'CA':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Los Angeles' and region == 'CA':
                        else:
                    else:
                elif region == 'CO':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Denver' and region == 'CO':
                        else:
                    else:
                elif region == 'CT':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Norwalk' and region == 'CT':
                        elif city == 'Stamford' and region == 'CT':
                        elif city == 'Trumbull' and region == 'CT':
                        else:
                    else:
                elif region == 'DE':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Newark' and region == 'DE':
                        else:
                    else:
                elif region == 'FL':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Boca Raton' and region == 'FL':
                        elif city == 'Brandon' and region == 'FL':
                        elif city == 'Clearwater' and region == 'FL':
                        elif city == 'Miami' and region == 'FL':
                        elif city == 'Tampa' and region == 'FL':
                        elif city == 'Winter Park' and region == 'FL':
                        else:
                    else:
                elif region == 'GA':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Atlanta' and region == 'GA':
                        elif city == 'Marietta' and region == 'GA':
                        else:
                    else:
                elif region == 'HI':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Honolulu' and region == 'HI':
                        else:
                    else:
                elif region == 'ID':
                elif region == 'IL':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Glenview' and region == 'IL':
                        elif city == 'Hoffman Estates' and region == 'IL':
                        elif city == 'Chicago' and region == 'IL':
                        else:
                    else:
                elif region == 'IN':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Bloomington' and region == 'IN':
                        elif city == 'Indianapolis' and region == 'IN':
                        elif city == 'Munster' and region == 'IN':
                        elif city == 'Valparaiso' and region == 'IN':
                        else:
                    else:
                elif region == 'IA':
                elif region == 'KS':
                elif region == 'KY':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Louisville' and region == 'KY':
                        else:
                    else:
                elif region == 'LA':
                elif region == 'ME':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Bangor' and region == 'ME':
                        else:
                    else:
                elif region == 'MD':
                elif region == 'MA':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Boston' and region == 'MA':
                        else:
                    else:
                elif region == 'MI':
                elif region == 'MN':
                elif region == 'MS':
                elif region == 'MO':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'St. Louis' and region == 'MO':
                        else:
                    else:
                elif region == 'MT':
                elif region == 'NE':
                elif region == 'NV':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'St. Louis' and region == 'MO':
                        else:
                    else:
                elif region == 'NH':
                elif region == 'NJ':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Hoboken' and region == 'NJ':
                        elif city == 'Jersey City' and region == 'NJ':
                        elif city == 'Marlton' and region == 'NJ':
                        elif city == 'Princeton' and region == 'NJ':
                        else:
                    else:
                elif region == 'NM':
                elif region == 'NY':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Brooklyn' and region == 'NY':
                        elif city == 'New York City' and region == 'NY':
                        elif city == 'Staten Island' and region == 'NY':
                        elif city == 'Syracuse' and region == 'NY':
                        else:
                    else:
                elif region == 'NC':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Charlotte' and region == 'NC':
                        else:
                    else:
                elif region == 'ND':
                elif region == 'OH':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Akron' and region == 'OH':
                        elif city == 'West Chester' and region == 'OH':
                        else:
                    else:
                elif region == 'OK':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Oklahoma City' and region == 'OK':
                        else:
                    else:
                elif region == 'OR':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Portland' and region == 'OR':
                        else:
                    else:
                elif region == 'PA':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Bethlehem' and region == 'PA':
                        elif city == 'Lancaster' and region == 'PA':
                        elif city == 'Philadelphia' and region == 'PA':
                        elif city == 'West Chester' and region == 'PA':
                        else:
                    else:
                elif region == 'PR':
                elif region == 'RI':
                elif region == 'SC':
                elif region == 'SD':
                elif region == 'TN':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Franklin' and region == 'TN':
                        elif city == 'Chattanooga' and region == 'TN':
                        elif city == 'Nashville' and region == 'TN':
                        elif city == 'West Chester' and region == 'PA':
                        else:
                    else:
                elif region == 'TX':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Austin' and region == 'TX':
                        elif city == 'Dallas' and region == 'TX':
                        elif city == 'Frisco' and region == 'TX':
                        elif city == 'Houston' and region == 'TX':
                        elif city == 'McKinney' and region == 'TX':
                        elif city == 'San Antonio' and region == 'TX':
                        elif city == 'Sugar Land' and region == 'TX':
                        elif city == 'Webster' and region == 'TX':
                        else:
                    else:
                elif region == 'UT':
                elif region == 'VT':
                elif region == 'VA':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Arlington' and region == 'VA':
                        elif city == 'Fairfax' and region == 'VA':
                        elif city == 'Reston' and region == 'VA':
                        else:
                    else:
                elif region == 'WA':
                    if 'City' in request.GET:
                        city = request.GET['City']
                        if city == 'Bellevue' and region == 'WA':
                        elif city == 'Kirkland' and region == 'WA':
                        elif city == 'Seattle' and region == 'WA':
                        else:
                    else:
                elif region == 'WV':
                elif region == 'WI':
                elif region == 'WY':
                elif region == 'DC':
                else:
            elif:
                if 'treatments' in request.GET:
                    treatments = request.GET['treatments']
            else:

        elif states == 'UK':
            if 'Region' in request.GET:
                region = request.GET['Region']
                if region == 'Aberdeen':
                elif region == 'Bath':
                elif region == 'Belfast':
                elif region == 'Birmingham':
                elif region == 'Bournemouth':
                elif region == 'BrightonHove':
                elif region == 'Bristol':
                elif region == 'Cambridge':
                elif region == 'Cardiff':
                elif region == 'Colchester':
                elif region == 'Derby':
                elif region == 'Exeter':
                elif region == 'Glasgow':
                elif region == 'Hull':
                elif region == 'Chelmsford':
                elif region == 'Leeds':
                elif region == 'Leicester':
                elif region == 'Liverpool':
                elif region == 'London':
                elif region == 'Manchester':
                elif region == 'Middlesbrough':
                elif region == 'Newcastle':
                elif region == 'Norwich':
                elif region == 'Nottingham':
                elif region == 'Oxford':
                elif region == 'Peterborough':
                elif region == 'Plymouth':
                elif region == 'Portsmouth':
                elif region == 'Salisbury':
                elif region == 'Sheffield':
                elif region == 'Southampton':
                elif region == 'Swansea':
                else:
            elif:
                if 'treatments' in request.GET:
                    treatments = request.GET['treatments']
            else:

        elif states == 'CZ':
            if 'Region' in request.GET:
            region = request.GET['Region']
                if region == 'Prague':
                elif region == 'Brno':
                else:
            elif:
                if 'treatments' in request.GET:
                    treatments = request.GET['treatments']
            else:

        elif states == 'SP':
            if 'Region' in request.GET:
                region = request.GET['Region']
                if region == 'Alicante':
                elif region == 'Barcelona':
                elif region == 'Madrid':
                elif region == 'Malaga':
                elif region == 'Seville':
                elif region == 'Valencia':
                else:
            elif:
                if 'treatments' in request.GET:
                    treatments = request.GET['treatments']
            else:

        elif states == 'IN':
            if 'Region' in request.GET:
                region = request.GET['Region']
                if region == 'Chennai':
                elif region == 'Hyderabad':
                elif region == 'Mumbai':
                elif region == 'Patna':
                elif region == 'Raipur':
                elif region == 'Amdavad':
                elif region == 'Chandigarh':
                elif region == 'Faridabad':
                elif region == 'Jamshedpur':
                elif region == 'Bangalore':
                elif region == 'Trivandrum':
                elif region == 'Kochi':
                elif region == 'Bhopal':
                elif region == 'Indore':
                elif region == 'Nagpur':
                elif region == 'Bhubaneswar':
                elif region == 'Ludhiana':
                elif region == 'Jaipur':
                elif region == 'Lucknow':
                elif region == 'Kanpur':
                elif region == 'Dehradun':
                elif region == 'Kolkata':
                elif region == 'Visakhapatnam':
                elif region == 'Vijayawada':
                elif region == 'New Delhi':
                elif region == 'Vadodara':
                elif region == 'Gurugram':
                elif region == 'Rohtak':
                elif region == 'Jammu':
                elif region == 'Ranchi':
                elif region == 'Gwalior':
                elif region == 'Pune':
                elif region == 'Warangal':
                elif region == 'Gachibowli':
                elif region == 'Madhapur':
                elif region == 'Noida':
                elif region == 'Meerut':
                elif region == 'Haldwani':
                else:
            elif:
                if 'treatments' in request.GET:
                    treatments = request.GET['treatments']
            else:

        elif states == 'GR':
            if 'Region' in request.GET:
                region = request.GET['Region']
                if region == 'Athens':
                elif region == 'Thessaloniki':
                else:
            elif:
                if 'treatments' in request.GET:
                    treatments = request.GET['treatments']
            else:

        elif states == 'CY':
            if 'Region' in request.GET:
                region = request.GET['Region']
                if region == 'Nicosia':
                elif region == 'Girne':
                else:
            elif:
                if 'treatments' in request.GET:
                    treatments = request.GET['treatments']
            else:

        elif states == 'MX':
            if 'Region' in request.GET:
                region = request.GET['Region']
                if region == 'Cancún':
                elif region == 'Mexico City':
                else:
            elif:
                if 'treatments' in request.GET:
                    treatments = request.GET['treatments']
            else:

        elif 'treatments' in request.GET:
                tretments = request.GET['treatments']
        else
    else:




        todayDate = timezone.now()

        listing = Package.objects.all()
        prolisting = Package.objects.filter(packageclinic__pro_is_published = True, packageclinic__ppq_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
        ppqlisting = Package.objects.filter(packageclinic__ppq_is_published = True, packageclinic__pro_is_published = False).exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
        count = listing.count()

        prolisting = prolisting.order_by('package_end_list_date')
        ppqlisting = ppqlisting.order_by('package_end_list_date')

        order_data = list(ppqlisting) + list(prolisting)

        paginator = Paginator(order_data, 50)
        page = request.GET.get('page')
        paginationing = paginator.get_page(page)

        context = {
            'listing': listing, 'count': count, 'order_data': paginationing, 'paginationing': paginationing, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET,
        }

        return render(request, 'packages/search.html', context)
