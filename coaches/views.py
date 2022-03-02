from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Coaches, PreferredLanguage, SnippetNew, Snippet
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from .forms import SnippetForm, SnippetUpdateForm, SnippetCreateForm2
from blog.models import Blog


class CoachDetailView(DetailView):
    model = Coaches
    template_name = '../templates/ivfcoach/coach-detail-view/0base-view.html'
    context_object_name = 'coach'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coach = self.get_object()

        languages = PreferredLanguage.objects.filter(coaches_relationship__coach_user=coach.coach_user)
        context['languages'] = languages

        snippets = Snippet.objects.filter(owner=coach, status='is published')
        context['snippets'] = snippets

        return context


class CoachDeleteView(DeleteView):
    model = Coaches
    template_name = '../templates/ivfcoach/coaches-delete.html'
    success_url = reverse_lazy('coach_dashboard')
    success_message = "- Coach successfully deleted."


def coach_search(request):
    return render(request, 'ivfcoach/fertility-coach-search.html')


@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def SnippetCreateFormView(request, blog_id):
    user = request.user
    coach = Coaches.objects.get(coach_user=user)
    blog = Blog.objects.get(pk=blog_id)

    form = SnippetForm(request.POST or None, request.FILES or None)

    if form.is_valid():
            form = form.save(commit=False)
            form.blog=blog
            form.owner=coach
            form.save()

        # send_mail(
        #     'Coach profile upraven -' + str(form.coach_user),
        #     'Právě někdo upravil svůj profile a je třeba jej ověřit ' +
        #     '\nUser username: ' + str(user.email),
        #     'info@fertilitycommunity.com',
        #     ['David.langr@fertilitycommunity.com'],
        #     fail_silently=False,
        #     )

            messages.success(request, '- Snippet successfully created. Wait for our team to review and publish it.')
            return redirect('coach_dashboard')

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'ivfcoach/snippet-create.html', context)


@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def SnippetCreateFormView2(request, coach_id):
    coach = Coaches.objects.get(pk=coach_id)

    form = SnippetCreateForm2(coach, request.POST or None, request.FILES or None)

    if form.is_valid():
            obj = form.save(commit=False)
            obj.owner=coach
            obj.save()
            form.save_m2m()

            messages.success(request, '- Snippet successfully created. Wait for our team to review and publish it.')
            return redirect('coach_dashboard')

    context = {
        'form': form,
    }

    return render(request, 'ivfcoach/snippet-create-with-coach.html', context)


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

        # send_mail(
        #     'Coach profile upraven -' + str(form.coach_user),
        #     'Právě někdo upravil svůj profile a je třeba jej ověřit ' +
        #     '\nUser username: ' + str(user.email),
        #     'info@fertilitycommunity.com',
        #     ['David.langr@fertilitycommunity.com'],
        #     fail_silently=False,
        #     )

            messages.success(request, '- Snippet successfully created. Wait for our team to review and publish it.')
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