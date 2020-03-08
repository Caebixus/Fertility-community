from django.urls import path

from . import views

urlpatterns = [
    path('clinics-uk/harley-street-fertility-clinic', views.hsfc, name='hsfc'),
    path('clinics-uk/ivi-london', views.iviLondon, name='iviLondon'),
    path('clinics-uk/crgh', views.crgh, name='crgh'),
]
