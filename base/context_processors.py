from django.shortcuts import get_object_or_404

from Fertility.settings import reCAPTCHA
from clinic.models import BasicClinic
from cookies.forms import AllCookiesAccepted
from cookies.models import CookiesConsents, CookieSettings
from owners.models import AuthenticatedUser


def recaptcha(request):
    recaptcha_site_key = reCAPTCHA
    return {
        "recaptcha_site_key": recaptcha_site_key,
    }


def authentication_clinic_coach(request):
    user = request.user
    if user.id != None:
        auth_user = AuthenticatedUser.objects.get(user__id=user.pk)
        return {
            "auth_user": auth_user,
        }
    else:
        return {
            "auth_user": False,
        }


def cookies_check(request):
    cookies_list = request.COOKIES
    cookies_setting = get_object_or_404(CookieSettings, pk=1)

    if 'cookie_variable' in cookies_list:
        cookie_variable = request.COOKIES['cookie_variable']
        if CookiesConsents.objects.filter(custom_cookie=cookie_variable).exists():
            cookies = get_object_or_404(CookiesConsents, custom_cookie=cookie_variable)
            formupdate = AllCookiesAccepted(instance=cookies)
            return {
                "cookies": cookies,
                "formupdate": formupdate,
                "cookies_setting": cookies_setting,
            }
        else:
            formNew = AllCookiesAccepted(request.GET)
            return {
                "formNew": formNew,
                "cookies_setting": cookies_setting,
            }

    else:
        formNew = AllCookiesAccepted(request.GET)
        return {
            "formNew": formNew,
            "cookies_setting": cookies_setting,
        }


