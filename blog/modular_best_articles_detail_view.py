from django.views.generic import DetailView

from .models import ModularBestClinics


class ModularDetailView(DetailView):
    model = ModularBestClinics
    template_name = '../templates/blog/best-ivf-clinics-classed-template/best-clinic.html'
    context_object_name = 'blog'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        simple = self.get_object()
        blogpk = simple.pk

        author = Author.objects.get(pk=simple.author.pk)
        context['author'] = author

        reviewed_by = Coaches.objects.filter(blog_state_best_clinics_review=blogpk)
        context['reviewed_by'] = reviewed_by

        faq_objects = StateBestClinics.objects.filter(pk=blogpk, faq_best_clinic_article_state_reverse__isnull=True)
        context['faq_objects'] = faq_objects

        coach_premium = Coaches.objects.filter(coach_is_premium=True)
        context['coach_premium'] = coach_premium

        BestClinicBlogCountry = BestClinicArticleCountry.objects.filter(best_article_country_noindex_sitemap_boolean=True).order_by('-created_at')
        context['BestClinicBlogCountry'] = BestClinicBlogCountry

        snippets = SnippetSimpleBlog.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
        count_snippets = snippets.count()

        if count_snippets == 1:
            snippets = SnippetSimpleBlog.objects.get(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
            context['snippets'] = snippets
            context['one_snippet'] = 'one_snippet'

        elif count_snippets > 1:
            snippets = SnippetSimpleBlog.objects.filter(blog=blogpk, status='is published', owner__coach_is_premium=True, owner__coach_is_published=True)
            context['snippets'] = snippets
        else:
            pass

        return context