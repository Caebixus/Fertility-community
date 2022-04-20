def count_best_clinics_in_article(basic_queryset):
    best_country_article_count = basic_queryset.filter(best_article_country_boolean=True).exclude(best_article_country_actual_text__exact='')
    best_country_article_count = best_country_article_count.count()
    return best_country_article_count