from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Coaches, Snippet, SnippetCity
from django.views.generic.edit import DeleteView
from .forms import SnippetCityUpdateForm, SnippetCityCreateForm
from blog.models import BestClinicArticleCity

@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def SnippetCityCreateFormView(request, coach_id):
    coach = Coaches.objects.get(pk=coach_id)

    form = SnippetCityCreateForm(coach, request.POST or None, request.FILES or None)

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

    return render(request, 'ivfcoach/snippet-city/snippet-city-create.html', context)


@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def SnippetCityUpdateFormView(request, blog_id, snippet_id):
    user = request.user
    coach = Coaches.objects.get(coach_user=user)
    blog = BestClinicArticleCity.objects.get(pk=blog_id)
    snippet = SnippetCity.objects.get(blog=blog_id, owner=coach)

    form = SnippetCityUpdateForm(request.POST or None, request.FILES or None, instance=snippet)

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

    return render(request, 'ivfcoach/snippet-city/snippet-city-update.html', context)


class SnippetCityDeleteView(DeleteView):
    model = SnippetCity
    template_name = '../templates/ivfcoach/snippet-city/snippet-city-delete.html'
    success_url = reverse_lazy('coach_dashboard')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, '- Snippet successfully deleted.')
        return response