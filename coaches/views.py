from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView

from .models import Coaches, PreferredLanguage, Snippet, TypeJobs, SnippetCity, SnippetState, SnippetCountry, SnippetSimpleBlog, SnippetModularBestClinicsBlog
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from .forms import SnippetUpdateForm, SnippetCreateForm2
from blog.models import Blog, FAQBlog

from coaches.choices import coach_country_search
from itertools import chain



class CoachDetailView(DetailView):
    model = Coaches
    template_name = '../templates/ivfcoach/coach-detail-view/0base-view.html'
    context_object_name = 'coach'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coach = self.get_object()

        languages = PreferredLanguage.objects.filter(coaches_relationship__coach_user=coach.coach_user)
        context['languages'] = languages

        jobs = TypeJobs.objects.filter(coaches_relationship__coach_user=coach.coach_user)
        context['jobs'] = jobs

        if jobs.filter(type_of_job="Gynecologist"):
            context['gynecologist'] = True

        snippets = Snippet.objects.filter(owner=coach, status='is published')
        snippetCity = SnippetCity.objects.filter(owner=coach, status='is published')
        snippetState = SnippetState.objects.filter(owner=coach, status='is published')
        snippetCountry = SnippetCountry.objects.filter(owner=coach, status='is published')
        snippetSimpleBlog = SnippetSimpleBlog.objects.filter(owner=coach, status='is published')
        snippetModularBestClinicsBlog = SnippetModularBestClinicsBlog.objects.filter(owner=coach, status='is published')

        context['snippets'] = list(chain(snippets, snippetCity, snippetState, snippetCountry, snippetSimpleBlog, snippetModularBestClinicsBlog))

        return context


class CoachDeleteView(DeleteView):
    model = Coaches
    template_name = '../templates/ivfcoach/coaches-delete.html'
    success_url = reverse_lazy('coach_dashboard')
    success_message = "- Coach successfully deleted."


@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def SnippetCreateFormView(request, coach_id):
    coach = Coaches.objects.get(pk=coach_id)

    form = SnippetCreateForm2(coach, request.POST or None, request.FILES or None)

    if form.is_valid():
            obj = form.save(commit=False)
            obj.owner=coach
            obj.save()

            send_mail(
                'Snippet vytvořen -' + str(obj.owner),
                'Právě někdo upravil svůj profile a je třeba jej ověřit ' +
                '\nUser username: ' + str(coach.coach_user),
                'info@fertilitycommunity.com',
                ['David.langr@fertilitycommunity.com'],
                fail_silently=False,
            )

            messages.success(request, '- Comment successfully created. Wait for our team to review and publish it.')
            return redirect('coach_dashboard')

    context = {
        'form': form,
    }

    return render(request, 'ivfcoach/snippet-create.html', context)


@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def SnippetUpdateFormView(request, blog_id, snippet_id):
    user = request.user
    coach = Coaches.objects.get(coach_user=user)
    blog = Blog.objects.get(pk=blog_id)
    snippet = Snippet.objects.get(blog=blog_id, owner=coach)

    form = SnippetUpdateForm(request.POST or None, request.FILES or None, instance=snippet)

    if form.is_valid():
            form = form.save(commit=False)
            form.blog=blog
            form.owner=coach
            form.save()

            send_mail(
                'Snippet upraven -' + str(form.owner),
                'Právě někdo upravil svůj profile a je třeba jej ověřit ' +
                '\nUser username: ' + str(user.email),
                'info@fertilitycommunity.com',
                ['David.langr@fertilitycommunity.com'],
                fail_silently=False,
                )

            messages.success(request, '- Comment successfully created. Wait for our team to review and publish it.')
            return redirect('coach_dashboard')

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'ivfcoach/snippet-update.html', context)


class SnippetDeleteView(DeleteView):
    model = Snippet
    template_name = '../templates/ivfcoach/snippet-delete.html'
    success_url = reverse_lazy('coach_dashboard')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, '- Snippet successfully deleted.')
        return response

class CoachListView(ListView):
    model = Coaches
    template_name = 'ivfcoach/fertility-specialists.html'
    order_by = 'order_by'
    context_object_name = 'order_data'
    paginate_by = 100
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super(CoachListView, self).get_context_data(**kwargs)
        context['countries'] = coach_country_search()
        context['values'] = self.request.GET
        context['blog'] = FAQBlog.objects.filter(id=29)

        snippets = Snippet.objects.filter(status='is published')[:3]
        snippetCity = SnippetCity.objects.filter(status='is published')[:1]
        snippetState = SnippetState.objects.filter(status='is published')[:1]
        snippetCountry = SnippetCountry.objects.filter(status='is published')[:1]
        snippetSimpleBlog = SnippetSimpleBlog.objects.filter(status='is published')[:3]
        snippetModularBestClinicsBlog = SnippetModularBestClinicsBlog.objects.filter(status='is published')[:3]

        context['snippets'] = list(chain(snippets, snippetCity, snippetState, snippetCountry, snippetSimpleBlog, snippetModularBestClinicsBlog))

        if "States" in self.request.GET.keys():
            count_coaches = Coaches.objects.filter(coach_is_published=True, coach_is_claimed=True, coach_preferred_client_country=self.request.GET['States']).count()
            context['count_coaches'] = count_coaches
        else:
            count_coaches = Coaches.objects.filter(coach_is_published=True, coach_is_claimed=True).count()
            context['count_coaches'] = count_coaches

        return context

    def get_queryset(self, **kwargs):
        queryset = super(CoachListView, self).get_queryset(**kwargs)
        if kwargs:
            queryset = queryset.filter(**kwargs)
        queryset = queryset.filter(coach_is_published=True, coach_is_claimed=True)


        values = self.request.GET
        if 'States' in values.keys():
            states = self.request.GET['States']
            if states == None or states == '':
                states = 'empty'
        else:
            states = 'empty'

        if states != 'empty':
            queryset = queryset.filter(coach_preferred_client_country__iexact=states)

        return queryset