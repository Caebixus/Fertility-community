from blog.models import Author, SimpleBlog
from django.views.generic.detail import DetailView

from coaches.models import Coaches



class SimpleDetailView(DetailView):
    model = SimpleBlog
    template_name = '../templates/blog/simple/simple-detail-view.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faq = self.get_object()

        author = Author.objects.get(pk=faq.author.pk)
        context['author'] = author

        reviewed_by = Coaches.objects.filter(blog_faq_review=faq.pk)
        context['reviewed_by'] = reviewed_by

        coach_premium = Coaches.objects.filter(coach_is_premium=True)
        context['coach_premium'] = coach_premium

        BestClinicBlogCountry = BestClinicArticleCountry.objects.filter(best_article_country_noindex_sitemap_boolean=True).order_by('-created_at')
        context['BestClinicBlogCountry'] = BestClinicBlogCountry

        return context