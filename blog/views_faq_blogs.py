from django.shortcuts import render, get_object_or_404
from blog.models import Author, Blog, FAQBlog
from packages.models import Package
from django.utils import timezone
from clinic.models import BasicClinic
from django.db.models import Avg
from django.views.generic.detail import DetailView

from coaches.models import Snippet, Coaches



class FaqDetailView(DetailView):
    model = FAQBlog
    template_name = '../templates/blog/faq/faq-detail-view.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faq = self.get_object()

        author = Author.objects.get(pk=faq.author.pk)
        context['author'] = author

        return context