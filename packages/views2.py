from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from blog.models import Blog

from search.choices import *


def packages2(request):
    return HttpResponsePermanentRedirect(reverse('packagesearch'))

def packages3(request):
    return HttpResponsePermanentRedirect(reverse('packagesearch'))


def packagesearch(request):
    todayDate = timezone.now()
    blog = Blog.objects.filter(tag__iexact='IVF Packages').order_by('-created_at')
    alllisting = Package.objects.all().exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
    countall = alllisting.count()
    allpackages = 'All packages'

    values = request.GET
    if "States" or "Region" or "packages" in values.keys():
        search_origin_version = True
    else:
        search_origin_version = False

    states = 'empty'
    region = 'empty'
    packages = 'empty'

    if 'States' in values.keys():
        states = request.GET['States']
        if states == None or states == '':
            states = 'empty'
    else:
        states = 'empty'

    if 'Region' in values.keys():
        region = request.GET['Region']
        if region == None or region == '':
            region = 'empty'
    else:
        region = 'empty'

    if 'packages' in values.keys():
        packages = request.GET['packages']
        if packages == None or packages == '':
            packages = 'empty'
    else:
        packages = 'empty'


    if states != 'empty':

        if region != 'empty':

            if packages != 'empty':

                if packages == allpackages:
                    prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False, packageclinic__clinicState__iexact=states, packageclinic__clinicRegion__iexact=region)
                    ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False, packageclinic__clinicState__iexact=states, packageclinic__clinicRegion__iexact=region)
                    count = prolisting.count() + ppqlisting.count()

                    prolisting = prolisting.order_by('package_end_list_date')
                    ppqlisting = ppqlisting.order_by('package_end_list_date')

                    order_data = list(ppqlisting) + list(prolisting)

                    paginator = Paginator(order_data, 50)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
                    }
                    return render(request, 'packages/package-search.html', context)

                elif packages != 'empty':
                    prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False, packagecategory=packages)
                    ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False, packagecategory=packages)
                    count = prolisting.count() + ppqlisting.count()

                    prolisting = prolisting.order_by('package_end_list_date')
                    ppqlisting = ppqlisting.order_by('package_end_list_date')

                    order_data = list(ppqlisting) + list(prolisting)

                    paginator = Paginator(order_data, 50)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
                    }
                    return render(request, 'packages/package-search.html', context)

                else:
                    prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False)
                    ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False)
                    count = prolisting.count() + ppqlisting.count()

                    prolisting = prolisting.order_by('package_end_list_date')
                    ppqlisting = ppqlisting.order_by('package_end_list_date')

                    order_data = list(ppqlisting) + list(prolisting)

                    paginator = Paginator(order_data, 50)
                    page = request.GET.get('page')
                    paginationing = paginator.get_page(page)

                    context = {
                        'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
                    }
                    return render(request, 'packages/package-search.html', context)

            else:
                prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False, packageclinic__clinicState__iexact=states, packageclinic__clinicRegion__iexact=region)
                ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False, packageclinic__clinicState__iexact=states, packageclinic__clinicRegion__iexact=region)
                count = prolisting.count() + ppqlisting.count()

                prolisting = prolisting.order_by('package_end_list_date')
                ppqlisting = ppqlisting.order_by('package_end_list_date')

                order_data = list(ppqlisting) + list(prolisting)

                paginator = Paginator(order_data, 50)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {
                    'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
                }

                return render(request, 'packages/package-search.html', context)

        else:
            if packages == allpackages:
                prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False, packageclinic__clinicState__iexact=states)
                ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False, packageclinic__clinicState__iexact=states)
                count = prolisting.count() + ppqlisting.count()

                prolisting = prolisting.order_by('package_end_list_date')
                ppqlisting = ppqlisting.order_by('package_end_list_date')

                order_data = list(ppqlisting) + list(prolisting)

                paginator = Paginator(order_data, 50)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {
                    'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
                }
                return render(request, 'packages/package-search.html', context)


            elif packages != 'empty':
                prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False, packageclinic__clinicState__iexact=states, packagecategory=packages)
                ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False, packageclinic__clinicState__iexact=states, packagecategory=packages)
                count = prolisting.count() + ppqlisting.count()

                prolisting = prolisting.order_by('package_end_list_date')
                ppqlisting = ppqlisting.order_by('package_end_list_date')

                order_data = list(ppqlisting) + list(prolisting)

                paginator = Paginator(order_data, 50)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {
                    'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
                }
                return render(request, 'packages/package-search.html', context)

            else:
                prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False, packageclinic__clinicState__iexact=states)
                ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False, packageclinic__clinicState__iexact=states)
                count = prolisting.count() + ppqlisting.count()

                prolisting = prolisting.order_by('package_end_list_date')
                ppqlisting = ppqlisting.order_by('package_end_list_date')

                order_data = list(ppqlisting) + list(prolisting)

                paginator = Paginator(order_data, 50)
                page = request.GET.get('page')
                paginationing = paginator.get_page(page)

                context = {
                    'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
                }
                return render(request, 'packages/package-search.html', context)

            prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False, packageclinic__clinicState__iexact=states)
            ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False, packageclinic__clinicState__iexact=states)
            count = prolisting.count() + ppqlisting.count()

            prolisting = prolisting.order_by('package_end_list_date')
            ppqlisting = ppqlisting.order_by('package_end_list_date')

            order_data = list(ppqlisting) + list(prolisting)

            paginator = Paginator(order_data, 50)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {
                'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
            }

            return render(request, 'packages/package-search.html', context)

    else:
        if packages == allpackages:
            prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False)
            ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False)
            count = prolisting.count() + ppqlisting.count()

            prolisting = prolisting.order_by('package_end_list_date')
            ppqlisting = ppqlisting.order_by('package_end_list_date')

            order_data = list(ppqlisting) + list(prolisting)

            paginator = Paginator(order_data, 50)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {
                'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
            }
            return render(request, 'packages/package-search.html', context)

        elif packages != 'empty':
            prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False, packagecategory=packages)
            ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False, packagecategory=packages)
            count = prolisting.count() + ppqlisting.count()

            prolisting = prolisting.order_by('package_end_list_date')
            ppqlisting = ppqlisting.order_by('package_end_list_date')

            order_data = list(ppqlisting) + list(prolisting)

            paginator = Paginator(order_data, 50)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {
                'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
            }
            return render(request, 'packages/package-search.html', context)

        else:
            prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False)
            ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False)
            count = prolisting.count() + ppqlisting.count()

            prolisting = prolisting.order_by('package_end_list_date')
            ppqlisting = ppqlisting.order_by('package_end_list_date')

            order_data = list(ppqlisting) + list(prolisting)

            paginator = Paginator(order_data, 50)
            page = request.GET.get('page')
            paginationing = paginator.get_page(page)

            context = {
                'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
            }
            return render(request, 'packages/package-search.html', context)

        prolisting = Package.objects.filter(packageclinic__pro_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__ppq_is_published=False)
        ppqlisting = Package.objects.filter(packageclinic__ppq_is_published=True, package_end_list_date__date__gte=todayDate, packageclinic__pro_is_published=False)
        count = prolisting.count() + ppqlisting.count()

        prolisting = prolisting.order_by('package_end_list_date')
        ppqlisting = ppqlisting.order_by('package_end_list_date')

        order_data = list(ppqlisting) + list(prolisting)

        paginator = Paginator(order_data, 50)
        page = request.GET.get('page')
        paginationing = paginator.get_page(page)

        context = {
            'count': count, 'countall': countall, 'order_data': paginationing, 'paginationing': paginationing, 'blog': blog, 'CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA': CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA, 'CATEGORY_CHOICES_STATES_PACKAGES_EUROPE': CATEGORY_CHOICES_STATES_PACKAGES_EUROPE, 'CATEGORY_CHOICES_STATES_PACKAGES_ASIA': CATEGORY_CHOICES_STATES_PACKAGES_ASIA, 'CATEGORY_CHOICES_US_REGION': CATEGORY_CHOICES_US_REGION, 'CATEGORY_CHOICES_UK_CITIES': CATEGORY_CHOICES_UK_CITIES, 'CATEGORY_CHOICES_CZ_CITIES': CATEGORY_CHOICES_CZ_CITIES, 'CATEGORY_CHOICES_SK_CITIES': CATEGORY_CHOICES_SK_CITIES, 'CATEGORY_CHOICES_DK_CITIES': CATEGORY_CHOICES_DK_CITIES, 'CATEGORY_CHOICES_SP_CITIES': CATEGORY_CHOICES_SP_CITIES, 'CATEGORY_CHOICES_IN_CITIES': CATEGORY_CHOICES_IN_CITIES, 'CATEGORY_CHOICES_GR_CITIES': CATEGORY_CHOICES_GR_CITIES, 'CATEGORY_CHOICES_CY_CITIES': CATEGORY_CHOICES_CY_CITIES, 'AL_CITIES': AL_CITIES, 'AZ_CITIES': AZ_CITIES, 'CA_CITIES': CA_CITIES, 'CO_CITIES': CO_CITIES, 'CT_CITIES': CT_CITIES, 'DE_CITIES': DE_CITIES, 'FL_CITIES': FL_CITIES, 'GA_CITIES': GA_CITIES, 'HI_CITIES': HI_CITIES, 'IL_CITIES': IL_CITIES, 'IN_CITIES': IN_CITIES, 'KY_CITIES': KY_CITIES, 'LA_CITIES': LA_CITIES, 'ME_CITIES': ME_CITIES, 'MA_CITIES': MA_CITIES, 'MO_CITIES': MO_CITIES, 'NV_CITIES': NV_CITIES, 'NJ_CITIES': NJ_CITIES, 'NY_CITIES': NY_CITIES, 'NC_CITIES': NC_CITIES, 'OH_CITIES': OH_CITIES, 'OK_CITIES': OK_CITIES, 'OR_CITIES': OR_CITIES, 'PA_CITIES': PA_CITIES, 'TN_CITIES': TN_CITIES, 'TX_CITIES': TX_CITIES, 'VA_CITIES': VA_CITIES, 'WA_CITIES': WA_CITIES, 'values': request.GET, 'search_origin_version': search_origin_version,
        }

        return render(request, 'packages/package-search.html', context)
