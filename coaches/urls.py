from . import views
from django.urls import path

from .views import CoachDetailView, CoachDeleteView, SnippetDeleteView

app_name = 'coach'

urlpatterns = [
    path('fertility-specialists', views.coach_search, name='coach_search'),
    path('fertility-specialist/<int:pk>/<slug>/', CoachDetailView.as_view(), name='coach-detail'),
    path('fertility-specialist/delete/<int:pk>/<slug>/', CoachDeleteView.as_view(), name='coach-delete'),

    path('fertility-specialist/delete/<int:pk>/', SnippetDeleteView.as_view(), name='snippet-delete'),
    path('fertility-specialist/snippet/create-with-coach/<int:coach_id>', views.SnippetCreateFormView2, name='snippet-create-with-coach'),
    path('fertility-specialist/snippet/create/<int:blog_id>', views.SnippetCreateFormView, name='snippet-create'),
    path('fertility-specialist/snippet/update/<int:blog_id>/<int:snippet_id>', views.SnippetUpdateFormView, name='snippet-update'),

]