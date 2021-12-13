from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from clinic.models import BasicClinic
from .forms import Bestarticleproposition, Picclinicform
from django.core.mail import send_mail

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def bestclinicarticles(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)

    form = Bestarticleproposition(request.POST or None, instance=instance, prefix="form1")
    picform = Picclinicform(request.POST or None, request.FILES or None, instance=instance, prefix="form2")


    if form.is_valid() and picform.is_valid():
        form = form.save(commit=False)
        form.save()
        picform.save()

        klinika = instance.clinicName

        send_mail(
            'Klinika updatovala Best IVF Clinic Blogpost -' + str(klinika),
            'Buď někdo updatnul nový draft textu nebo unchecknul políčko',
            'info@fertilitycommunity.com',
            ['David.langr@fertilitycommunity.com'],
            fail_silently=False,
            )

        messages.success(request, '- Update successful. If you post new draft, please wait for our team to review and publish it.')
        return redirect(dashboard)

    context = {
        'picform': picform,
        'instance': instance,
        'form': form,
    }

    return render(request, 'owners/best-articles/owners-best-articles.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def bestclinicarticlescity(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)

    form = Bestarticleproposition(request.POST or None, instance=instance, prefix="form1")
    picform = Picclinicform(request.POST or None, request.FILES or None, instance=instance, prefix="form2")

    if form.is_valid() and picform.is_valid():
        form = form.save(commit=False)
        form.save()
        picform.save()

        klinika = instance.clinicName

        send_mail(
            'Klinika updatovala "Best IVF clinic - city" blogpost -' + str(klinika),
            'Buď někdo updatnul nový draft textu nebo unchecknul políčko',
            'info@fertilitycommunity.com',
            ['David.langr@fertilitycommunity.com'],
            fail_silently=False,
            )

        messages.success(request, '- Update successful. If you post new draft, please wait for our team to review and publish it.')
        return redirect(dashboard)

    context = {
        'picform': picform,
        'instance': instance,
        'form': form,
    }

    return render(request, 'owners/best-articles/owners-best-articles-city.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def bestclinicarticlesstate(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)

    form = Bestarticleproposition(request.POST or None, instance=instance, prefix="form1")
    picform = Picclinicform(request.POST or None, request.FILES or None, instance=instance, prefix="form2")

    if form.is_valid() and picform.is_valid():
        form = form.save(commit=False)
        form.save()
        picform.save()

        klinika = instance.clinicName

        send_mail(
            'Klinika updatovala "Best IVF clinic - state" blogpost -' + str(klinika),
            'Buď někdo updatnul nový draft textu nebo unchecknul políčko',
            'info@fertilitycommunity.com',
            ['David.langr@fertilitycommunity.com'],
            fail_silently=False,
            )

        messages.success(request, '- Update successful. If you post new draft, please wait for our team to review and publish it.')
        return redirect(dashboard)

    context = {
        'picform': picform,
        'instance': instance,
        'form': form,
    }

    return render(request, 'owners/best-articles/owners-best-articles-state.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def bestclinicarticlescountry(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)

    form = Bestarticleproposition(request.POST or None, instance=instance, prefix="form1")
    picform = Picclinicform(request.POST or None, request.FILES or None, instance=instance, prefix="form2")

    if form.is_valid() and picform.is_valid():
        form = form.save(commit=False)
        form.save()
        picform.save()

        klinika = instance.clinicName

        send_mail(
            'Klinika updatovala "Best IVF clinic - country" blogpost -' + str(klinika),
            'Buď někdo updatnul nový draft textu nebo unchecknul políčko',
            'info@fertilitycommunity.com',
            ['David.langr@fertilitycommunity.com'],
            fail_silently=False,
            )

        messages.success(request, '- Update successful. If you post new draft, please wait for our team to review and publish it.')
        return redirect(dashboard)

    context = {
        'picform': picform,
        'instance': instance,
        'form': form,
    }

    return render(request, 'owners/best-articles/owners-best-articles-country.html', context)