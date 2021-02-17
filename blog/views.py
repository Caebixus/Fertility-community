from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from search.choices import CATEGORY_CHOICES_STATES, CATEGORY_CHOICES_US_REGION, CATEGORY_CHOICES_UK_CITIES
from django import template
from contact.forms import WebsiteForm
from django.core.mail import send_mail
from django.contrib import messages, auth
from clinic.models import BasicClinic
from blog.models import Author, Blog

#Authors
def authorlisaholliman(request):
    author = get_object_or_404(Author, pk=6)
    blog = author.entries.all()

    context = {
        'author': author,
        'blog': blog,
    }

    return render(request, 'blog/authors/lisa-holliman.html', context)



def ivfabroadcosts(request):
    author = get_object_or_404(Author, pk=6)
    blog = get_object_or_404(Blog, pk=7)

    context = {
        'author': author,
        'blog': blog,
    }

    return render(request, 'blog/IVF-abroad/ivf-abroad-costs.html', context)
