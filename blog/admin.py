from django.contrib import admin
from .models import Blog, Author, BestClinicArticleCountry, BestClinicArticleState, BestClinicArticleCity, FAQBlog, SimpleBlog


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ('author_name', 'author_page_url',)


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('id', 'tag', 'title', 'created_at', 'last_modified', 'blog_url')


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


class FAQBlogAdmin(admin.ModelAdmin):
    model = FAQBlog
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('id', 'title', 'created_at', 'last_modified', 'slug')

    fieldsets = (
        ('Basic information', {'fields': ('title', 'author', 'description', 'keywords', 'pic_blog', 'last_modified', 'slug', 'minute_read', 'year', 'active',)}),
        ('Content', {'fields': ('content',)}),
        ('FAQ', {'fields': ('faq_simple_blog', 'faq_question', 'faq_answer', )}),
        ('FAQ Old blog', {'fields': ('faq_old_blog', 'faq_old_blog_question', 'faq_old_blog_answer',)}),
        ('FAQ BestClinicArticleCity', {'fields': ('faq_bestclinicarticlecity', 'faq_bestclinicarticlecity_question', 'faq_bestclinicarticlecity_answer',)}),
    )


class SimpleBlogAdmin(admin.ModelAdmin):
    model = SimpleBlog
    prepopulated_fields = {'simple_slug': ('title',), }
    list_display = ('id', 'tag', 'title', 'created_at', 'last_modified', 'simple_slug')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BestClinicArticleCountry, BestClinicArticleCountryAdmin)
admin.site.register(BestClinicArticleState, BestClinicArticleStateAdmin)
admin.site.register(BestClinicArticleCity, BestClinicArticleCityAdmin)
admin.site.register(FAQBlog, FAQBlogAdmin)
admin.site.register(SimpleBlog, SimpleBlogAdmin)