def navbar_clinics_count(request):
    clinicsall = BasicClinic.objects.all().exclude(is_published=False)

    ukclinics = clinicsall.filter(clinicState__iexact='United Kingdom')
    ukclinics = ukclinics.count()

    usclinics = clinicsall.filter(clinicState__iexact='United States')
    usclinics = usclinics.count()

    czclinics = clinicsall.filter(clinicState__iexact='Czech Republic')
    czclinics = czclinics.count()

    skclinics = clinicsall.filter(clinicState__iexact='Slovakia')
    skclinics = skclinics.count()

    spclinics = clinicsall.filter(clinicState__iexact='Spain')
    spclinics = spclinics.count()

    declinics = clinicsall.filter(clinicState__iexact='Germany')
    declinics = declinics.count()

    lvclinics = clinicsall.filter(clinicState__iexact='Latvia')
    lvclinics = lvclinics.count()

    ptclinics = clinicsall.filter(clinicState__iexact='Portugal')
    ptclinics = ptclinics.count()

    dkclinics = clinicsall.filter(clinicState__iexact='Denmark')
    dkclinics = dkclinics.count()

    inclinics = clinicsall.filter(clinicState__iexact='India')
    inclinics = inclinics.count()

    grclinics = clinicsall.filter(clinicState__iexact='Greece')
    grclinics = grclinics.count()

    cyclinics = clinicsall.filter(clinicState__iexact='Cyprus')
    cyclinics = cyclinics.count()

    mxclinics = clinicsall.filter(clinicState__iexact='Mexico')
    mxclinics = mxclinics.count()

    #UK CITIES
    londonclinics = clinicsall.filter(clinicRegion__iexact='London')
    londonclinics = londonclinics.count()

    bristolclinics = clinicsall.filter(clinicRegion__iexact='Bristol')
    bristolclinics = bristolclinics.count()

    leedsclinics = clinicsall.filter(clinicRegion__iexact='Leeds')
    leedsclinics = leedsclinics.count()

    nottinghamclinics = clinicsall.filter(clinicRegion__iexact='Nottingham')
    nottinghamclinics = nottinghamclinics.count()

    birminghamclinics = clinicsall.filter(clinicRegion__iexact='Birmingham')
    birminghamclinics = birminghamclinics.count()

    exeterclinics = clinicsall.filter(clinicRegion__iexact='Exeter')
    exeterclinics = exeterclinics.count()

    liverpoolclinics = clinicsall.filter(clinicRegion__iexact='Liverpool')
    liverpoolclinics = liverpoolclinics.count()

    portsmouthclinics = clinicsall.filter(clinicRegion__iexact='Portsmouth')
    portsmouthclinics = portsmouthclinics.count()

    bournemouthclinics = clinicsall.filter(clinicRegion__iexact='Bournemouth')
    bournemouthclinics = bournemouthclinics.count()

    glasgowclinics = clinicsall.filter(clinicRegion__iexact='Glasgow')
    glasgowclinics = glasgowclinics.count()

    manchesterclinics = clinicsall.filter(clinicRegion__iexact='Manchester')
    manchesterclinics = manchesterclinics.count()

    sheffieldclinics = clinicsall.filter(clinicRegion__iexact='Sheffield')
    sheffieldclinics = sheffieldclinics.count()

    #CZ REGIONS
    pragueclinics = clinicsall.filter(clinicRegion__iexact='Prague')
    pragueclinics = pragueclinics.count()

    brnoclinics = clinicsall.filter(clinicRegion__iexact='Brno')
    brnoclinics = brnoclinics.count()

    #SK REGIONS
    bratislavaclinics = clinicsall.filter(clinicRegion__iexact='Bratislava')
    bratislavaclinics = bratislavaclinics.count()

    #US REGIONS
    californiaclinics = clinicsall.filter(clinicRegion__iexact='California')
    californiaclinics = californiaclinics.count()

    alabamaclinics = clinicsall.filter(clinicRegion__iexact='Alabama')
    alabamaclinics = alabamaclinics.count()

    arizonaclinics = clinicsall.filter(clinicRegion__iexact='Arizona')
    arizonaclinics = arizonaclinics.count()

    floridaclinics = clinicsall.filter(clinicRegion__iexact='Florida')
    floridaclinics = floridaclinics.count()

    texasclinics = clinicsall.filter(clinicRegion__iexact='Texas')
    texasclinics = texasclinics.count()

    newyorkclinics = clinicsall.filter(clinicRegion__iexact='New York')
    newyorkclinics = newyorkclinics.count()

    arkansasclinics = clinicsall.filter(clinicRegion__iexact='Arkansas')
    arkansasclinics = arkansasclinics.count()

    coloradoclinics = clinicsall.filter(clinicRegion__iexact='Colorado')
    coloradoclinics = coloradoclinics.count()

    hawaiiclinics = clinicsall.filter(clinicRegion__iexact='Hawaii')
    hawaiiclinics = hawaiiclinics.count()

    pennsylvaniaclinics = clinicsall.filter(clinicRegion__iexact='Pennsylvania')
    pennsylvaniaclinics = pennsylvaniaclinics.count()

    michiganclinics = clinicsall.filter(clinicRegion__iexact='Michigan')
    michiganclinics = michiganclinics.count()

    utahclinics = clinicsall.filter(clinicRegion__iexact='Utah')
    utahclinics = utahclinics.count()

    connecticutclinics = clinicsall.filter(clinicRegion__iexact='Connecticut')
    connecticutclinics = connecticutclinics.count()

    delawareclinics = clinicsall.filter(clinicRegion__iexact='Delaware')
    delawareclinics = delawareclinics.count()

    georgiaclinics = clinicsall.filter(clinicRegion__iexact='Georgia')
    georgiaclinics = georgiaclinics.count()

    illinoisclinics = clinicsall.filter(clinicRegion__iexact='Illinois')
    illinoisclinics = illinoisclinics.count()

    newjerseyclinics = clinicsall.filter(clinicRegion__iexact='New Jersey')
    newjerseyclinics = newjerseyclinics.count()

    #SP REGIONS
    alicanteclinics = clinicsall.filter(clinicRegion__iexact='Alicante')
    alicanteclinics = alicanteclinics.count()

    barcelonaclinics = clinicsall.filter(clinicRegion__iexact='Barcelona')
    barcelonaclinics = barcelonaclinics.count()

    madridclinics = clinicsall.filter(clinicRegion__iexact='Madrid')
    madridclinics = madridclinics.count()

    malagaclinics = clinicsall.filter(clinicRegion__iexact='Malaga')
    malagaclinics = malagaclinics.count()

    sevilleclinics = clinicsall.filter(clinicRegion__iexact='Seville')
    sevilleclinics = sevilleclinics.count()

    valenciaclinics = clinicsall.filter(clinicRegion__iexact='Valencia')
    valenciaclinics = valenciaclinics.count()

    #IN REGIONS
    chennaiclinics = clinicsall.filter(clinicCity__iexact='Chennai')
    chennaiclinics = chennaiclinics.count()

    hyderabadclinics = clinicsall.filter(clinicCity__iexact='Hyderabad')
    hyderabadclinics = hyderabadclinics.count()

    mumbaiclinics = clinicsall.filter(clinicCity__iexact='Mumbai')
    mumbaiclinics = mumbaiclinics.count()

    patnaclinics = clinicsall.filter(clinicCity__iexact='Patna')
    patnaclinics = patnaclinics.count()

    raipurclinics = clinicsall.filter(clinicCity__iexact='Raipur')
    raipurclinics = raipurclinics.count()

    amdavadclinics = clinicsall.filter(clinicCity__iexact='Amdavad')
    amdavadclinics = amdavadclinics.count()

    chandigarhclinics = clinicsall.filter(clinicCity__iexact='Chandigarh')
    chandigarhclinics = chandigarhclinics.count()

    faridabadclinics = clinicsall.filter(clinicCity__iexact='Faridabad')
    faridabadclinics = faridabadclinics.count()

    jamshedpurclinics = clinicsall.filter(clinicCity__iexact='Jamshedpur')
    jamshedpurclinics = jamshedpurclinics.count()

    bangaloreclinics = clinicsall.filter(clinicCity__iexact='Bangalore')
    bangaloreclinics = bangaloreclinics.count()

    trivandrumclinics = clinicsall.filter(clinicCity__iexact='Trivandrum')
    trivandrumclinics = trivandrumclinics.count()

    kochiclinics = clinicsall.filter(clinicCity__iexact='Kochi')
    kochiclinics = kochiclinics.count()

    bhopalclinics = clinicsall.filter(clinicCity__iexact='Bhopal')
    bhopalclinics = bhopalclinics.count()

    indoreclinics = clinicsall.filter(clinicCity__iexact='Indore')
    indoreclinics = indoreclinics.count()

    nagpurclinics = clinicsall.filter(clinicCity__iexact='Nagpur')
    nagpurclinics = nagpurclinics.count()

    bhubaneswarclinics = clinicsall.filter(clinicCity__iexact='Bhubaneswar')
    bhubaneswarclinics = bhubaneswarclinics.count()

    ludhianaclinics = clinicsall.filter(clinicCity__iexact='Ludhiana')
    ludhianaclinics = ludhianaclinics.count()

    jaipurclinics = clinicsall.filter(clinicCity__iexact='Jaipur')
    jaipurclinics = jaipurclinics.count()

    lucknowclinics = clinicsall.filter(clinicCity__iexact='Lucknow')
    lucknowclinics = lucknowclinics.count()

    kanpurclinics = clinicsall.filter(clinicCity__iexact='Kanpur')
    kanpurclinics = kanpurclinics.count()

    dehradunclinics = clinicsall.filter(clinicCity__iexact='Dehradun')
    dehradunclinics = dehradunclinics.count()

    kolkataclinics = clinicsall.filter(clinicCity__iexact='Kolkata')
    kolkataclinics = kolkataclinics.count()

    #GR REGIONS
    athensclinics = clinicsall.filter(clinicCity__iexact='Athens')
    athensclinics = athensclinics.count()

    thessalonikiclinics = clinicsall.filter(clinicCity__iexact='Thessaloniki')
    thessalonikiclinics = thessalonikiclinics.count()

    #CY REGIONS
    nicosiaclinics = clinicsall.filter(clinicCity__iexact='Nicosia')
    nicosiaclinics = nicosiaclinics.count()

    girneclinics = clinicsall.filter(clinicCity__iexact='Girne')
    girneclinics = girneclinics.count()

    #MX REGIONS
    cancunclinics = clinicsall.filter(clinicCity__iexact='Cancún')
    cancunclinics = cancunclinics.count()

    mexicocityclinics = clinicsall.filter(clinicCity__iexact='Mexico City')
    mexicocityclinics = mexicocityclinics.count()

    #DK REGIONS
    copenhagenclinics = clinicsall.filter(clinicCity__iexact='Copenhagen')
    copenhagenclinics = copenhagenclinics.count()

    #PT REGIONS
    lisbonclinics = clinicsall.filter(clinicCity__iexact='Lisbon')
    lisbonclinics = lisbonclinics.count()

    #LV REGIONS
    rigaclinics = clinicsall.filter(clinicCity__iexact='Riga')
    rigaclinics = rigaclinics.count()

    #DE REGIONS
    berlinclinics = clinicsall.filter(clinicCity__iexact='Berlin')
    berlinclinics = berlinclinics.count()

    return {
        'ukclinics': ukclinics,
        'usclinics': usclinics,
        'czclinics': czclinics,
        'skclinics': skclinics,
        'spclinics': spclinics,
        'dkclinics': dkclinics,
        'inclinics': inclinics,
        'grclinics': grclinics,
        'cyclinics': cyclinics,
        'mxclinics': mxclinics,
        'declinics': declinics,
        'ptclinics': ptclinics,
        'lvclinics': lvclinics,

        'londonclinics': londonclinics,
        'bristolclinics': bristolclinics,
        'leedsclinics': leedsclinics,
        'nottinghamclinics': nottinghamclinics,
        'birminghamclinics': birminghamclinics,
        'exeterclinics': exeterclinics,
        'liverpoolclinics': liverpoolclinics,
        'portsmouthclinics': portsmouthclinics,
        'bournemouthclinics': bournemouthclinics,
        'glasgowclinics': glasgowclinics,
        'manchesterclinics': manchesterclinics,
        'sheffieldclinics': sheffieldclinics,

        'pragueclinics': pragueclinics,
        'brnoclinics': brnoclinics,

        'bratislavaclinics': bratislavaclinics,

        'californiaclinics': californiaclinics,
        'alabamaclinics': alabamaclinics,
        'arizonaclinics': arizonaclinics,
        'floridaclinics': floridaclinics,
        'texasclinics': texasclinics,
        'newyorkclinics': newyorkclinics,
        'arkansasclinics': arkansasclinics,
        'coloradoclinics': coloradoclinics,
        'hawaiiclinics': hawaiiclinics,
        'pennsylvaniaclinics': pennsylvaniaclinics,
        'michiganclinics': michiganclinics,
        'utahclinics': utahclinics,
        'connecticutclinics': connecticutclinics,
        'delawareclinics': delawareclinics,
        'georgiaclinics': georgiaclinics,
        'illinoisclinics': illinoisclinics,
        'newjerseyclinics': newjerseyclinics,

        'alicanteclinics': alicanteclinics,
        'barcelonaclinics': barcelonaclinics,
        'madridclinics': madridclinics,
        'malagaclinics': malagaclinics,
        'sevilleclinics': sevilleclinics,
        'valenciaclinics': valenciaclinics,

        'chennaiclinics': chennaiclinics,
        'hyderabadclinics': hyderabadclinics,
        'mumbaiclinics': mumbaiclinics,
        'patnaclinics': patnaclinics,
        'raipurclinics': raipurclinics,
        'amdavadclinics': amdavadclinics,
        'chandigarhclinics': chandigarhclinics,
        'faridabadclinics': faridabadclinics,
        'jamshedpurclinics': jamshedpurclinics,
        'bangaloreclinics': bangaloreclinics,
        'trivandrumclinics': trivandrumclinics,
        'kochiclinics': kochiclinics,
        'bhopalclinics': bhopalclinics,
        'indoreclinics': indoreclinics,
        'nagpurclinics': nagpurclinics,
        'bhubaneswarclinics': bhubaneswarclinics,
        'ludhianaclinics': ludhianaclinics,
        'jaipurclinics': jaipurclinics,
        'lucknowclinics': lucknowclinics,
        'kanpurclinics': kanpurclinics,
        'dehradunclinics': dehradunclinics,
        'kolkataclinics': kolkataclinics,

        'athensclinics': athensclinics,
        'thessalonikiclinics': thessalonikiclinics,

        'nicosiaclinics': nicosiaclinics,
        'girneclinics': girneclinics,

        'cancunclinics': cancunclinics,
        'mexicocityclinics': mexicocityclinics,

        'copenhagenclinics': copenhagenclinics,

        'lisbonclinics': lisbonclinics,

        'rigaclinics': rigaclinics,

        'berlinclinics': berlinclinics,
    }