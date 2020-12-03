from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages, auth
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from clinic.models import BasicClinic
from packages.models import Packages
from packages.models import Package
from payments.models import Customer
from .models import ownerProInterested, ProUser, AuthenticatedUser
from contact.models import contactClinic
from django.utils import timezone
from datetime import datetime, timedelta
from .forms import PostForm, PostFormPro, UpdatePrice, UpdatePricePro, OwnerProInterestedForm, CreateClinic, CreatePackage, PostFormProUpdatePackage, CreatePackageEmail, ProlongPackage
from contact.forms import ContactForm, ClaimForm
from django.core.mail import send_mail
from django.forms.fields import Field, FileField
from .decorators import allowed_users
from django.contrib.auth.models import Group
from django.db.models import F
from django.db.models import Count

# Create your views here.
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if passwords match
        if password == password2:
            #check Email
            if User.objects.filter(email=email).exists():
                messages.error(request, '- That email is already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, password=password, username=username)
                #login after registered
                auth.login(request, user)
                messages.success(request, '- You are now logged in')

                send_mail(
                    'Confirm registration - fertilitycommunity.com',
                    'Please activate your account via this link (copy this): https://www.fertilitycommunity.com/account/activate-user?xx1kfdj4sdsdsf48a6aasd7',
                    'info@fertilitycommunity.com',
                    [user.email],
                    fail_silently=False,
                    )

                return redirect('notActiveUser')
        else:
            messages.error(request, '- Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'owners/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, username=username, password=password)

        if user is not None:
            try:
                if user.authenticateduser.is_activated == True:
                    auth.login(request, user)
                    messages.success(request, '- You are now logged in')
                    return redirect('dashboard')
                else:
                    auth.login(request, user)
                    return redirect('notActiveUser')
            except ObjectDoesNotExist:
                auth.login(request, user)
                return redirect('notActiveUser')
        else:
            messages.error(request, '- Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'owners/signin.html')

def upgrade2(request):
    return render(request, 'owners/upgrade2.html')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def howtousefertilitycommunity(request):
    return render(request, 'owners/how-to-use-fertilitycommunity.html')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def notActiveUser(request):
    return render(request, 'owners/not-active-user.html')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def activateUser(request):
    user = request.user
    try:
        authenticateduser = AuthenticatedUser()
        authenticateduser.user = user
        authenticateduser.is_activated = True
        authenticateduser.save()
        return render(request, 'owners/user-active.html')
    except ObjectDoesNotExist:
        authenticateduser = AuthenticatedUser()
        authenticateduser.user = user
        authenticateduser.is_activated = True
        authenticateduser.save()
        return render(request, 'owners/user-active.html')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, '- You are logged out')
        return redirect('index')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def dashboard(request):
    todayDate = timezone.now()
    user = request.user
    try:
        if user.authenticateduser.is_activated == False:
            return redirect('notActiveUser')
        else:
            all = BasicClinic.objects.filter(clinicOwner_id=request.user)
            listingsbasic = BasicClinic.objects.filter(clinicOwner_id=request.user)

            listingspro = BasicClinic.objects.filter(clinicOwner_id=request.user).filter(pro_is_published=True)
            package_pro_count = listingspro.filter(package__package_end_list_date__gte=todayDate).annotate(number_of_packages=Count('package'))

            listingsppq = BasicClinic.objects.filter(clinicOwner_id=request.user).filter(ppq_is_published=True)
            package_ppq_count = listingsppq.filter(package__package_end_list_date__gte=todayDate).annotate(number_of_packages=Count('package'))

            customer = Customer.objects.filter(customerClinic__in=all)

            package = Package.objects.filter(packageclinic__in=all)
            package = package.count()

            basic = all.filter(clinicOwner_id=request.user)
            instance = basic.filter(pro_is_published='True')
            ppqinstance = basic.filter(ppq_is_published='True')
            ppqinstance = ppqinstance.count()
            instance = instance.count()
            instance = (instance * 2) + (ppqinstance * 6)

            userdata = User.objects.get(username=request.user).last_login

            usergroup = ProUser.objects.all()
            usergroup = usergroup.filter(user=request.user)
            usergroup = usergroup.filter(paidPropublished=True)

            context = {
                'package_ppq_count': package_ppq_count,
                'package_pro_count': package_pro_count,
                'listingsbasic': listingsbasic,
                'listingspro': listingspro,
                'listingsppq': listingsppq,
                'customer': customer,
                'package': package,
                'userdata': userdata,
                'instance': instance,
                'usergroup': usergroup,
            }

            return render(request, 'owners/dashboard.html', context)
    except ObjectDoesNotExist:
        return redirect('notActiveUser')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def settings(request):
    user = request.user
    try:
        if user.authenticateduser.is_activated == False:
            return redirect('notActiveUser')
        else:
            usergroup = ProUser.objects.all()
            usergroup = usergroup.filter(user=request.user)
            usergroup = usergroup.filter(paidPropublished=True)
            listings = BasicClinic.objects.filter(clinicOwner_id=request.user)

            context = {
                'listings': listings,
                'usergroup': usergroup,
            }

            return render(request, 'owners/settings.html', context)
    except ObjectDoesNotExist:
        return redirect('notActiveUser')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def banners(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)
    listings = BasicClinic.objects.filter(clinicOwner_id=request.user)
    california = listings.filter(clinicRegion__iexact='California').first()
    alabama = listings.filter(clinicRegion__iexact='Alabama').first()
    england = listings.filter(clinicRegion__iexact='England').first()

    context = {
        'listings': listings,
        'usergroup': usergroup,
        'california': california,
        'alabama': alabama,
        'england': england,
    }

    return render(request, 'owners/banners.html', context)


@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def upgrade(request, listing_id):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    listings = get_object_or_404(BasicClinic, pk=listing_id)

    context = {
        'usergroup': usergroup,
        'listings': listings,
    }

    return render(request, 'owners/upgrade.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def claim(request):
    user = request.user
    try:
        if user.authenticateduser.is_activated == False:
            return redirect('notActiveUser')
        else:
            usergroup = ProUser.objects.all()
            usergroup = usergroup.filter(user=request.user)
            usergroup = usergroup.filter(paidPropublished=True)
            context={'usergroup': usergroup}
            return render(request, 'owners/claim.html', context)
    except ObjectDoesNotExist:
        return redirect('notActiveUser')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def create(request):
    user = request.user
    try:
        if user.authenticateduser.is_activated == False:
            return redirect('notActiveUser')
        else:
            usergroup = ProUser.objects.all()
            usergroup = usergroup.filter(user=request.user)
            usergroup = usergroup.filter(paidPropublished=True)
            if request.method == 'POST':
                listing = BasicClinic()

                listing.clinicOwner = request.user
                listing.name = request.POST['name']
                listing.title = request.POST['title']
                listing.description = request.POST['description']
                listing.logo_pic = request.FILES['logo_pic']
                listing.main_pic = request.FILES['main_pic']

                listing.contact_url = request.POST['contact_url']
                listing.contact_phone = request.POST['contact_phone']
                listing.contact_email = request.POST['contact_email']

                listing.address = request.POST['address']
                listing.city = request.POST['city']
                listing.state = request.POST['state']
                listing.zipcode = request.POST['zipcode']

                if 'ivf_treatment' in request.POST:
                    listing.ivf_treatment = True
                else:
                    listing.ivf_treatment = False
                if 'egg_donation' in request.POST:
                    listing.egg_donation = True
                else:
                    egg_donation = False
                if 'sperm_donation' in request.POST:
                    listing.sperm_donation = True
                else:
                    sperm_donation = False
                if 'embryo_donation' in request.POST:
                    listing.embryo_donation = True
                else:
                    embryo_donation = False

                if 'ivf_treatment_cost' in request.POST:
                    listing.ivf_treatment_cost = request.POST['ivf_treatment_cost']
                else:
                    listing.ivf_treatment_cost = int('0')
                if 'egg_donation_cost' in request.POST:
                    listing.egg_donation_cost = request.POST['egg_donation_cost']
                else:
                    listing.egg_donation_cost = int('0')
                if 'sperm_donation_cost' in request.POST:
                    listing.sperm_donation_cost = request.POST['sperm_donation_cost']
                else:
                    listing.sperm_donation_cost = int('0')
                if 'embryo_donation_cost' in request.POST:
                    listing.embryo_donation_cost = request.POST['embryo_donation_cost']
                else:
                    listing.embryo_donation_cost = int('0')

                if 'single_woman_treatment' in request.POST:
                    listing.single_woman_treatment = True
                else:
                    single_woman_treatment = False
                if 'reciprocal_ivf' in request.POST:
                    listing.reciprocal_ivf = True
                else:
                    reciprocal_ivf = False
                if 'hiv_patients' in request.POST:
                    listing.hiv_patients = True
                else:
                    hiv_patients = False
                if 'fertility_preservation' in request.POST:
                    listing.fertility_preservation = True
                else:
                    fertility_preservation = False

                listing.list_date = timezone.datetime.now()
                listing.is_claimed = True

                listing.save()
                return render(request, 'owners/dashboard.html')
            else:
                context = {
                    'usergroup': usergroup,
                }

                return render(request, 'owners/create.html', context)

            context = {
                'usergroup': usergroup,
            }

            return render(request, 'owners/create.html', context)
    except ObjectDoesNotExist:
        return redirect('notActiveUser')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def create1(request):
    user = request.user
    try:
        if user.authenticateduser.is_activated == False:
            return redirect('notActiveUser')
        else:
            usergroup = ProUser.objects.all()
            usergroup = usergroup.filter(user=request.user)
            usergroup = usergroup.filter(paidPropublished=True)
            form = CreateClinic(request.POST or None, request.FILES or None)
            if form.is_valid():
                form = form.save(commit=False)
                form.is_published_list_date = datetime.now()
                form.clinicOwner = request.user
                form.is_claimed = True
                form.save()

                klinika = form.clinicName

                send_mail(
                    'New Clinic Registration',
                    'Právě se vytvořila nová klinika ' +
                    '\nClinic username: ' + str(klinika),
                    'info@fertilitycommunity.com',
                    ['info@fertilitycommunity.com'],
                    fail_silently=False,
                    )

                messages.success(request, '- Clinic created - please wait for out team to review your clinic')
                return redirect(dashboard)

            context = {
                'form': form,
                'usergroup': usergroup,
            }

            return render(request, 'owners/create1.html', context)
    except ObjectDoesNotExist:
        return redirect('notActiveUser')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def update(request, listing_id):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.update_list_date = datetime.now()
        instance.save()

        data = form.cleaned_data
        klinika = instance.clinicName

        if instance.is_claimed == True:
            send_mail(
                'Change of clinics information',
                'Someone just changed information detail in ' +
                '\nClinic username: ' + str(klinika),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )
            messages.success(request, '- Clinics pricing succesfully updated')
            return redirect(dashboard)
        else:
            messages.success(request, '- Clinics information succesfully updated')
            return redirect(dashboard)

    context = {
        'instance': instance,
        'form': form,
        'usergroup': usergroup,
    }

    return render(request, 'owners/update.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def updatePricing(request, listing_id):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)
    form = UpdatePrice(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.update_list_date = datetime.now()
        instance.save()

        data = form.cleaned_data
        klinika = instance.clinicName

        if instance.is_claimed == True:
            send_mail(
                'Change of clinic pricing detail',
                'Someone just changed pricing detail in ' +
                '\nClinic username: ' + str(klinika),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )
            messages.success(request, '- Clinics pricing succesfully updated')
            return redirect(dashboard)
        else:
            messages.success(request, '- Clinics pricing succesfully updated')
            return redirect(dashboard)

    context = {
        'instance': instance,
        'form': form,
        'usergroup': usergroup,
    }

    return render(request, 'owners/updateprice.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def updateproclinic(request, listing_id):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)
    form = PostFormPro(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.pro_update_is_published_list_date = datetime.now()
        instance.save()

        data = form.cleaned_data
        klinika = instance.clinicName

        if instance.is_claimed == True:
            send_mail(
                'Change of clinic PRO information',
                'Someone just changed information in ' +
                '\nClinic username: ' + str(klinika),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )
            messages.success(request, '- Clinics information succesfully updated')
            return redirect(dashboard)

        else:
            messages.success(request, '- Clinics information succesfully updated')
            return redirect(dashboard)

    context = {
        'instance': instance,
        'form': form,
        'usergroup': usergroup,
    }

    return render(request, 'owners/updateproclinic.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def updatePricingPro(request, listing_id):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)
    form = UpdatePricePro(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.pro_update_is_published_list_date = datetime.now()
        instance.save()

        data = form.cleaned_data
        klinika = instance.clinicName

        if instance.is_claimed == True:
            send_mail(
                'Change of clinic pricing detail',
                'Someone just changed pricing detail in ' +
                '\nClinic username: ' + str(klinika),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )
            messages.success(request, '- Clinics pricing succesfully updated')
            return redirect(dashboard)
        else:
            messages.success(request, '- Clinics pricing succesfully updated')
            return redirect(dashboard)

    context = {
        'instance': instance,
        'form': form,
        'usergroup': usergroup,
    }

    return render(request, 'owners/updatepricepro.html', context)


@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def contactClinic(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.clinicOwner = request.user
        form.save()

        send_mail(
            'Klinika prosí o kontakt',
            'Někdo zaregistrovaný napsal na kontaktní formulář - zkontroluj!',
            'info@fertilitycommunity.com',
            ['info@fertilitycommunity.com'],
            fail_silently=False,
            )

        messages.success(request, '- Your message was sent! We will contact you back as soon as possible!')
        return redirect(dashboard)

    context = {
        'form': form,
        'usergroup': usergroup,
    }

    return render(request, 'owners/contactus.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def claimClinic(request):
    user = request.user
    try:
        if user.authenticateduser.is_activated == False:
            return redirect('notActiveUser')
        else:
            usergroup = ProUser.objects.all()
            usergroup = usergroup.filter(user=request.user)
            usergroup = usergroup.filter(paidPropublished=True)
            form = ClaimForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form = form.save(commit=False)
                form.clinicOwner = request.user
                form.save()

                send_mail(
                    'Klinika prosí o claim',
                    'Někdo se zaregistroval a poslal prosbu o claim - zkontroluj!',
                    'info@fertilitycommunity.com',
                    ['info@fertilitycommunity.com'],
                    fail_silently=False,
                    )

                messages.success(request, '- Your claim was sent! We will contact you back as soon as possible!')
                return redirect(dashboard)

            context = {
                'form': form,
                'usergroup': usergroup,
            }

            return render(request, 'owners/claim.html', context)
    except ObjectDoesNotExist:
        return redirect('notActiveUser')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def change_password(request):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was changed successfully!')
            return redirect('settings')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {
            'form': form,
            'usergroup': usergroup,
            }
        return render(request, 'owners/change-password.html', args)


# Packages SECTION
@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def packages(request, listing_id):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

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
        'usergroup': usergroup
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
    form.fields['packageclinic'].queryset = BasicClinic.objects.filter(id=listing).filter(pro_is_published=True)

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
        messages.warning(request, '- Maximum packages for PREMIUM clinic is {}' .format(instance))
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
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

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
        'usergroup': usergroup,
        'listing': listing,
        'package_count': package_count,
        'notactivelisting': notactivelisting,
        'instance': instance,
    }
    return render(request, 'owners/packages/clinic-package-settings.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def updatepropackage(request, package_id):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    instance = get_object_or_404(Package, pk=package_id)
    clinic = get_object_or_404(BasicClinic, pk=instance.packageclinic_id)

    form = PostFormProUpdatePackage(request.POST or None, request.FILES or None, instance=instance, prefix="form1")
    emailform = CreatePackageEmail(request.POST or None, request.FILES or None, instance=clinic, prefix="form2")

    if form.is_valid() and emailform.is_valid():
        instance = form.save(commit=False)
        instance.package_update_date = datetime.now()
        instance.save()
        emailform.save()

        messages.success(request, '- Package information succesfully updated')
        return redirect(dashboard)

    context = {
        'instance': instance,
        'emailform': emailform,
        'form': form,
        'usergroup': usergroup,
    }

    return render(request, 'owners/packages/update-package.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def prolongpropackage(request, package_id):
    usergroup = ProUser.objects.all()
    usergroup = usergroup.filter(user=request.user)
    usergroup = usergroup.filter(paidPropublished=True)

    instance = get_object_or_404(Package, pk=package_id)
    clinic = get_object_or_404(BasicClinic, pk=instance.packageclinic_id)

    form = ProlongPackage(request.POST or None, request.FILES or None, instance=instance,)

    if form.is_valid():
        form = form.save(commit=False)
        form.package_list_date = datetime.now()
        if form.package_limit_days == '30 Days':
            form.package_end_list_date = form.package_list_date + timedelta(days=30)
        else:
            form.package_end_list_date = form.package_list_date + timedelta(days=90)
        form.save()

        messages.success(request, '- Package end date succesfully prolonged')
        return redirect(dashboard)

    context = {
        'instance': instance,
        'form': form,
        'usergroup': usergroup,
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
