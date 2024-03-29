from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler400, handler500
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import views
from django.contrib import sitemaps
from .sitemaps import StaticViewSitemap
from .sitemapsModularBlogs import ModularBlogsViewSitemap
from .sitemapsRegions import RegionsViewSitemap
from .sitemapsCountries import CountriesViewSitemap
from .sitemapsCities import CitiesViewSitemap
from .sitemapsClinics import ClinicsViewSitemap
from .sitemapsCosts import CostsViewSitemap
from .sitemapsBlogs import BlogsViewSitemap
from .sitemapsFaqBlogs import FaqBlogsViewSitemap
from .sitemapsCoaches import CoachesViewSitemap
from .sitemapsSimpleBlogs import SimpleBlogsViewSitemap

handler404 = 'base.views.error404'
handler400 = 'base.views.error400'
handler500 = 'base.views.error500'

sitemaps = {
    'static': StaticViewSitemap,
    'regions': RegionsViewSitemap,
    'cities': CitiesViewSitemap,
    'countries': CountriesViewSitemap,
    'costs': CostsViewSitemap,
    'blogs': BlogsViewSitemap,
    'faq-blogs': FaqBlogsViewSitemap,
    'simple-blogs': SimpleBlogsViewSitemap,
    'clinics': ClinicsViewSitemap,
    'experts': CoachesViewSitemap,
    'modular-blogs': ModularBlogsViewSitemap,
}

urlpatterns = [
    path('mojeadministrace/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('search.urls')),
    path('', include('packages.urls')),
    path('', include('coaches.urls', namespace='coach_search')),
    path('', include('location.urls')),
    path('', include('blog.urls')),

    path('clinics/', include('clinic.urls', namespace='clinic')),


    path('', include('searchLocationsCities.urls')),
    path('', include('searchLocationsCountries.urls')),
    path('', include('searchLocationsRegionsUS.urls')),
    path('account/', include('owners.urls')),
    path('account/', include('payments.urls')),
    path('account/', include('guestblogging.urls')),
    path('cookies/', include('cookie_consent.urls')),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path(r'captcha/', include('captcha.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
