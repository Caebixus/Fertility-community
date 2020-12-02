from clinic.models import BasicClinic

my_total_count_usa = BasicClinic.objects.filter(clinicState__iexact='United States')
my_total_count_usa = my_total_count_usa.filter(is_published=True)
my_total_count_usa = my_total_count_usa.count()

my_total_count_uk = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
my_total_count_uk = my_total_count_uk.filter(is_published=True)
my_total_count_uk = my_total_count_uk.count()

my_total_count_cze = BasicClinic.objects.filter(clinicState__iexact='Czech Republic')
my_total_count_cze = my_total_count_cze.filter(is_published=True)
my_total_count_cze = my_total_count_cze.count()

my_total_count_spain = BasicClinic.objects.filter(clinicState__iexact='Spain')
my_total_count_spain = my_total_count_spain.filter(is_published=True)
my_total_count_spain = my_total_count_spain.count()

my_total_count_india = BasicClinic.objects.filter(clinicState__iexact='India')
my_total_count_india = my_total_count_india.filter(is_published=True)
my_total_count_india = my_total_count_india.count()

my_total_count_greece = BasicClinic.objects.filter(clinicState__iexact='Greece')
my_total_count_greece = my_total_count_greece.filter(is_published=True)
my_total_count_greece = my_total_count_greece.count()

my_total_count_cyprus = BasicClinic.objects.filter(clinicState__iexact='Cyprus')
my_total_count_cyprus = my_total_count_cyprus.filter(is_published=True)
my_total_count_cyprus = my_total_count_cyprus.count()

CATEGORY_CHOICES_STATES = {
    'US': 'United States - ' + str(my_total_count_usa) + ' fertility clinics',
    'UK': 'United Kingdom - ' + str(my_total_count_uk) + ' fertility clinics',
    'CZ': 'Czech Republic - ' + str(my_total_count_cze) + ' fertility clinics',
    'SP': 'Spain - ' + str(my_total_count_spain) + ' fertility clinics',
    'IN': 'India - ' + str(my_total_count_india) + ' fertility clinics',
    'GR': 'Greece - ' + str(my_total_count_greece) + ' fertility clinics',
    'CY': 'Cyprus - ' + str(my_total_count_greece) + ' fertility clinics',
    }



#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_CZ_CITIES = {
    'Prague': 'Prague',
    'Brno': 'Brno',
    }


#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_GR_CITIES = {
    'Athens': 'Athens',
    'Thessaloniki': 'Thessaloniki',
    }

#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_CY_CITIES = {
    'Nicosia': 'Nicosia',
    'Girne': 'Girne',
    }

#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_SP_CITIES = {
    'Alicante': 'Alicante ',
    'Barcelona': 'Barcelona',
    'Madrid': 'Madrid',
    'Malaga': 'Malaga',
    'Seville': 'Seville',
    'Valencia': 'Valencia',
    }

CATEGORY_CHOICES_US_REGION = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NV': 'Nevada',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
    'DC': 'District of Columbia',
    }

CATEGORY_CHOICES_IN_CITIES = {
    'Amdavad': 'Amdavad',
    'Bangalore': 'Bangalore',
    'Bhopal': 'Bhopal',
    'Bhubaneswar': 'Bhubaneswar',
    'Chandigarh': 'Chandigarh',
    'Chennai': 'Chennai',
    'Dehradun': 'Dehradun',
    'Faridabad': 'Faridabad',
    'Gachibowli': 'Gachibowli',
    'Gurugram': 'Gurugram',
    'Gwalior': 'Gwalior',
    'Haldwani': 'Haldwani',
    'Hyderabad': 'Hyderabad',
    'Indore': 'Indore',
    'Jaipur': 'Jaipur',
    'Jammu': 'Jammu',
    'Jamshedpur': 'Jamshedpur',
    'Kanpur': 'Kanpur',
    'Kochi': 'Kochi',
    'Kolkata': 'Kolkata',
    'Lucknow': 'Lucknow',
    'Ludhiana': 'Ludhiana',
    'Madhapur': 'Madhapur',
    'Meerut': 'Meerut',
    'Mumbai': 'Mumbai',
    'Nagpur': 'Nagpur',
    'New Delhi': 'New Delhi',
    'Noida': 'Noida',
    'Patna': 'Patna',
    'Pune': 'Pune',
    'Raipur': 'Raipur',
    'Ranchi': 'Ranchi',
    'Rohtak': 'Rohtak',
    'Trivandrum': 'Trivandrum',
    'Vadodara': 'Vadodara',
    'Vijayawada': 'Vijayawada',
    'Visakhapatnam': 'Visakhapatnam',
    'Warangal': 'Warangal',
    }

CATEGORY_CHOICES_UK_CITIES = {
    'Aberdeen': 'Aberdeen',
    'Bath': 'Bath',
    'Belfast': 'Belfast',
    'Birmingham': 'Birmingham',
    'Bournemouth': 'Bournemouth',
    'BrightonHove': 'BrightonHove',
    'Bristol': 'Bristol',
    'Cambridge': 'Cambridge',
    'Cardiff': 'Cardiff',
    'Colchester': 'Colchester',
    'Derby': 'Derby',
    'Exeter': 'Exeter',
    'Glasgow': 'Glasgow',
    'Hull': 'Hull',
    'Chelmsford': 'Chelmsford',
    'Leeds': 'Leeds',
    'Leicester': 'Leicester',
    'Liverpool': 'Liverpool',
    'London': 'London',
    'Manchester': 'Manchester',
    'Middlesbrough': 'Middlesbrough',
    'Newcastle': 'Newcastle',
    'Norwich': 'Norwich',
    'Nottingham': 'Nottingham',
    'Oxford': 'Oxford',
    'Peterborough': 'Peterborough',
    'Plymouth': 'Plymouth',
    'Portsmouth': 'Portsmouth',
    'Salisbury': 'Salisbury',
    'Sheffield': 'Sheffield',
    'Southampton': 'Southampton',
    'Swansea': 'Swansea',
    }
