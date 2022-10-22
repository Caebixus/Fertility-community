

def count_best_clinics(clinics):
    best_clinics = clinics.filter(modular_city_active=True).exclude(modular_city_actual_text__isnull=True).exclude(
        modular_city_actual_text__exact='')
    return best_clinics.count()
