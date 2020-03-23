from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler400, handler500
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views
from django.contrib import sitemaps
from .sitemaps import StaticViewSitemap
from .sitemapsRegions import RegionsViewSitemap
from .sitemapsCountries import CountriesViewSitemap
from .sitemapsCities import CitiesViewSitemap
from .sitemapsClinics import ClinicsViewSitemap

handler404 = 'base.views.error404'
handler400 = 'base.views.error400'
handler500 = 'base.views.error500'

sitemaps = {
    'static': StaticViewSitemap,
    'regions': RegionsViewSitemap,
    'cities': CitiesViewSitemap,
    'countries': CountriesViewSitemap,
    'clinics': ClinicsViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('search.urls')),
    path('', include('location.urls')),
    path('', include('searchLocationsCities.urls')),
    path('', include('searchLocationsCountries.urls')),
    path('', include('searchLocationsRegionsUS.urls')),
    path('account/', include('owners.urls')),
    path('', include('clinicsUK.urls')),
    path('', include('clinicsUS.urls')),
    path('', include('agenciesUS.urls')),
    path('cookies/', include('cookie_consent.urls')),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
