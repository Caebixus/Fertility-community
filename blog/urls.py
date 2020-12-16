from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('blog/ivf-abroad-costs', views.ivfabroadcosts, name='ivfabroadcosts'),
]
