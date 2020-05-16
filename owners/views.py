from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from clinic.models import BasicClinic
from .models import ownerProInterested
from contact.models import contactClinic
from django.utils import timezone
from datetime import datetime
from .forms import PostForm, PostFormPro, UpdatePrice, UpdatePricePro, OwnerProInterestedForm, CreateClinic
from contact.forms import ContactForm, ClaimForm
from django.core.mail import send_mail
from django.forms.fields import Field, FileField

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
                return redirect('dashboard')
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
            auth.login(request, user)
            messages.success(request, '- You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, '- Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'owners/signin.html')

def upgrade2(request):
    return render(request, 'owners/upgrade2.html')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, '- You are logged out')
        return redirect('index')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def dashboard(request):
    listings = BasicClinic.objects.filter(clinicOwner_id=request.user)

    context = {
        'listings': listings,
    }

    return render(request, 'owners/dashboard.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def settings(request):
    listings = BasicClinic.objects.filter(clinicOwner_id=request.user)

    context = {
        'listings': listings,
    }

    return render(request, 'owners/settings.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def upgrade(request):
    form = OwnerProInterestedForm(request.POST or None)
    if form.is_valid():
        if ownerProInterested.objects.filter(clinicOwner=request.user).exists():
            messages.error(request, ' - Already opt-in!')
            return redirect(dashboard)
        else:
            form = form.save(commit=False)
            form.clinicOwner = request.user
            form.save()

            messages.success(request, ' - Successfully opt-in!')
            return redirect(dashboard)

    context = {
        'form': form,
    }

    return render(request, 'owners/upgrade.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def claim(request):
    return render(request, 'owners/claim.html')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def create(request):
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
        return render(request, 'owners/create.html')
    return render(request, 'owners/create.html')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def create1(request):
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

        messages.success(request, '- Clinic created - please check additional information + treatment pricing')
        return redirect(dashboard)

    context = {
        'form': form,
    }

    return render(request, 'owners/create1.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def update(request, listing_id):
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
    }

    return render(request, 'owners/update.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def updatePricing(request, listing_id):
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
    }

    return render(request, 'owners/updateprice.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def updatepro(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.pro_update_is_published_list_date = datetime.now()
        instance.pro_is_published = True
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
    }

    return render(request, 'owners/updatepro.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def updatePricingPro(request, listing_id):
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
    }

    return render(request, 'owners/updatepricepro.html', context)


@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def contactClinic(request):
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
    }

    return render(request, 'owners/contactus.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def claimClinic(request):
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
    }

    return render(request, 'owners/claim.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was changed successfully!')
            return redirect('settings')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'owners/change-password.html', args)
