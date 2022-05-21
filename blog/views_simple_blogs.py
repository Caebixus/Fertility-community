from blog.models import Author, SimpleBlog, BestClinicArticleCountry
from django.views.generic.detail import DetailView

from coaches.models import Coaches, SnippetSimpleBlog


class SimpleDetailView(DetailView):
    model = SimpleBlog
    template_name = '../templates/blog/simple/simple-detail-view.html'
    context_object_name = 'blog'
    slug_field = 'simple_slug'
    slug_url_kwarg = 'simple_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        simple = self.get_object()
        blogpk = simple.pk

        author = Author.objects.get(pk=simple.author.pk)
        context['author'] = author

        reviewed_by = Coaches.objects.filter(blog_faq_review=blogpk)
        context['reviewed_by'] = reviewed_by



        faq_simple_blog_objects = SimpleBlog.objects.filter(pk=blogpk, faq_simple_blog_reverse__isnull=True)
        context['faq_simple_blog_objects'] = faq_simple_blog_objects



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