def count_best_clinics_in_article_city(basic_queryset, place):
    best_city_article_count = basic_queryset.filter(modular_country__city=place)
    best_city_article_count = best_city_article_count.count()
    return best_city_article_count