from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
HttpResponseRedirect, HttpResponsePermanentRedirect)
from django.urls import reverse
from django.core.paginator import Paginator
from search.choices import CATEGORY_CHOICES_STATES
from django import template
from contact.forms import WebsiteForm
from django.core.mail import send_mail
from django.contrib import messages, auth

def index(request):

    context = {
        'CATEGORY_CHOICES_STATES': CATEGORY_CHOICES_STATES
    }

    return render(request, 'main/index.html', context)

def businessinsiderbacklink(request):
    return HttpResponsePermanentRedirect(reverse('index'))

def about(request):
    return render(request, 'main/about.html')

def ivf_country_difference(request):
    return render(request, 'main/ivf-country-difference.html')

def robots(request):
    return render(request, 'main/robots.txt')

def team(request):
    return render(request, 'main/team.html')

def travelCalculator(request):
    return render(request, 'main/travel-calculator.html')

def cookies(request):
    return render(request, 'main/cookies.html')

def privacy(request):
    return render(request, 'main/privacy-policy.html')

def contactWebsite(request):
    form = WebsiteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()

        send_mail(
            'Někdo prosí o kontakt',
            'Obyčejný smrtelník prosí o kontakt - zkontroluj!',
            'langr.marketing@gmail.com',
            ['langr.marketing@gmail.com'],
            fail_silently=False,
            )

        messages.success(request, 'Your message was sent! We will contact you back as soon as possible!')
        return redirect(index)

    context = {
        'form': form,
    }

    return render(request, 'main/contact.html', context)

def error404(request, exception):
    data = {}
    return render(request,'main/404.html', data)

def error400(request, exception):
    data = {}
    return render(request,'main/400.html', data)

def error500(request):
    data = {}
    return render(request,'main/500.html', data)
