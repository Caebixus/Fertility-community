from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from clinic.models import BasicClinic
from packages.models import Package
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta
from .forms import CreatePackage, PostFormProUpdatePackage, CreatePackageEmail, ProlongPackage
from django.db.models import F
from .views import dashboard


@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def packages(request, listing_id):
    instance = Packages.objects.filter(packageClinic=listing_id)
    instance = instance.objects.filter(packageOwner_id=request.user)
    instance = instance.first()

    listing = Packages.objects.all()
    listing = listing.filter(packageOwner_id=request.user)
    listing = listing.filter(packageClinic=listing_id)
    count = listing.count()

    context = {
        'instance': instance,
        'listing': listing,
        'count': count,
    }

    return render(request, 'owners/packages/packages.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def createpackage(request, listing_id):
    clinic = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)

    listing = Package.objects.all()
    listing = listing.filter(packageclinic_id=listing_id)
    count = listing.count()

    if clinic.pro_is_published == True:
        instance = 2
    else:
        instance = 6

    form = CreatePackage(request.POST or None, request.FILES or None, initial={'packageclinic': clinic.id}, prefix="form1")
    emailform = CreatePackageEmail(request.POST or None, request.FILES or None, instance=clinic, prefix="form2")

    if count < instance:
        if form.is_valid() and emailform.is_valid():
            form = form.save(commit=False)
            form.package_list_date = datetime.now()
            if form.package_limit_days == '30 Days':
                form.package_end_list_date = form.package_list_date + timedelta(days=30)
            else:
                form.package_end_list_date = form.package_list_date + timedelta(days=90)
            form.packageclinic = clinic
            form.is_package_active = True
            form.save()
            emailform.save()

            clinic.packageClinicCounterNumber += int(1)
            clinic.save()

            messages.success(request, '- Package created')
            return redirect(dashboard)
    else:
        messages.warning(request, '- the maximum number of packages for this clinic paid plan is {} ' .format(instance))
        return redirect(dashboard)

    context = {
        'form': form,
        'emailform': emailform,
        'count': count,
        'instance': instance,
        'clinic': clinic,
    }

    return render(request, 'owners/packages/create-package.html', context)


@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def clinicpackagesettings(request, listing_id):
    todayDate = timezone.now()

    all_packages = Package.objects.filter(packageclinic_id=listing_id)
    package_count = all_packages.count()

    listing = Package.objects.filter(package_end_list_date__gte=todayDate)
    listing = listing.filter(packageclinic_id=listing_id)

    notactivelisting = Package.objects.filter(package_end_list_date__lte=todayDate)
    notactivelisting = notactivelisting.filter(packageclinic_id=listing_id)

    instance = get_object_or_404(BasicClinic, pk=listing_id)

    context = {
        'all_packages': all_packages,
        'listing': listing,
        'package_count': package_count,
        'notactivelisting': notactivelisting,
        'instance': instance,
    }
    return render(request, 'owners/packages/clinic-package-settings.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def updatepropackage(request, package_id):
    instance = get_object_or_404(Package, pk=package_id)
    clinic = get_object_or_404(BasicClinic, pk=instance.packageclinic_id)
    listing_id=clinic.pk

    form = PostFormProUpdatePackage(request.POST or None, request.FILES or None, instance=instance, prefix="form1")
    emailform = CreatePackageEmail(request.POST or None, request.FILES or None, instance=clinic, prefix="form2")

    if form.is_valid() and emailform.is_valid():
        instance = form.save(commit=False)
        if instance.package_pic_delete == True:
            instance.package_pic.delete()
            instance.package_update_date = datetime.now()

            instance.save()
            emailform.save()

            messages.success(request, '- Package information successfully updated')
            return redirect(reverse('clinicpackagesettings', kwargs={"listing_id": listing_id}))
        else:
            instance.package_update_date = datetime.now()

            instance.save()
            emailform.save()

            messages.success(request, '- Package information successfully updated')
            return redirect(reverse('clinicpackagesettings', kwargs={"listing_id": listing_id}))

    context = {
        'instance': instance,
        'emailform': emailform,
        'clinic': clinic,
        'form': form,
    }

    return render(request, 'owners/packages/update-package.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def prolongpropackage(request, package_id):
    instance = get_object_or_404(Package, pk=package_id)
    clinic = get_object_or_404(BasicClinic, pk=instance.packageclinic_id)
    listing_id=clinic.pk

    form = ProlongPackage(request.POST or None, request.FILES or None, instance=instance,)

    if form.is_valid():
        form = form.save(commit=False)
        form.package_list_date = datetime.now()
        if form.package_limit_days == '30 Days':
            form.package_end_list_date = form.package_list_date + timedelta(days=30)
        else:
            form.package_end_list_date = form.package_list_date + timedelta(days=90)
        form.save()

        messages.success(request, '- Package end date successfully prolonged')
        return redirect(reverse('clinicpackagesettings', kwargs={"listing_id": listing_id}))

    context = {
        'instance': instance,
        'form': form,
    }

    return render(request, 'owners/packages/prolong-package.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def deletepropackage(request, package_id):
    instance = get_object_or_404(Package, pk=package_id)

    clinic = get_object_or_404(BasicClinic, pk=instance.packageclinic.id)
    clinic.packageClinicCounterNumber = F('packageClinicCounterNumber') - 1
    clinic.save()

    instance.delete()

    messages.success(request, '- Package deleted')
    return redirect(dashboard)