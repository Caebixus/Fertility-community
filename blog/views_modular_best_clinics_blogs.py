from blog.models import Author, ModularBestClinics, FAQBlog
from django.views.generic.detail import DetailView

from clinic.models import BasicClinic
from coaches.models import Coaches, SnippetModularBestClinicsBlog


class ModularBestClinicsDetailView(DetailView):
    model = ModularBestClinics
    template_name = '../templates/blog/modular-best-clinics/modular.html'
    context_object_name = 'blog'
    slug_field = 'modular_slug'
    slug_url_kwarg = 'modular_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        simple = self.get_object()
        blogpk = simple.pk
        country = simple.country
        state = simple.state
        city = simple.city

        author = Author.objects.get(pk=simple.author.pk)
        context['author'] = author

        reviewed_by = Coaches.objects.filter(blog_modular_best_clinics_review=blogpk)
        context['reviewed_by'] = reviewed_by

        faq_modular_best_clinics_blog_objects = FAQBlog.objects.filter(pk=blogpk, faq_best_clinic_article_state__isnull=True)
        context['faq'] = faq_modular_best_clinics_blog_objects

        coach_premium = Coaches.objects.filter(coach_is_premium=True)
        context['coach_premium'] = coach_premium

        snippets = SnippetModularBestClinicsBlog.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
        count_snippets = snippets.count()

        clinics = BasicClinic.objects.all()
        clinics_modular_country = clinics.filter(modular_country=blogpk)
        clinics_modular_state = clinics.filter(modular_state=blogpk)
        clinics_modular_city = clinics.filter(modular_city=blogpk)


        if clinics_modular_country:
            best_clinics = clinics.filter(modular_country=blogpk).exclude(modular_country_actual_text__exact='').exclude(modular_country_active=False)
            best_clinics = best_clinics.order_by('-digitalTransparencyIndex')
            context['best_clinics'] = best_clinics
            context['best_clinics_count'] = best_clinics.count()
        elif clinics_modular_state:
            best_clinics = clinics.filter(modular_state=blogpk).exclude(modular_state_actual_text__exact='').exclude(modular_state_active=False)
            best_clinics = best_clinics.order_by('-digitalTransparencyIndex')
            context['best_clinics'] = best_clinics
            context['best_clinics_count'] = best_clinics.count()
        elif clinics_modular_city:
            best_clinics = clinics.filter(modular_city=blogpk).exclude(modular_city_actual_text__exact='').exclude(modular_city_active=False)
            best_clinics = best_clinics.order_by('-digitalTransparencyIndex')
            context['best_clinics'] = best_clinics
            context['best_clinics_count'] = best_clinics.count()
        pass

        if country:
            clinics_location_count = clinics.filter(clinicState=country).exclude(is_published=False)
            context['clinics_location_count'] = clinics_location_count.count()
        elif state:
            clinics_location_count = clinics.filter(clinicRegion=state).exclude(is_published=False)
            context['clinics_location_count'] = clinics_location_count.count()
        elif city:
            clinics_location_count = clinics.filter(clinicCity=city).exclude(is_published=False)
            context['clinics_location_count'] = clinics_location_count.count()
        else:
            pass

        if count_snippets == 1:
            snippets = SnippetModularBestClinicsBlog.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
            context['snippets'] = snippets
            context['one_snippet'] = 'one_snippet'

        elif count_snippets > 1:
            snippets = SnippetModularBestClinicsBlog.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
            context['snippets'] = snippets
        else:
            pass

        return context