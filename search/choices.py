from clinic.models import BasicClinic
from packages.models import Package
from datetime import datetime, timedelta
from django.utils import timezone

todayDate = timezone.now()

#----------------------------------------------------------------------------------------------------------------------------
#Fertility clinics
my_total_count_usa = BasicClinic.objects.filter(clinicState__iexact='United States')
my_total_count_usa = my_total_count_usa.filter(is_published=True)
my_total_count_usa = my_total_count_usa.count()

my_total_count_uk = BasicClinic.objects.filter(clinicState__iexact='United Kingdom')
my_total_count_uk = my_total_count_uk.filter(is_published=True)
my_total_count_uk = my_total_count_uk.count()

my_total_count_denmark = BasicClinic.objects.filter(clinicState__iexact='Denmark')
my_total_count_denmark = my_total_count_denmark.filter(is_published=True)
my_total_count_denmark = my_total_count_denmark.count()

my_total_count_germany = BasicClinic.objects.filter(clinicState__iexact='Germany')
my_total_count_germany = my_total_count_germany.filter(is_published=True)
my_total_count_germany = my_total_count_germany.count()

my_total_count_latvia = BasicClinic.objects.filter(clinicState__iexact='Latvia')
my_total_count_latvia = my_total_count_latvia.filter(is_published=True)
my_total_count_latvia = my_total_count_latvia.count()

my_total_count_portugal = BasicClinic.objects.filter(clinicState__iexact='Portugal')
my_total_count_portugal = my_total_count_portugal.filter(is_published=True)
my_total_count_portugal = my_total_count_portugal.count()

my_total_count_cze = BasicClinic.objects.filter(clinicState__iexact='Czech Republic')
my_total_count_cze = my_total_count_cze.filter(is_published=True)
my_total_count_cze = my_total_count_cze.count()

my_total_count_slovakia = BasicClinic.objects.filter(clinicState__iexact='Slovakia')
my_total_count_slovakia = my_total_count_slovakia.filter(is_published=True)
my_total_count_slovakia = my_total_count_slovakia.count()

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

my_total_count_mexico = BasicClinic.objects.filter(clinicState__iexact='Mexico')
my_total_count_mexico = my_total_count_mexico.filter(is_published=True)
my_total_count_mexico = my_total_count_mexico.count()


CATEGORY_CHOICES_STATES_NORTH_AMERICA = {
    'US': 'United States - ' + str(my_total_count_usa) + ' fertility clinics',
    'MX': 'Mexico - ' + str(my_total_count_mexico) + ' fertility clinics',
    }

CATEGORY_CHOICES_STATES_EUROPE = {
    'UK': 'United Kingdom - ' + str(my_total_count_uk) + ' fertility clinics',
    'DK': 'Denmark - ' + str(my_total_count_denmark) + ' fertility clinics',
    'CZ': 'Czech Republic - ' + str(my_total_count_cze) + ' fertility clinics',
    'SK': 'Slovakia - ' + str(my_total_count_slovakia) + ' fertility clinics',
    'SP': 'Spain - ' + str(my_total_count_spain) + ' fertility clinics',
    'GR': 'Greece - ' + str(my_total_count_greece) + ' fertility clinics',
    'CY': 'Cyprus - ' + str(my_total_count_cyprus) + ' fertility clinics',
    'DE': 'Germany - ' + str(my_total_count_germany) + ' fertility clinics',
    'PT': 'Portugal - ' + str(my_total_count_portugal) + ' fertility clinics',
    'LV': 'Latvia - ' + str(my_total_count_latvia) + ' fertility clinics',
    }

CATEGORY_CHOICES_STATES_ASIA = {
    'IN': 'India - ' + str(my_total_count_india) + ' fertility clinics',
    }

#----------------------------------------------------------------------------------------------------------------------------
#Packages
my_total_package_count_usa = Package.objects.filter(packageclinic__clinicState__iexact='United States').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_usa = my_total_package_count_usa.count()

my_total_package_count_uk = Package.objects.filter(packageclinic__clinicState__iexact='United Kingdom').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_uk = my_total_package_count_uk.count()

