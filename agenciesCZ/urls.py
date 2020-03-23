from django.urls import path

from . import views

urlpatterns = [
    path('agencies/cz/pragamedica', views.pragamedica, name='pragamedica'),
]
