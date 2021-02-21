from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    #Authors
    path('authors/lisa-holliman', views.authorlisaholliman, name='authorlisaholliman'),

    #Blogs
    path('blog/ivf-abroad-costs', views.ivfabroadcosts, name='ivfabroadcosts'),
    path('blog/fertility-treatment-abroad-what-you-need-to-know', views.fertilityTreatmentAbroadWhatYouNeedToKnow, name='fertilityTreatmentAbroadWhatYouNeedToKnow'),
]
