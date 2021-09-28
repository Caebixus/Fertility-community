from django.contrib import admin
from .models import Blog, Author, BestClinicArticleCountry, BestClinicArticleState, BestClinicArticleCity


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ('author_name', 'author_page_url',)

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('id', 'title', 'created_at', 'last_modified', 'blog_url')

class BestClinicArticleCountryAdmin(admin.ModelAdmin):
    model = BestClinicArticleCountry
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('id', 'title', 'created_at', 'last_modified', 'slug')

class BestClinicArticleStateAdmin(admin.ModelAdmin):
    model = BestClinicArticleState
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('id', 'title', 'created_at', 'last_modified', 'slug')

class BestClinicArticleCityAdmin(admin.ModelAdmin):
    model = BestClinicArticleCity
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('id', 'title', 'created_at', 'last_modified', 'slug')

admin.site.register(Author, AuthorAdmin)

admin.site.register(Blog, BlogAdmin)

admin.site.register(BestClinicArticleCountry, BestClinicArticleCountryAdmin)
admin.site.register(BestClinicArticleState, BestClinicArticleStateAdmin)
admin.site.register(BestClinicArticleCity, BestClinicArticleCityAdmin)
