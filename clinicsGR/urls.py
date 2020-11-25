from django.urls import path

from . import views

urlpatterns = [
    #Thessaloniki
    path('clinics/gr/thessaloniki/newlife-ivf-clinic', views.newlifeivfclinic, name='newlifeivfclinic'),
    path('clinics/gr/thessaloniki/embryoclinic', views.embryoclinic, name='embryoclinic'),
    path('clinics/gr/thessaloniki/embryolab', views.embryolab, name='embryolab'),

    #Athens
    path('clinics/gr/athens/serum-ivf-center', views.serumivfcenter, name='serumivfcenter'),
    path('clinics/gr/athens/ivf-athens-center', views.ivfathenscenter, name='ivfathenscenter'),
    path('clinics/gr/athens/embryoland-ivf-center-athens', views.embryolandivfcenterathens, name='embryolandivfcenterathens'),
    path('clinics/gr/athens/embio-medical-center', views.embiomedicalcenter, name='embiomedicalcenter'),
    path('clinics/gr/athens/mitosis-ivf-clinic', views.mitosisivfclinic, name='mitosisivfclinic'),
    path('clinics/gr/athens/eugonia-assisted-reproduction-unit', views.eugoniaassistedreproductionunit, name='eugoniaassistedreproductionunit'),

    #Chania
    path('clinics/gr/chania/mediterranean-fertility-institute', views.mediterraneanfertilityinstitute, name='mediterraneanfertilityinstitute'),
    ]
