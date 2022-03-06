from django.contrib import admin
from .models import Coaches, TypeJobs, PreferredLanguage, PreferredCountry, Snippet, SnippetCity, SnippetCountry, SnippetState


class CoachesAdmin(admin.ModelAdmin):
    model = Coaches
    list_display = ('id', 'coach_user', 'coach_full_name', 'coach_username', 'coach_is_published', 'coach_is_not_approved', 'coach_is_premium', 'coach_created')

admin.site.register(Coaches, CoachesAdmin)


class SnippetAdmin(admin.ModelAdmin):
    model = Snippet
    list_display = ('id', 'owner', 'blog', 'blog_id', 'status')

admin.site.register(Snippet, SnippetAdmin)

class SnippetCityAdmin(admin.ModelAdmin):
    model = SnippetCity
    list_display = ('id', 'owner', 'blog', 'blog_id', 'status')

admin.site.register(SnippetCity, SnippetCityAdmin)

class SnippetCountryAdmin(admin.ModelAdmin):
    model = SnippetCountry
    list_display = ('id', 'owner', 'blog', 'blog_id', 'status')

admin.site.register(SnippetCountry, SnippetCountryAdmin)

class SnippetStateAdmin(admin.ModelAdmin):
    model = SnippetState
    list_display = ('id', 'owner', 'blog', 'blog_id', 'status')

admin.site.register(SnippetState, SnippetStateAdmin)

class TypeJobsAdmin(admin.ModelAdmin):
    model = TypeJobs
    list_display = ('type_of_job', 'id',)

admin.site.register(TypeJobs, TypeJobsAdmin)


class PreferredLanguageAdmin(admin.ModelAdmin):
    model = PreferredLanguage
    list_display = ('preferred_language', 'id',)

admin.site.register(PreferredLanguage, PreferredLanguageAdmin)


class PreferredCountryAdmin(admin.ModelAdmin):
    model = PreferredCountry
    list_display = ('preferred_country', 'id',)

admin.site.register(PreferredCountry, PreferredCountryAdmin)