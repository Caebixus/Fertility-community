from blog.models import Author, SimpleBlog, BestClinicArticleCountry
from django.views.generic.detail import DetailView

from coaches.models import Coaches


class SimpleDetailView(DetailView):
    model = SimpleBlog
    template_name = '../templates/blog/simple/simple-detail-view.html'
    context_object_name = 'blog'
    slug_field = 'simple_slug'
    slug_url_kwarg = 'simple_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        simple = self.get_object()

        author = Author.objects.get(pk=simple.author.pk)
        context['author'] = author

        reviewed_by = Coaches.objects.filter(blog_faq_review=simple.pk)
        context['reviewed_by'] = reviewed_by

        coach_premium = Coaches.objects.filter(coach_is_premium=True)
        context['coach_premium'] = coach_premium

        BestClinicBlogCountry = BestClinicArticleCountry.objects.filter(best_article_country_noindex_sitemap_boolean=True).order_by('-created_at')
        context['BestClinicBlogCountry'] = BestClinicBlogCountry

        return context