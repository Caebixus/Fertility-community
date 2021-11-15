from django.db import models
from .choices import GUEST_BLOG_TAG_CHOICES
from clinic.models import BasicClinic
from clinic.validators import validate_file_size


class GuestAuthor(models.Model):
    guestauthor = models.ForeignKey(BasicClinic, on_delete=models.CASCADE)
    guestauthorname = models.CharField(max_length=40)
    guestauthorlastname = models.CharField(max_length=40)
    guestauthorpic = models.ImageField(upload_to='guestBloggingPhotos', blank=True, null=True)
    guestauthorpicdelete = models.BooleanField(default=False, blank=True, null=True)
    guestauthordescription = models.TextField()
    guestlinkedinurl = models.URLField(blank=True, null=True)
    guestfacebookurl = models.URLField(blank=True, null=True)
    guesttwitterurl = models.URLField(blank=True, null=True)
    guestadditionalurl = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.guestauthorname) + ' ' + str(self.guestauthorlastname)

class GuestBlog(models.Model):
    guestblogtitle = models.CharField(max_length=200)
    guestblogauthor = models.ForeignKey(GuestAuthor, on_delete=models.CASCADE)
    guestblogdescription = models.TextField()

    guestblogpicblogmain = models.ImageField(upload_to='guestBloggingPhotos', validators=[validate_file_size])
    guestblogpicblog1 = models.ImageField(upload_to='guestBloggingPhotos', blank=True, null=True, validators=[validate_file_size])
    guestblogpicblog2 = models.ImageField(upload_to='guestBloggingPhotos', blank=True, null=True, validators=[validate_file_size])
    guestblogpicblog3 = models.ImageField(upload_to='guestBloggingPhotos', blank=True, null=True, validators=[validate_file_size])

    guestblogcity = models.CharField(max_length=200, blank=True, null=True)
    guestblogregion = models.CharField(max_length=200, blank=True, null=True)
    guestblogcountry = models.CharField(max_length=200, blank=True, null=True)

    guestblogtag = models.CharField(max_length=40, choices=GUEST_BLOG_TAG_CHOICES, null=True)

    guestblogcreatedat = models.DateTimeField(auto_now_add=True)
    guestbloglastmodified = models.DateTimeField(auto_now=True)

    guestblogblogurl = models.URLField(blank=True, null=True)
    guestblogminuteread = models.IntegerField(null=True, blank=True)

    guestblogactive = models.BooleanField(default=False)

    def __str__(self):
        return str(self.guestblogtitle)
