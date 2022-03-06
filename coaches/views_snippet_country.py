from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Coaches, SnippetCountry
from django.views.generic.edit import DeleteView
from .forms import SnippetCountryUpdateForm, SnippetCountryCreateForm
from blog.models import BestClinicArticleCountry

@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def SnippetCountryCreateFormView(request, coach_id):
    coach = Coaches.objects.get(pk=coach_id)

    form = SnippetCountryCreateForm(coach, request.POST or None, request.FILES or None)

    if form.is_valid():
            obj = form.save(commit=False)
            obj.owner=coach
            obj.save()

            send_mail(
                'Snippet - City upraven -' + str(obj.owner),
                'Právě někdo upravil svůj snippet a je třeba jej ověřit ' +
                '\nUser username: ' + str(coach.coach_user),
                'info@fertilitycommunity.com',
                ['David.langr@fertilitycommunity.com'],
                fail_silently=False,
                )

            messages.success(request, '- Snippet successfully created. Wait for our team to review and publish it.')
            return redirect('coach_dashboard')

    context = {
        'form': form,
    }

    return render(request, 'ivfcoach/snippet-country/snippet-country-create.html', context)


@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def SnippetCountryUpdateFormView(request, blog_id, snippet_id):
    user = request.user
    coach = Coaches.objects.get(coach_user=user)
    blog = BestClinicArticleCountry.objects.get(pk=blog_id)
    snippet = SnippetCountry.objects.get(blog=blog_id, owner=coach)

    form = SnippetCountryUpdateForm(request.POST or None, request.FILES or None, instance=snippet)

    if form.is_valid():
            form = form.save(commit=False)
            form.blog=blog
            form.owner=coach
            form.save()

            send_mail(
                'Snippet - City upraven -' + str(form.owner),
                'Právě někdo upravil svůj snippet a je třeba jej ověřit ' +
                '\nUser username: ' + str(coach.coach_user),
                'info@fertilitycommunity.com',
                ['David.langr@fertilitycommunity.com'],
                fail_silently=False,
            )

            messages.success(request, '- Snippet successfully created. Wait for our team to review and publish it.')
            return redirect('coach_dashboard')

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'ivfcoach/snippet-country/snippet-country-update.html', context)


class SnippetCountryDeleteView(DeleteView):
    model = SnippetCountry
    template_name = '../templates/ivfcoach/snippet-country/snippet-country-delete.html'
    success_url = reverse_lazy('coach_dashboard')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, '- Snippet successfully deleted.')
        return response