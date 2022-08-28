from coaches.models import Coaches

CATEGORY_CHOICES_LANGUAGES = (
    ('English', 'English'),
    ('German', 'German'),
    ('Spanish', 'Spanish'),
    ('Portuguese', 'Portuguese'),
    ('Russian', 'Russian'),
    ('Chinese', 'Chinese'),
)

CATEGORY_TYPE = (
    ('Fertility Coach', 'Fertility Coach'),
    ('Fertility Specialist', 'Fertility Specialist'),
    ('Reproductive Endocrinologist', 'Reproductive Endocrinologist'),
    ('Andrologist', 'Andrologist'),
    ('Reproductive Surgeon', 'Reproductive Surgeon'),
    ('Reproductive Immunologist', 'Reproductive Immunologist'),
    ('Obstetrician', 'Obstetrician'),
    ('Gynecologist', 'Gynecologist'),
    )


#----------------------------------------------------------------------------------------------------------------------------
def coach_country_search():
    coaches = Coaches.objects.filter(coach_is_published=True, coach_is_claimed=True).order_by('coach_preferred_client_country')
    coaches_dict = {}
    for coach in coaches:
        key = coach.coach_preferred_client_country
        value = Coaches.objects.filter(coach_preferred_client_country=key).count()
        coaches_dict[key] = value

    return coaches_dict


# def coach_country_search():
#     coaches = Coaches.objects.filter(coach_is_published=True, coach_is_claimed=True)
#     coaches_list = []
#     for coach in coaches:
#         coaches_list.append(coach.coach_preferred_client_country)
#
#     final_dict = dict.fromkeys(coaches_list, 'country')
#
#     return final_dict