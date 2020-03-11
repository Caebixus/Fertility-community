from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from django.utils import timezone

# Create your views here.
def tcffag(request):
    listing = BasicClinic.objects.get(pk=6)
    context = {
        'listing': listing,
        }

    return render(request, 'agencies/US/California/the-center-for-fertility-and-gynecology.html', context)
