from django.urls import path

from . import views
from . import views2

urlpatterns = [
    path('search', views2.search_new, name='search'),
]
