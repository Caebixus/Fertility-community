from django.urls import path
from .views import ClinicDetailView

app_name = 'clinics'

urlpatterns = [
    path('<int:pk>/<slug>/', ClinicDetailView.as_view(), name='clinic-detail')
]
