from django.urls import path

from . import views

urlpatterns = [
    path('agencies/cz/pragamedica.html', views.pragamedica, name='pragamedica'),
]
