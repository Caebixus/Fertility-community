from django.contrib import admin
from .models import GuestBlog, GuestAuthor
# Register your models here.
class GuestBlogAdmin(admin.ModelAdmin):
    model = GuestBlog
    list_display = ('id', 'guestblogauthor', 'guestblogtitle', 'guestblogcreatedat', 'guestbloglastmodified',)

class GuestAuthorAdmin(admin.ModelAdmin):
    model = GuestAuthor
    list_display = ('id', 'guestauthor', 'guestauthorname', 'guestauthorlastname')


admin.site.register(GuestBlog, GuestBlogAdmin)

admin.site.register(GuestAuthor, GuestAuthorAdmin)
