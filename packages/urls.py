from django.urls import path

from . import views

urlpatterns = [
    path('packages', views.packages, name='packages'),
    path('searching', views.searchpackages, name='searchpackages'),
]
