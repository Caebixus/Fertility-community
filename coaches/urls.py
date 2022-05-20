from . import views, views_snippet_city, views_snippet_state, views_snippet_country
from django.urls import path

from .views import CoachDetailView, CoachDeleteView, SnippetDeleteView, CoachListView
from .views_snippet_city import SnippetCityUpdateFormView, SnippetCityCreateFormView, SnippetCityDeleteView
from .views_snippet_state import SnippetStateUpdateFormView, SnippetStateCreateFormView, SnippetStateDeleteView
from .views_snippet_country import SnippetCountryUpdateFormView, SnippetCountryCreateFormView, SnippetCountryDeleteView

app_name = 'coach'

urlpatterns = [
    path('fertility-specialists', CoachListView.as_view(), name='coach_search'),
    path('fertility-specialist/<int:pk>/<slug>/', CoachDetailView.as_view(), name='coach-detail'),
    path('fertility-specialist/delete/<int:pk>/<slug>/', CoachDeleteView.as_view(), name='coach-delete'),

    # General blogposts snippet
    path('fertility-specialist/delete/<int:pk>/', SnippetDeleteView.as_view(), name='snippet-delete'),
    path('fertility-specialist/snippet/create-with-coach/<int:coach_id>', views.SnippetCreateFormView, name='snippet-create'),
    path('fertility-specialist/snippet/update/<int:blog_id>/<int:snippet_id>', views.SnippetUpdateFormView, name='snippet-update'),

    # City blogposts snippet
    path('fertility-specialist/delete/sci/<int:pk>/', SnippetCityDeleteView.as_view(), name='snippet-city-delete'),
    path('fertility-specialist/snippet/sci/create-with-coach/<int:coach_id>', views_snippet_city.SnippetCityCreateFormView, name='snippet-city-create'),
    path('fertility-specialist/snippet/sci/update/<int:blog_id>/<int:snippet_id>', views_snippet_city.SnippetCityUpdateFormView, name='snippet-city-update'),

    # State blogposts snippet
    path('fertility-specialist/delete/sst/<int:pk>/', SnippetStateDeleteView.as_view(), name='snippet-state-delete'),
    path('fertility-specialist/snippet/sst/create-with-coach/<int:coach_id>', views_snippet_state.SnippetStateCreateFormView, name='snippet-state-create'),
    path('fertility-specialist/snippet/sst/update/<int:blog_id>/<int:snippet_id>', views_snippet_state.SnippetStateUpdateFormView, name='snippet-state-update'),

    # State blogposts snippet
    path('fertility-specialist/delete/sco/<int:pk>/', SnippetCountryDeleteView.as_view(), name='snippet-country-delete'),
    path('fertility-specialist/snippet/sco/create-with-coach/<int:coach_id>', views_snippet_country.SnippetCountryCreateFormView, name='snippet-country-create'),
    path('fertility-specialist/snippet/sco/update/<int:blog_id>/<int:snippet_id>', views_snippet_country.SnippetCountryUpdateFormView, name='snippet-country-update'),
]