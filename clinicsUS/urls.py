from django.urls import path

from . import views

urlpatterns = [
    path('clinics-uk/harley-street-fertility-clinic', views.hsfc, name='hsfc'),
]
