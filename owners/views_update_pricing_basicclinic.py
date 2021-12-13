from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from clinic.models import BasicClinic
from datetime import datetime
from .forms import PostForm, PostFormPro, UpdatePrice, UpdatePricePro
from django.core.mail import send_mail


@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def update(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)

    form = PostForm(request.POST or None, request.FILES or None, instance=instance, prefix="form1")

    if form.is_valid():
        instance = form.save(commit=False)

        if instance.clinic_pro_logo_pic_del == True:
            instance.clinic_pro_logo_pic.delete()
        if instance.clinic_pro_photo_1_del == True:
            instance.clinic_pro_photo_1.delete()
        else:
            pass
        if instance.clinic_pro_photo_2_del == True:
            instance.clinic_pro_photo_2.delete()
        else:
            pass
        if instance.clinic_pro_photo_3_del == True:
            instance.clinic_pro_photo_3.delete()
        else:
            pass
        if instance.clinic_pro_photo_4_del == True:
            instance.clinic_pro_photo_4.delete()
        else:
            pass
        if instance.clinic_pro_photo_5_del == True:
            instance.clinic_pro_photo_5.delete()
        else:
            pass
        if instance.clinic_pro_photo_6_del == True:
            instance.clinic_pro_photo_6.delete()
        else:
            pass

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
                ['David.langr@fertilitycommunity.com'],
                fail_silently=False,
                )
            messages.success(request, '- Clinics information successfully updated')
            return redirect(dashboard)
        else:
            messages.success(request, '- Clinics information successfully updated')
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
                ['David.langr@fertilitycommunity.com'],
                fail_silently=False,
                )
            messages.success(request, '- Clinics pricing successfully updated')
            return redirect(dashboard)
        else:
            messages.success(request, '- Clinics pricing successfully updated')
            return redirect(dashboard)

    context = {
        'instance': instance,
        'form': form,
    }

    return render(request, 'owners/updateprice.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def updateproclinic(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)

    form = PostFormPro(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        if instance.clinic_pro_logo_pic_del == True:
            instance.clinic_pro_logo_pic.delete()
        else:
            pass
        if instance.team1pic_del == True:
            instance.team1pic.delete()
        else:
            pass
        if instance.team2pic_del == True:
            instance.team2pic.delete()
        else:
            pass
        if instance.team3pic_del == True:
            instance.team3pic.delete()
        else:
            pass
        if instance.clinic_pro_photo_1_del == True:
            instance.clinic_pro_photo_1.delete()
        else:
            pass
        if instance.clinic_pro_photo_2_del == True:
            instance.clinic_pro_photo_2.delete()
        else:
            pass
        if instance.clinic_pro_photo_3_del == True:
            instance.clinic_pro_photo_3.delete()
        else:
            pass
        if instance.clinic_pro_photo_4_del == True:
            instance.clinic_pro_photo_4.delete()
        else:
            pass
        if instance.clinic_pro_photo_5_del == True:
            instance.clinic_pro_photo_5.delete()
        else:
            pass
        if instance.clinic_pro_photo_6_del == True:
            instance.clinic_pro_photo_6.delete()
        else:
            pass
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
                ['David.langr@fertilitycommunity.com'],
                fail_silently=False,
                )
            messages.success(request, '- Clinics information successfully updated')
            return redirect(dashboard)

        else:
            messages.success(request, '- Clinics information successfully updated')
            return redirect(dashboard)

    context = {
        'instance': instance,
        'form': form,
    }

    return render(request, 'owners/updateproclinic.html', context)

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
                ['David.langr@fertilitycommunity.com'],
                fail_silently=False,
                )
            messages.success(request, '- Clinics pricing successfully updated')
            return redirect(dashboard)
        else:
            messages.success(request, '- Clinics pricing successfully updated')
            return redirect(dashboard)

    context = {
        'instance': instance,
        'form': form,
    }

    return render(request, 'owners/updatepricepro.html', context)