my_total_package_count_denmark = Package.objects.filter(packageclinic__clinicState__iexact='Denmark').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_denmark = my_total_package_count_denmark.count()

my_total_package_count_latvia = Package.objects.filter(packageclinic__clinicState__iexact='Latvia').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_latvia = my_total_package_count_latvia.count()

my_total_package_count_germany = Package.objects.filter(packageclinic__clinicState__iexact='Germany').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_germany = my_total_package_count_germany.count()

my_total_package_count_portugal = Package.objects.filter(packageclinic__clinicState__iexact='Portugal').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_portugal = my_total_package_count_portugal.count()

my_total_package_count_cze = Package.objects.filter(packageclinic__clinicState__iexact='Czech Republic').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_cze = my_total_package_count_cze.count()

my_total_package_count_slovakia = Package.objects.filter(packageclinic__clinicState__iexact='Slovakia').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_slovakia = my_total_package_count_slovakia.count()

my_total_package_count_spain = Package.objects.filter(packageclinic__clinicState__iexact='Spain').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_spain = my_total_package_count_spain.count()

my_total_package_count_india = Package.objects.filter(packageclinic__clinicState__iexact='India').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_india = my_total_package_count_india.count()

my_total_package_count_greece = Package.objects.filter(packageclinic__clinicState__iexact='Greece').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_greece = my_total_package_count_greece.count()

my_total_package_count_cyprus = Package.objects.filter(packageclinic__clinicState__iexact='Cyprus').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_cyprus = my_total_package_count_cyprus.count()

my_total_package_count_mexico = Package.objects.filter(packageclinic__clinicState__iexact='Mexico').exclude(package_end_list_date__lte=todayDate).exclude(is_package_active=False)
my_total_package_count_mexico = my_total_package_count_mexico.count()

CATEGORY_CHOICES_STATES_PACKAGES_NORTH_AMERICA = {
    'United': 'United States - ' + str(my_total_package_count_usa) + ' packages',
    'Mexico': 'Mexico - ' + str(my_total_package_count_mexico) + ' packages',
    }

CATEGORY_CHOICES_STATES_PACKAGES_EUROPE = {
    'Cyprus': 'Cyprus - ' + str(my_total_package_count_cyprus) + ' packages',
    'Czech Republic': 'Czech Republic - ' + str(my_total_package_count_cze) + ' packages',
    'Denmark': 'Denmark - ' + str(my_total_package_count_denmark) + ' packages',
    'Germany': 'Germany - ' + str(my_total_package_count_germany) + ' packages',
    'Greece': 'Greece - ' + str(my_total_package_count_greece) + ' packages',
    'Latvia': 'Latvia - ' + str(my_total_package_count_latvia) + ' packages',
    'Portugal': 'Portugal - ' + str(my_total_package_count_portugal) + ' packages',
    'Slovakia': 'Slovakia - ' + str(my_total_package_count_slovakia) + ' packages',
    'Spain': 'Spain - ' + str(my_total_package_count_spain) + ' packages',
    'United Kingdom': 'United Kingdom - ' + str(my_total_package_count_uk) + ' packages',
    }

CATEGORY_CHOICES_STATES_PACKAGES_ASIA = {
    'India': 'India - ' + str(my_total_package_count_india) + ' packages',
    }

#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_MX_CITIES = {
    'Cancún': 'Cancún',
    'Mexico City': 'Mexico City',
    }

#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_DK_CITIES = {
    'Copenhagen': 'Copenhagen',
    }

#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_CZ_CITIES = {
    'Prague': 'Prague',
    'Brno': 'Brno',
    }
#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_SK_CITIES = {
    'Bratislava': 'Bratislava',
    }

#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_SK_CITIES = {
    'Bratislava': 'Bratislava',
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

#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_DE_CITIES = {
    'Berlin': 'Berlin',
}

#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_PT_CITIES = {
    'Lisbon': 'Lisbon',
}

#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_LV_CITIES = {
    'Riga': 'Riga',
}

#----------------------------------------------------------------------------------------------------------------------------
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

#----------------------------------------------------------------------------------------------------------------------------
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

