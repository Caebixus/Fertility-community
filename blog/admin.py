from django.contrib import admin
from .models import Blog, Author


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('id', 'title', 'created_at', 'last_modified', 'blog_url',)

class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ('author_name', 'author_page_url',)


admin.site.register(Blog, BlogAdmin)

admin.site.register(Author, AuthorAdmin)
