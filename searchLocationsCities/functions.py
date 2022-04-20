def count_best_clinics_in_article_city(basic_queryset):
    best_city_article_count = basic_queryset.filter(best_article_city_boolean=True)
    best_city_article_count = best_city_article_count.count()
    return best_city_article_count