#----------------------------------------------------------------------------------------------------------------------------
CATEGORY_CHOICES_UK_CITIES = {
    'Aberdeen': 'Aberdeen',
    'Bath': 'Bath',
    'Belfast': 'Belfast',
    'Birmingham': 'Birmingham',
    'Bournemouth': 'Bournemouth',
    'Brighton': 'Brighton',
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

#----------------------------------------------------------------------------------------------------------------------------
AL_CITIES = {
    'Birmingham': 'Birmingham',
    'Mobile': 'Mobile',
    }

AZ_CITIES = {
    'Gilbert': 'Gilbert',
    'Mesa': 'Mesa',
    'Scottsdale': 'Scottsdale',
    }

CA_CITIES = {
    'Los Angeles': 'Los Angeles',
    }

CO_CITIES = {
    'Denver': 'Denver',
    }

CT_CITIES = {
    'Norwalk': 'Norwalk',
    'Stamford': 'Stamford',
    'Trumbull': 'Trumbull',
    }

DE_CITIES = {
    'Newark': 'Newark',
    }

FL_CITIES = {
    'Boca Raton': 'Boca Raton',
    'Brandon': 'Brandon',
    'Clearwater': 'Clearwater',
    'Miami': 'Miami',
    'Tampa': 'Tampa',
    'Winter Park': 'Winter Park',
    }

GA_CITIES = {
    'Atlanta': 'Atlanta',
    'Marietta': 'Marietta',
    }

HI_CITIES = {
    'Honolulu': 'Honolulu',
    }

IL_CITIES = {
    'Glenview': 'Glenview',
    'Hoffman Estates': 'Hoffman Estates',
    'Chicago': 'Chicago',
    }

IN_CITIES = {
    'Bloomington': 'Bloomington',
    'Indianapolis': 'Indianapolis',
    'Munster': 'Munster',
    'Valparaiso': 'Valparaiso',
    }

KY_CITIES = {
    'Louisville': 'Louisville',
    }

LA_CITIES = {
    'Baton Rouge': 'Baton Rouge',
    'New Orleans': 'New Orleans',
    }

ME_CITIES = {
    'Bangor': 'Bangor',
    }

MA_CITIES = {
    'Boston': 'Boston',
    }

MO_CITIES = {
    'St. Louis': 'St. Louis',
    }

NV_CITIES = {
    'Las Vegas': 'Las Vegas',
    }

NJ_CITIES = {
    'Hoboken': 'Hoboken',
    'Jersey City': 'Jersey City',
    'Marlton': 'Marlton',
    'Princeton': 'Princeton',
    }

NY_CITIES = {
    'Brooklyn': 'Brooklyn',
    'New York City': 'New York City',
    'Staten Island': 'Staten Island',
    'Syracuse': 'Syracuse',
    }

NC_CITIES = {
    'Charlotte': 'Charlotte',
    }

OH_CITIES = {
    'Akron': 'Akron',
    'West Chester': 'West Chester',
    }

OK_CITIES = {
    'Oklahoma City': 'Oklahoma City',
    }

OR_CITIES = {
    'Portland': 'Portland',
    }

PA_CITIES = {
    'Bethlehem': 'Bethlehem',
    'Lancaster': 'Lancaster',
    'Philadelphia': 'Philadelphia',
    'West Chester': 'West Chester',
    }

TN_CITIES = {
    'Franklin': 'Franklin',
    'Chattanooga': 'Chattanooga',
    'Nashville': 'Nashville',
    }

TX_CITIES = {
    'Austin': 'Austin',
    'Dallas': 'Dallas',
    'Frisco': 'Frisco',
    'Houston': 'Houston',
    'McKinney': 'McKinney',
    'San Antonio': 'San Antonio',
    'Sugar Land': 'Sugar Land',
    'Webster': 'Webster',
    }

VA_CITIES = {
    'Arlington': 'Arlington',
    'Fairfax': 'Fairfax',
    'Reston': 'Reston',
    }

WA_CITIES = {
    'Bellevue': 'Bellevue',
    'Kirkland': 'Kirkland',
    'Seattle': 'Seattle',
    }