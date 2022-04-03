from django.contrib import admin
from .models import Coaches, TypeJobs, PreferredLanguage, PreferredCountry, Snippet, SnippetCity, SnippetCountry, SnippetState


class CoachesAdmin(admin.ModelAdmin):
    model = Coaches
    list_display = ('id', 'coach_user', 'coach_full_name', 'coach_username', 'coach_is_published', 'coach_is_not_approved', 'coach_is_premium', 'coach_created')
    fieldsets = (
        ('Basic information', {'fields': ('coach_user', 'coach_full_name', 'coach_username', 'coach_profile_photo', 'coach_bio', 'coach_education', 'coach_specialization', 'coach_certification', 'coach_other',)}),
        ('Contact', {'fields': ('coach_contact_email', 'coach_phone',)}),
        ('Reviewed blogs', {'fields': ('blog_review', 'blog_best_country_review', 'blog_best_city_review', 'blog_best_state_review',)}),
        ('Social', {'fields': ('coach_social_instagram', 'coach_social_facebook', 'coach_social_linkedin', 'coach_social_pinterest', 'coach_social_twitter', 'coach_social_youtube', 'coach_social_website',)}),
        ('Intern', {'fields': ('coach_is_published', 'coach_is_not_approved', 'coach_is_premium', 'coach_created', 'coach_updated', 'coach_subscription_update',)}),
    )
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