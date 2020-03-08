from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler400, handler500
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps
from .sitemaps import StaticViewSitemap

handler404 = 'base.views.error404'
handler400 = 'base.views.error400'
handler500 = 'base.views.error500'

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('search.urls')),
    path('', include('location.urls')),
    path('', include('searchLocationsCities.urls')),
    path('', include('searchLocationsCountries.urls')),
    path('account/', include('owners.urls')),
    path('', include('clinicsUK.urls')),
    path('cookies/', include('cookie_consent.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
