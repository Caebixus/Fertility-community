from django.views.generic.detail import DetailView

from .models import BasicClinic
from django.contrib.auth.models import User
from packages.models import Package
from django.utils import timezone
from owners.models import ProUser
from guestblogging.models import GuestBlog, GuestAuthor

class ClinicDetailView(DetailView):
    model = BasicClinic
    template_name = '../templates/clinicdetails/clinic-detail-view/base-view/clinic-detail-page-view.html'
    context_object_name = 'clinic'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        allcliniclisting = BasicClinic.objects.all()

        alllisting = allcliniclisting.filter(is_published=True)
        alllisting = alllisting.count()
        context['alllisting'] = alllisting

        listing = BasicClinic.objects.get(pk=self.object.pk)
        pkid = BasicClinic.objects.filter(pk=self.object.pk)
        user = self.request.user

        todayDate = timezone.now()
        package = Package.objects.all().exclude(package_end_list_date__lte=todayDate)
        package = package.filter(packageclinic__id=listing.id)
        context['package'] = package

        author = GuestAuthor.objects.filter(guestauthor_id=pkid)
        context['author'] = author
        guestblog = GuestBlog.objects.filter(guestblogauthor_id__in=author)
        context['author'] = guestblog

        user_owner = User.objects.filter(basicclinic__pk=listing.pk)
        if BasicClinic.objects.filter(clinicOwner_id__in=user_owner).count() >= 2:
            user_objects_count = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=listing.pk).filter(is_claimed=True, is_published=True).count()
            user_objects = BasicClinic.objects.filter(clinicOwner_id__in=user_owner).exclude(id=listing.pk).filter(is_claimed=True, is_published=True)
            context['user_objects_count'] = user_objects_count
            context['user_objects'] = user_objects
        else:
            pass

        if user == user.is_authenticated:
            usergroup = ProUser.objects.all()
            usergroup = usergroup.filter(user=request.user)
            usergroup = usergroup.filter(paidPropublished=True)
            context['usergroup'] = usergroup
        else:
            pass

        return context
