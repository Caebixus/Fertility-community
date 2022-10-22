

def count_best_clinics_city(clinics):
    best_clinics = clinics.filter(modular_city_active=True).exclude(modular_city_actual_text__isnull=True).exclude(
        modular_city_actual_text__exact='')
    return best_clinics.count()


def count_best_clinics_country(clinics):
    best_clinics = clinics.filter(modular_country_active=True).exclude(modular_country_actual_text__isnull=True).exclude(
        modular_country_actual_text__exact='')
    return best_clinics.count()