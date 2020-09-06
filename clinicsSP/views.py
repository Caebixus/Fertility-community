from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from packages.models import Packages
from django.utils import timezone
from owners.models import ownerProInterested, ProUser

# Create your views here.
def aberfercen(request):
    return request()
