from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .views import dashboard
from .models import SingleClinicBestArticleText
from .forms import Singleclinicbestarticleform, Singleclinicbestarticleupdateform


@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def bestclinicworldsettings(request):
    current_user = request.user
    form = Singleclinicbestarticleform(current_user, request.POST or None, request.FILES or None)
    user_owner = User.objects.filter(basicclinic__pk=current_user.pk).count()

    if request.method == 'POST':
        if form.is_valid():
            if user_owner >= 1:
                form = form.save(commit=False)
                form.user = current_user
                form.save()

                messages.success(request, '- information updated')
                return redirect(dashboard)
            else:
                messages.error(request, '- cannot create another')
                return redirect(bestclinicworldsettings)

    context = {
        'form': form,
    }

    return render(request, 'owners/single-clinic-best-article-text/best-world-clinic-settings.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def bestclinicworldsettingsupdate(request, bestclinicworldsettingsupdate_id):
    instance = get_object_or_404(SingleClinicBestArticleText, pk=bestclinicworldsettingsupdate_id)
    current_user = request.user
    form = Singleclinicbestarticleupdateform(current_user, request.POST or None, request.FILES or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            messages.success(request, '- information updated')
            return redirect(dashboard)

    context = {
        'instance': instance,
        'form': form,
    }

    return render(request, 'owners/single-clinic-best-article-text/best-world-clinic-settings-update.html', context)