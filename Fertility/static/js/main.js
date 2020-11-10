<!-- DISPLAY REGION FORM IF UNITED STATES IS SELECTED | OWNERS --->
$(document).ready(function (e) {
    $('#ChooseCurrency').change(function () {
        if ($(this).val() == 'USD') {
            $('#usdBoard1a').show();
            $('#usdBoard1b').show();
            $('#usdBoard1c').show();
            $('#usdBoard1d').show();
            $('#eurBoard2a').hide();
            $('#eurBoard2b').hide();
            $('#eurBoard2c').hide();
            $('#eurBoard2d').hide();
            $('#gbpBoard3a').hide();
            $('#gbpBoard3b').hide();
            $('#gbpBoard3c').hide();
            $('#gbpBoard3d').hide();
            $('#defaultBoard1a').hide();
            $('#defaultBoard1b').hide();
            $('#defaultBoard1c').hide();
            $('#defaultBoard1d').hide();
        } else if ($(this).val() == 'EUR') {
            $('#usdBoard1a').hide();
            $('#usdBoard1b').hide();
            $('#usdBoard1c').hide();
            $('#usdBoard1d').hide();
            $('#eurBoard2a').show();
            $('#eurBoard2b').show();
            $('#eurBoard2c').show();
            $('#eurBoard2d').show();
            $('#gbpBoard3a').hide();
            $('#gbpBoard3b').hide();
            $('#gbpBoard3c').hide();
            $('#gbpBoard3d').hide();
            $('#defaultBoard1a').hide();
            $('#defaultBoard1b').hide();
            $('#defaultBoard1c').hide();
            $('#defaultBoard1d').hide();
        } else if ($(this).val() == 'GBP') {
            $('#usdBoard1a').hide();
            $('#usdBoard1b').hide();
            $('#usdBoard1c').hide();
            $('#usdBoard1d').hide();
            $('#eurBoard2a').hide();
            $('#eurBoard2b').hide();
            $('#eurBoard2c').hide();
            $('#eurBoard2d').hide();
            $('#gbpBoard3a').show();
            $('#gbpBoard3b').show();
            $('#gbpBoard3c').show();
            $('#gbpBoard3d').show();
            $('#defaultBoard1a').hide();
            $('#defaultBoard1b').hide();
            $('#defaultBoard1c').hide();
            $('#defaultBoard1d').hide();
        } else {
            $('#usdBoard1a').hide();
            $('#usdBoard1b').hide();
            $('#usdBoard1c').hide();
            $('#usdBoard1d').hide();
            $('#eurBoard2a').hide();
            $('#eurBoard2b').hide();
            $('#eurBoard2c').hide();
            $('#eurBoard2d').hide();
            $('#gbpBoard3a').hide();
            $('#gbpBoard3b').hide();
            $('#gbpBoard3c').hide();
            $('#gbpBoard3d').hide();
            $('#defaultBoard1a').show();
            $('#defaultBoard1b').show();
            $('#defaultBoard1c').show();
            $('#defaultBoard1d').show();
        }
    });
});


<!-- DISPLAY REGION FORM IF UNITED STATES IS SELECTED | OWNERS --->
$(document).ready(function (e) {
    $('#id_clinicState').change(function () {
        if ($(this).val() == 'US') {
            $('#Regionsx').show();
        } else {
            $('#Regionsx').hide();
        }
    });
});


<!-- ADD CLINIC FORMULÁŘ --->
<!-- 1. řádka --->
$('#ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_ivf_cost').show();
  } else {
    $('#js_ivf_cost').hide();
  }
});

$('#id_ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_ivf_cost').show();
  } else {
    $('#js_ivf_cost').hide();
  }
});

$('#mild_ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_mild_ivf_cost').show();
  } else {
    $('#js_mild_ivf_cost').hide();
  }
});

$('#id_mild_ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_mild_ivf_cost').show();
  } else {
    $('#js_mild_ivf_cost').hide();
  }
});

$('#ovarian_ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_ovarian_ivf_cost').show();
  } else {
    $('#js_ovarian_ivf_cost').hide();
  }
});

$('#id_ovarian_ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_ovarian_ivf_cost').show();
  } else {
    $('#js_ovarian_ivf_cost').hide();
  }
});



<!-- 2. řádka --->
$('#iui_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_iui_cost').show();
  } else {
    $('#js_iui_cost').hide();
  }
});

$('#id_iui_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_iui_cost').show();
  } else {
    $('#js_iui_cost').hide();
  }
});

$('#icsi_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_icsi_cost').show();
  } else {
    $('#js_icsi_cost').hide();
  }
});

$('#id_icsi_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_icsi_cost').show();
  } else {
    $('#js_icsi_cost').hide();
  }
});

<!-- 3. řádka --->

$('#egg_donation').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_egg_cost').show();
  } else {
    $('#js_egg_cost').hide();
  }
});

$('#id_egg_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_egg_cost').show();
  } else {
    $('#js_egg_cost').hide();
  }
});

$('#sperm_donation').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_sperm_cost').show();
  } else {
    $('#js_sperm_cost').hide();
  }
});

$('#id_sperm_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_sperm_cost').show();
  } else {
    $('#js_sperm_cost').hide();
  }
});

$('#embryo_donation').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_embryo_cost').show();
  } else {
    $('#js_embryo_cost').hide();
  }
});

$('#id_embryo_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_embryo_cost').show();
  } else {
    $('#js_embryo_cost').hide();
  }
});

<!-- 4. řádka --->

$('#egg_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_egg_freezing').show();
  } else {
    $('#js_egg_freezing').hide();
  }
});

$('#id_egg_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_egg_freezing').show();
  } else {
    $('#js_egg_freezing').hide();
  }
});

$('#embryo_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_embryo_freezing').show();
  } else {
    $('#js_embryo_freezing').hide();
  }
});

$('#id_embryo_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_embryo_freezing').show();
  } else {
    $('#js_embryo_freezing').hide();
  }
});

$('#sperm_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_sperm_freezing').show();
  } else {
    $('#js_sperm_freezing').hide();
  }
});

$('#id_sperm_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_sperm_freezing').show();
  } else {
    $('#js_sperm_freezing').hide();
  }
});

$('#assisted_hatching').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_assisted_hatching').show();
  } else {
    $('#js_assisted_hatching').hide();
  }
});

<!-- 5. řádka --->

$('#surrogacy').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_surrogacy_cost').show();
  } else {
    $('#js_surrogacy_cost').hide();
  }
});

$('#id_surrogacy').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_surrogacy_cost').show();
  } else {
    $('#js_surrogacy_cost').hide();
  }
});

$('#pgd').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_pgd_cost').show();
  } else {
    $('#js_pgd_cost').hide();
  }
});

$('#vasectomy_reversal').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_vasectomy_reversal').show();
  } else {
    $('#js_vasectomy_reversal').hide();
  }
});

if (localStorage.getItem('cookieSeen') != 'shown') {
  $('.cookie-banner').delay(2000).show();
  localStorage.setItem('cookieSeen','shown')
};

$('.close').click(function() {
  $('.cookie-banner').hide(1000);
})

$('#myCarousel').carousel({
    interval: 10000
})

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$(function () {
  $('[data-toggle="popover"]').popover()
})

$("body").on("contextmenu",function(e){
     return false;
});

$("img").mousedown(function(e){
     e.preventDefault()
});


<!-- DISPLAY SELECTED CURRENCY ON US | MAIN/LOCATIONS --->
$(document).ready(function (e) {
    $('#ChooseCurrencyUS').change(function () {
        if ($(this).val() == 'USD') {
          $('#usdAlabama').show();
          $('#usdAlaska').show();
          $('#usdArizona').show();
          $('#usdArkansas').show();
          $('#usdCalifornia').show();
          $('#usdColorado').show();
          $('#usdConnecticut').show();
          $('#usdDelaware').show();
          $('#usdFlorida').show();
          $('#usdGeorgia').show();
          $('#usdHawaii').show();
          $('#usdIdaho').show();
          $('#usdIllinois').show();
          $('#usdIndiana').show();
          $('#usdIowa').show();
          $('#usdKansas').show();
          $('#usdKentucky').show();
          $('#usdLouisiana').show();
          $('#usdMaine').show();
          $('#usdMaryland').show();
          $('#usdMassachusetts').show();
          $('#usdMichigan').show();
          $('#usdMinnesota').show();
          $('#usdMississippi').show();
          $('#usdMissouri').show();
          $('#usdMontana').show();
          $('#usdNebraska').show();
          $('#usdNewHampshire').show();
          $('#usdNewJersey').show();
          $('#usdNewMexico').show();
          $('#usdNewYork').show();
          $('#usdNorthCarolina').show();
          $('#usdNorthDakota').show();
          $('#usdNevada').show();
          $('#usdOhio').show();
          $('#usdOklahoma').show();
          $('#usdOregon').show();
          $('#usdPennsylvania').show();
          $('#usdPuertoRico').show();
          $('#usdRhodeIsland').show();
          $('#usdSouthCarolina').show();
          $('#usdSouthDakota').show();
          $('#usdTennessee').show();
          $('#usdTexas').show();
          $('#usdUtah').show();
          $('#usdVermont').show();
          $('#usdVirginia').show();
          $('#usdWashington').show();
          $('#usdWestVirginia').show();
          $('#usdWisconsin').show();
          $('#usdWyoming').show();
          $('#usdDistrictOfColumbia').show();

          $('#eurAlabama').hide();
          $('#eurAlaska').hide();
          $('#eurArizona').hide();
          $('#eurArkansas').hide();
          $('#eurCalifornia').hide();
          $('#eurColorado').hide();
          $('#eurConnecticut').hide();
          $('#eurDelaware').hide();
          $('#eurFlorida').hide();
          $('#eurGeorgia').hide();
          $('#eurHawaii').hide();
          $('#eurIdaho').hide();
          $('#eurIllinois').hide();
          $('#eurIndiana').hide();
          $('#eurIowa').hide();
          $('#eurKansas').hide();
          $('#eurKentucky').hide();
          $('#eurLouisiana').hide();
          $('#eurMaine').hide();
          $('#eurMaryland').hide();
          $('#eurMassachusetts').hide();
          $('#eurMichigan').hide();
          $('#eurMinnesota').hide();
          $('#eurMississippi').hide();
          $('#eurMissouri').hide();
          $('#eurMontana').hide();
          $('#eurNebraska').hide();
          $('#eurNewHampshire').hide();
          $('#eurNewJersey').hide();
          $('#eurNewMexico').hide();
          $('#eurNewYork').hide();
          $('#eurNorthCarolina').hide();
          $('#eurNorthDakota').hide();
          $('#eurNevada').hide();
          $('#eurOhio').hide();
          $('#eurOklahoma').hide();
          $('#eurOregon').hide();
          $('#eurPennsylvania').hide();
          $('#eurPuertoRico').hide();
          $('#eurRhodeIsland').hide();
          $('#eurSouthCarolina').hide();
          $('#eurSouthDakota').hide();
          $('#eurTennessee').hide();
          $('#eurTexas').hide();
          $('#eurUtah').hide();
          $('#eurVermont').hide();
          $('#eurVirginia').hide();
          $('#eurWashington').hide();
          $('#eurWestVirginia').hide();
          $('#eurWisconsin').hide();
          $('#eurWyoming').hide();
          $('#eurDistrictOfColumbia').hide();

          $('#gbpAlabama').hide();
          $('#gbpAlaska').hide();
          $('#gbpArizona').hide();
          $('#gbpArkansas').hide();
          $('#gbpCalifornia').hide();
          $('#gbpColorado').hide();
          $('#gbpConnecticut').hide();
          $('#gbpDelaware').hide();
          $('#gbpFlorida').hide();
          $('#gbpGeorgia').hide();
          $('#gbpHawaii').hide();
          $('#gbpIdaho').hide();
          $('#gbpIllinois').hide();
          $('#gbpIndiana').hide();
          $('#gbpIowa').hide();
          $('#gbpKansas').hide();
          $('#gbpKentucky').hide();
          $('#gbpLouisiana').hide();
          $('#gbpMaine').hide();
          $('#gbpMaryland').hide();
          $('#gbpMassachusetts').hide();
          $('#gbpMichigan').hide();
          $('#gbpMinnesota').hide();
          $('#gbpMississippi').hide();
          $('#gbpMissouri').hide();
          $('#gbpMontana').hide();
          $('#gbpNebraska').hide();
          $('#gbpNewHampshire').hide();
          $('#gbpNewJersey').hide();
          $('#gbpNewMexico').hide();
          $('#gbpNewYork').hide();
          $('#gbpNorthCarolina').hide();
          $('#gbpNorthDakota').hide();
          $('#gbpNevada').hide();
          $('#gbpOhio').hide();
          $('#gbpOklahoma').hide();
          $('#gbpOregon').hide();
          $('#gbpPennsylvania').hide();
          $('#gbpPuertoRico').hide();
          $('#gbpRhodeIsland').hide();
          $('#gbpSouthCarolina').hide();
          $('#gbpSouthDakota').hide();
          $('#gbpTennessee').hide();
          $('#gbpTexas').hide();
          $('#gbpUtah').hide();
          $('#gbpVermont').hide();
          $('#gbpVirginia').hide();
          $('#gbpWashington').hide();
          $('#gbpWestVirginia').hide();
          $('#gbpWisconsin').hide();
          $('#gbpWyoming').hide();
          $('#gbpDistrictOfColumbia').hide();

          $('#defaultBoardAlabama').hide();
          $('#defaultBoardAlaska').hide();
          $('#defaultBoardArizona').hide();
          $('#defaultBoardArkansas').hide();
          $('#defaultBoardCalifornia').hide();
          $('#defaultBoardColorado').hide();
          $('#defaultBoardConnecticut').hide();
          $('#defaultBoardDelaware').hide();
          $('#defaultBoardFlorida').hide();
          $('#defaultBoardGeorgia').hide();
          $('#defaultBoardHawaii').hide();
          $('#defaultBoardIdaho').hide();
          $('#defaultBoardIllinois').hide();
          $('#defaultBoardIndiana').hide();
          $('#defaultBoardIowa').hide();
          $('#defaultBoardKansas').hide();
          $('#defaultBoardKentucky').hide();
          $('#defaultBoardLouisiana').hide();
          $('#defaultBoardMaine').hide();
          $('#defaultBoardMaryland').hide();
          $('#defaultBoardMassachusetts').hide();
          $('#defaultBoardMichigan').hide();
          $('#defaultBoardMinnesota').hide();
          $('#defaultBoardMississippi').hide();
          $('#defaultBoardMissouri').hide();
          $('#defaultBoardMontana').hide();
          $('#defaultBoardNebraska').hide();
          $('#defaultBoardNewHampshire').hide();
          $('#defaultBoardNewJersey').hide();
          $('#defaultBoardNewMexico').hide();
          $('#defaultBoardNewYork').hide();
          $('#defaultBoardNorthCarolina').hide();
          $('#defaultBoardNorthDakota').hide();
          $('#defaultBoardNevada').hide();
          $('#defaultBoardOhio').hide();
          $('#defaultBoardOklahoma').hide();
          $('#defaultBoardOregon').hide();
          $('#defaultBoardPennsylvania').hide();
          $('#defaultBoardPuertoRico').hide();
          $('#defaultBoardRhodeIsland').hide();
          $('#defaultBoardSouthCarolina').hide();
          $('#defaultBoardSouthDakota').hide();
          $('#defaultBoardTennessee').hide();
          $('#defaultBoardTexas').hide();
          $('#defaultBoardUtah').hide();
          $('#defaultBoardVermont').hide();
          $('#defaultBoardVirginia').hide();
          $('#defaultBoardWashington').hide();
          $('#defaultBoardWestVirginia').hide();
          $('#defaultBoardWisconsin').hide();
          $('#defaultBoardWyoming').hide();
          $('#defaultBoardDistrictOfColumbia').hide();

        } else if ($(this).val() == 'EUR') {
          $('#usdAlabama').hide();
          $('#usdAlaska').hide();
          $('#usdArizona').hide();
          $('#usdArkansas').hide();
          $('#usdCalifornia').hide();
          $('#usdColorado').hide();
          $('#usdConnecticut').hide();
          $('#usdDelaware').hide();
          $('#usdFlorida').hide();
          $('#usdGeorgia').hide();
          $('#usdHawaii').hide();
          $('#usdIdaho').hide();
          $('#usdIllinois').hide();
          $('#usdIndiana').hide();
          $('#usdIowa').hide();
          $('#usdKansas').hide();
          $('#usdKentucky').hide();
          $('#usdLouisiana').hide();
          $('#usdMaine').hide();
          $('#usdMaryland').hide();
          $('#usdMassachusetts').hide();
          $('#usdMichigan').hide();
          $('#usdMinnesota').hide();
          $('#usdMississippi').hide();
          $('#usdMissouri').hide();
          $('#usdMontana').hide();
          $('#usdNebraska').hide();
          $('#usdNewHampshire').hide();
          $('#usdNewJersey').hide();
          $('#usdNewMexico').hide();
          $('#usdNewYork').hide();
          $('#usdNorthCarolina').hide();
          $('#usdNorthDakota').hide();
          $('#usdNevada').hide();
          $('#usdOhio').hide();
          $('#usdOklahoma').hide();
          $('#usdOregon').hide();
          $('#usdPennsylvania').hide();
          $('#usdPuertoRico').hide();
          $('#usdRhodeIsland').hide();
          $('#usdSouthCarolina').hide();
          $('#usdSouthDakota').hide();
          $('#usdTennessee').hide();
          $('#usdTexas').hide();
          $('#usdUtah').hide();
          $('#usdVermont').hide();
          $('#usdVirginia').hide();
          $('#usdWashington').hide();
          $('#usdWestVirginia').hide();
          $('#usdWisconsin').hide();
          $('#usdWyoming').hide();
          $('#usdDistrictOfColumbia').hide();

          $('#eurAlabama').show();
          $('#eurAlaska').show();
          $('#eurArizona').show();
          $('#eurArkansas').show();
          $('#eurCalifornia').show();
          $('#eurColorado').show();
          $('#eurConnecticut').show();
          $('#eurDelaware').show();
          $('#eurFlorida').show();
          $('#eurGeorgia').show();
          $('#eurHawaii').show();
          $('#eurIdaho').show();
          $('#eurIllinois').show();
          $('#eurIndiana').show();
          $('#eurIowa').show();
          $('#eurKansas').show();
          $('#eurKentucky').show();
          $('#eurLouisiana').show();
          $('#eurMaine').show();
          $('#eurMaryland').show();
          $('#eurMassachusetts').show();
          $('#eurMichigan').show();
          $('#eurMinnesota').show();
          $('#eurMississippi').show();
          $('#eurMissouri').show();
          $('#eurMontana').show();
          $('#eurNebraska').show();
          $('#eurNewHampshire').show();
          $('#eurNewJersey').show();
          $('#eurNewMexico').show();
          $('#eurNewYork').show();
          $('#eurNorthCarolina').show();
          $('#eurNorthDakota').show();
          $('#eurNevada').show();
          $('#eurOhio').show();
          $('#eurOklahoma').show();
          $('#eurOregon').show();
          $('#eurPennsylvania').show();
          $('#eurPuertoRico').show();
          $('#eurRhodeIsland').show();
          $('#eurSouthCarolina').show();
          $('#eurSouthDakota').show();
          $('#eurTennessee').show();
          $('#eurTexas').show();
          $('#eurUtah').show();
          $('#eurVermont').show();
          $('#eurVirginia').show();
          $('#eurWashington').show();
          $('#eurWestVirginia').show();
          $('#eurWisconsin').show();
          $('#eurWyoming').show();
          $('#eurDistrictOfColumbia').show();

          $('#gbpAlabama').hide();
          $('#gbpAlaska').hide();
          $('#gbpArizona').hide();
          $('#gbpArkansas').hide();
          $('#gbpCalifornia').hide();
          $('#gbpColorado').hide();
          $('#gbpConnecticut').hide();
          $('#gbpDelaware').hide();
          $('#gbpFlorida').hide();
          $('#gbpGeorgia').hide();
          $('#gbpHawaii').hide();
          $('#gbpIdaho').hide();
          $('#gbpIllinois').hide();
          $('#gbpIndiana').hide();
          $('#gbpIowa').hide();
          $('#gbpKansas').hide();
          $('#gbpKentucky').hide();
          $('#gbpLouisiana').hide();
          $('#gbpMaine').hide();
          $('#gbpMaryland').hide();
          $('#gbpMassachusetts').hide();
          $('#gbpMichigan').hide();
          $('#gbpMinnesota').hide();
          $('#gbpMississippi').hide();
          $('#gbpMissouri').hide();
          $('#gbpMontana').hide();
          $('#gbpNebraska').hide();
          $('#gbpNewHampshire').hide();
          $('#gbpNewJersey').hide();
          $('#gbpNewMexico').hide();
          $('#gbpNewYork').hide();
          $('#gbpNorthCarolina').hide();
          $('#gbpNorthDakota').hide();
          $('#gbpNevada').hide();
          $('#gbpOhio').hide();
          $('#gbpOklahoma').hide();
          $('#gbpOregon').hide();
          $('#gbpPennsylvania').hide();
          $('#gbpPuertoRico').hide();
          $('#gbpRhodeIsland').hide();
          $('#gbpSouthCarolina').hide();
          $('#gbpSouthDakota').hide();
          $('#gbpTennessee').hide();
          $('#gbpTexas').hide();
          $('#gbpUtah').hide();
          $('#gbpVermont').hide();
          $('#gbpVirginia').hide();
          $('#gbpWashington').hide();
          $('#gbpWestVirginia').hide();
          $('#gbpWisconsin').hide();
          $('#gbpWyoming').hide();
          $('#gbpDistrictOfColumbia').hide();

          $('#defaultBoardAlabama').hide();
          $('#defaultBoardAlaska').hide();
          $('#defaultBoardArizona').hide();
          $('#defaultBoardArkansas').hide();
          $('#defaultBoardCalifornia').hide();
          $('#defaultBoardColorado').hide();
          $('#defaultBoardConnecticut').hide();
          $('#defaultBoardDelaware').hide();
          $('#defaultBoardFlorida').hide();
          $('#defaultBoardGeorgia').hide();
          $('#defaultBoardHawaii').hide();
          $('#defaultBoardIdaho').hide();
          $('#defaultBoardIllinois').hide();
          $('#defaultBoardIndiana').hide();
          $('#defaultBoardIowa').hide();
          $('#defaultBoardKansas').hide();
          $('#defaultBoardKentucky').hide();
          $('#defaultBoardLouisiana').hide();
          $('#defaultBoardMaine').hide();
          $('#defaultBoardMaryland').hide();
          $('#defaultBoardMassachusetts').hide();
          $('#defaultBoardMichigan').hide();
          $('#defaultBoardMinnesota').hide();
          $('#defaultBoardMississippi').hide();
          $('#defaultBoardMissouri').hide();
          $('#defaultBoardMontana').hide();
          $('#defaultBoardNebraska').hide();
          $('#defaultBoardNewHampshire').hide();
          $('#defaultBoardNewJersey').hide();
          $('#defaultBoardNewMexico').hide();
          $('#defaultBoardNewYork').hide();
          $('#defaultBoardNorthCarolina').hide();
          $('#defaultBoardNorthDakota').hide();
          $('#defaultBoardNevada').hide();
          $('#defaultBoardOhio').hide();
          $('#defaultBoardOklahoma').hide();
          $('#defaultBoardOregon').hide();
          $('#defaultBoardPennsylvania').hide();
          $('#defaultBoardPuertoRico').hide();
          $('#defaultBoardRhodeIsland').hide();
          $('#defaultBoardSouthCarolina').hide();
          $('#defaultBoardSouthDakota').hide();
          $('#defaultBoardTennessee').hide();
          $('#defaultBoardTexas').hide();
          $('#defaultBoardUtah').hide();
          $('#defaultBoardVermont').hide();
          $('#defaultBoardVirginia').hide();
          $('#defaultBoardWashington').hide();
          $('#defaultBoardWestVirginia').hide();
          $('#defaultBoardWisconsin').hide();
          $('#defaultBoardWyoming').hide();
          $('#defaultBoardDistrictOfColumbia').hide();

        } else if ($(this).val() == 'GBP') {
          $('#usdAlabama').hide();
          $('#usdAlaska').hide();
          $('#usdArizona').hide();
          $('#usdArkansas').hide();
          $('#usdCalifornia').hide();
          $('#usdColorado').hide();
          $('#usdConnecticut').hide();
          $('#usdDelaware').hide();
          $('#usdFlorida').hide();
          $('#usdGeorgia').hide();
          $('#usdHawaii').hide();
          $('#usdIdaho').hide();
          $('#usdIllinois').hide();
          $('#usdIndiana').hide();
          $('#usdIowa').hide();
          $('#usdKansas').hide();
          $('#usdKentucky').hide();
          $('#usdLouisiana').hide();
          $('#usdMaine').hide();
          $('#usdMaryland').hide();
          $('#usdMassachusetts').hide();
          $('#usdMichigan').hide();
          $('#usdMinnesota').hide();
          $('#usdMississippi').hide();
          $('#usdMissouri').hide();
          $('#usdMontana').hide();
          $('#usdNebraska').hide();
          $('#usdNewHampshire').hide();
          $('#usdNewJersey').hide();
          $('#usdNewMexico').hide();
          $('#usdNewYork').hide();
          $('#usdNorthCarolina').hide();
          $('#usdNorthDakota').hide();
          $('#usdNevada').hide();
          $('#usdOhio').hide();
          $('#usdOklahoma').hide();
          $('#usdOregon').hide();
          $('#usdPennsylvania').hide();
          $('#usdPuertoRico').hide();
          $('#usdRhodeIsland').hide();
          $('#usdSouthCarolina').hide();
          $('#usdSouthDakota').hide();
          $('#usdTennessee').hide();
          $('#usdTexas').hide();
          $('#usdUtah').hide();
          $('#usdVermont').hide();
          $('#usdVirginia').hide();
          $('#usdWashington').hide();
          $('#usdWestVirginia').hide();
          $('#usdWisconsin').hide();
          $('#usdWyoming').hide();
          $('#usdDistrictOfColumbia').hide();

          $('#eurAlabama').hide();
          $('#eurAlaska').hide();
          $('#eurArizona').hide();
          $('#eurArkansas').hide();
          $('#eurCalifornia').hide();
          $('#eurColorado').hide();
          $('#eurConnecticut').hide();
          $('#eurDelaware').hide();
          $('#eurFlorida').hide();
          $('#eurGeorgia').hide();
          $('#eurHawaii').hide();
          $('#eurIdaho').hide();
          $('#eurIllinois').hide();
          $('#eurIndiana').hide();
          $('#eurIowa').hide();
          $('#eurKansas').hide();
          $('#eurKentucky').hide();
          $('#eurLouisiana').hide();
          $('#eurMaine').hide();
          $('#eurMaryland').hide();
          $('#eurMassachusetts').hide();
          $('#eurMichigan').hide();
          $('#eurMinnesota').hide();
          $('#eurMississippi').hide();
          $('#eurMissouri').hide();
          $('#eurMontana').hide();
          $('#eurNebraska').hide();
          $('#eurNewHampshire').hide();
          $('#eurNewJersey').hide();
          $('#eurNewMexico').hide();
          $('#eurNewYork').hide();
          $('#eurNorthCarolina').hide();
          $('#eurNorthDakota').hide();
          $('#eurNevada').hide();
          $('#eurOhio').hide();
          $('#eurOklahoma').hide();
          $('#eurOregon').hide();
          $('#eurPennsylvania').hide();
          $('#eurPuertoRico').hide();
          $('#eurRhodeIsland').hide();
          $('#eurSouthCarolina').hide();
          $('#eurSouthDakota').hide();
          $('#eurTennessee').hide();
          $('#eurTexas').hide();
          $('#eurUtah').hide();
          $('#eurVermont').hide();
          $('#eurVirginia').hide();
          $('#eurWashington').hide();
          $('#eurWestVirginia').hide();
          $('#eurWisconsin').hide();
          $('#eurWyoming').hide();
          $('#eurDistrictOfColumbia').hide();

          $('#gbpAlabama').show();
          $('#gbpAlaska').show();
          $('#gbpArizona').show();
          $('#gbpArkansas').show();
          $('#gbpCalifornia').show();
          $('#gbpColorado').show();
          $('#gbpConnecticut').show();
          $('#gbpDelaware').show();
          $('#gbpFlorida').show();
          $('#gbpGeorgia').show();
          $('#gbpHawaii').show();
          $('#gbpIdaho').show();
          $('#gbpIllinois').show();
          $('#gbpIndiana').show();
          $('#gbpIowa').show();
          $('#gbpKansas').show();
          $('#gbpKentucky').show();
          $('#gbpLouisiana').show();
          $('#gbpMaine').show();
          $('#gbpMaryland').show();
          $('#gbpMassachusetts').show();
          $('#gbpMichigan').show();
          $('#gbpMinnesota').show();
          $('#gbpMississippi').show();
          $('#gbpMissouri').show();
          $('#gbpMontana').show();
          $('#gbpNebraska').show();
          $('#gbpNewHampshire').show();
          $('#gbpNewJersey').show();
          $('#gbpNewMexico').show();
          $('#gbpNewYork').show();
          $('#gbpNorthCarolina').show();
          $('#gbpNorthDakota').show();
          $('#gbpNevada').show();
          $('#gbpOhio').show();
          $('#gbpOklahoma').show();
          $('#gbpOregon').show();
          $('#gbpPennsylvania').show();
          $('#gbpPuertoRico').show();
          $('#gbpRhodeIsland').show();
          $('#gbpSouthCarolina').show();
          $('#gbpSouthDakota').show();
          $('#gbpTennessee').show();
          $('#gbpTexas').show();
          $('#gbpUtah').show();
          $('#gbpVermont').show();
          $('#gbpVirginia').show();
          $('#gbpWashington').show();
          $('#gbpWestVirginia').show();
          $('#gbpWisconsin').show();
          $('#gbpWyoming').show();
          $('#gbpDistrictOfColumbia').show();

          $('#defaultBoardAlabama').hide();
          $('#defaultBoardAlaska').hide();
          $('#defaultBoardArizona').hide();
          $('#defaultBoardArkansas').hide();
          $('#defaultBoardCalifornia').hide();
          $('#defaultBoardColorado').hide();
          $('#defaultBoardConnecticut').hide();
          $('#defaultBoardDelaware').hide();
          $('#defaultBoardFlorida').hide();
          $('#defaultBoardGeorgia').hide();
          $('#defaultBoardHawaii').hide();
          $('#defaultBoardIdaho').hide();
          $('#defaultBoardIllinois').hide();
          $('#defaultBoardIndiana').hide();
          $('#defaultBoardIowa').hide();
          $('#defaultBoardKansas').hide();
          $('#defaultBoardKentucky').hide();
          $('#defaultBoardLouisiana').hide();
          $('#defaultBoardMaine').hide();
          $('#defaultBoardMaryland').hide();
          $('#defaultBoardMassachusetts').hide();
          $('#defaultBoardMichigan').hide();
          $('#defaultBoardMinnesota').hide();
          $('#defaultBoardMississippi').hide();
          $('#defaultBoardMissouri').hide();
          $('#defaultBoardMontana').hide();
          $('#defaultBoardNebraska').hide();
          $('#defaultBoardNewHampshire').hide();
          $('#defaultBoardNewJersey').hide();
          $('#defaultBoardNewMexico').hide();
          $('#defaultBoardNewYork').hide();
          $('#defaultBoardNorthCarolina').hide();
          $('#defaultBoardNorthDakota').hide();
          $('#defaultBoardNevada').hide();
          $('#defaultBoardOhio').hide();
          $('#defaultBoardOklahoma').hide();
          $('#defaultBoardOregon').hide();
          $('#defaultBoardPennsylvania').hide();
          $('#defaultBoardPuertoRico').hide();
          $('#defaultBoardRhodeIsland').hide();
          $('#defaultBoardSouthCarolina').hide();
          $('#defaultBoardSouthDakota').hide();
          $('#defaultBoardTennessee').hide();
          $('#defaultBoardTexas').hide();
          $('#defaultBoardUtah').hide();
          $('#defaultBoardVermont').hide();
          $('#defaultBoardVirginia').hide();
          $('#defaultBoardWashington').hide();
          $('#defaultBoardWestVirginia').hide();
          $('#defaultBoardWisconsin').hide();
          $('#defaultBoardWyoming').hide();
          $('#defaultBoardDistrictOfColumbia').hide();

        } else {
          $('#usdAlabama').hide();
          $('#usdAlaska').hide();
          $('#usdArizona').hide();
          $('#usdArkansas').hide();
          $('#usdCalifornia').hide();
          $('#usdColorado').hide();
          $('#usdConnecticut').hide();
          $('#usdDelaware').hide();
          $('#usdFlorida').hide();
          $('#usdGeorgia').hide();
          $('#usdHawaii').hide();
          $('#usdIdaho').hide();
          $('#usdIllinois').hide();
          $('#usdIndiana').hide();
          $('#usdIowa').hide();
          $('#usdKansas').hide();
          $('#usdKentucky').hide();
          $('#usdLouisiana').hide();
          $('#usdMaine').hide();
          $('#usdMaryland').hide();
          $('#usdMassachusetts').hide();
          $('#usdMichigan').hide();
          $('#usdMinnesota').hide();
          $('#usdMississippi').hide();
          $('#usdMissouri').hide();
          $('#usdMontana').hide();
          $('#usdNebraska').hide();
          $('#usdNewHampshire').hide();
          $('#usdNewJersey').hide();
          $('#usdNewMexico').hide();
          $('#usdNewYork').hide();
          $('#usdNorthCarolina').hide();
          $('#usdNorthDakota').hide();
          $('#usdNevada').hide();
          $('#usdOhio').hide();
          $('#usdOklahoma').hide();
          $('#usdOregon').hide();
          $('#usdPennsylvania').hide();
          $('#usdPuertoRico').hide();
          $('#usdRhodeIsland').hide();
          $('#usdSouthCarolina').hide();
          $('#usdSouthDakota').hide();
          $('#usdTennessee').hide();
          $('#usdTexas').hide();
          $('#usdUtah').hide();
          $('#usdVermont').hide();
          $('#usdVirginia').hide();
          $('#usdWashington').hide();
          $('#usdWestVirginia').hide();
          $('#usdWisconsin').hide();
          $('#usdWyoming').hide();
          $('#usdDistrictOfColumbia').hide();

          $('#eurAlabama').hide();
          $('#eurAlaska').hide();
          $('#eurArizona').hide();
          $('#eurArkansas').hide();
          $('#eurCalifornia').hide();
          $('#eurColorado').hide();
          $('#eurConnecticut').hide();
          $('#eurDelaware').hide();
          $('#eurFlorida').hide();
          $('#eurGeorgia').hide();
          $('#eurHawaii').hide();
          $('#eurIdaho').hide();
          $('#eurIllinois').hide();
          $('#eurIndiana').hide();
          $('#eurIowa').hide();
          $('#eurKansas').hide();
          $('#eurKentucky').hide();
          $('#eurLouisiana').hide();
          $('#eurMaine').hide();
          $('#eurMaryland').hide();
          $('#eurMassachusetts').hide();
          $('#eurMichigan').hide();
          $('#eurMinnesota').hide();
          $('#eurMississippi').hide();
          $('#eurMissouri').hide();
          $('#eurMontana').hide();
          $('#eurNebraska').hide();
          $('#eurNewHampshire').hide();
          $('#eurNewJersey').hide();
          $('#eurNewMexico').hide();
          $('#eurNewYork').hide();
          $('#eurNorthCarolina').hide();
          $('#eurNorthDakota').hide();
          $('#eurNevada').hide();
          $('#eurOhio').hide();
          $('#eurOklahoma').hide();
          $('#eurOregon').hide();
          $('#eurPennsylvania').hide();
          $('#eurPuertoRico').hide();
          $('#eurRhodeIsland').hide();
          $('#eurSouthCarolina').hide();
          $('#eurSouthDakota').hide();
          $('#eurTennessee').hide();
          $('#eurTexas').hide();
          $('#eurUtah').hide();
          $('#eurVermont').hide();
          $('#eurVirginia').hide();
          $('#eurWashington').hide();
          $('#eurWestVirginia').hide();
          $('#eurWisconsin').hide();
          $('#eurWyoming').hide();
          $('#eurDistrictOfColumbia').hide();

          $('#gbpAlabama').hide();
          $('#gbpAlaska').hide();
          $('#gbpArizona').hide();
          $('#gbpArkansas').hide();
          $('#gbpCalifornia').hide();
          $('#gbpColorado').hide();
          $('#gbpConnecticut').hide();
          $('#gbpDelaware').hide();
          $('#gbpFlorida').hide();
          $('#gbpGeorgia').hide();
          $('#gbpHawaii').hide();
          $('#gbpIdaho').hide();
          $('#gbpIllinois').hide();
          $('#gbpIndiana').hide();
          $('#gbpIowa').hide();
          $('#gbpKansas').hide();
          $('#gbpKentucky').hide();
          $('#gbpLouisiana').hide();
          $('#gbpMaine').hide();
          $('#gbpMaryland').hide();
          $('#gbpMassachusetts').hide();
          $('#gbpMichigan').hide();
          $('#gbpMinnesota').hide();
          $('#gbpMississippi').hide();
          $('#gbpMissouri').hide();
          $('#gbpMontana').hide();
          $('#gbpNebraska').hide();
          $('#gbpNewHampshire').hide();
          $('#gbpNewJersey').hide();
          $('#gbpNewMexico').hide();
          $('#gbpNewYork').hide();
          $('#gbpNorthCarolina').hide();
          $('#gbpNorthDakota').hide();
          $('#gbpNevada').hide();
          $('#gbpOhio').hide();
          $('#gbpOklahoma').hide();
          $('#gbpOregon').hide();
          $('#gbpPennsylvania').hide();
          $('#gbpPuertoRico').hide();
          $('#gbpRhodeIsland').hide();
          $('#gbpSouthCarolina').hide();
          $('#gbpSouthDakota').hide();
          $('#gbpTennessee').hide();
          $('#gbpTexas').hide();
          $('#gbpUtah').hide();
          $('#gbpVermont').hide();
          $('#gbpVirginia').hide();
          $('#gbpWashington').hide();
          $('#gbpWestVirginia').hide();
          $('#gbpWisconsin').hide();
          $('#gbpWyoming').hide();
          $('#gbpDistrictOfColumbia').hide();

          $('#defaultBoardAlabama').show();
          $('#defaultBoardAlaska').show();
          $('#defaultBoardArizona').show();
          $('#defaultBoardArkansas').show();
          $('#defaultBoardCalifornia').show();
          $('#defaultBoardColorado').show();
          $('#defaultBoardConnecticut').show();
          $('#defaultBoardDelaware').show();
          $('#defaultBoardFlorida').show();
          $('#defaultBoardGeorgia').show();
          $('#defaultBoardHawaii').show();
          $('#defaultBoardIdaho').show();
          $('#defaultBoardIllinois').show();
          $('#defaultBoardIndiana').show();
          $('#defaultBoardIowa').show();
          $('#defaultBoardKansas').show();
          $('#defaultBoardKentucky').show();
          $('#defaultBoardLouisiana').show();
          $('#defaultBoardMaine').show();
          $('#defaultBoardMaryland').show();
          $('#defaultBoardMassachusetts').show();
          $('#defaultBoardMichigan').show();
          $('#defaultBoardMinnesota').show();
          $('#defaultBoardMississippi').show();
          $('#defaultBoardMissouri').show();
          $('#defaultBoardMontana').show();
          $('#defaultBoardNebraska').show();
          $('#defaultBoardNewHampshire').show();
          $('#defaultBoardNewJersey').show();
          $('#defaultBoardNewMexico').show();
          $('#defaultBoardNewYork').show();
          $('#defaultBoardNorthCarolina').show();
          $('#defaultBoardNorthDakota').show();
          $('#defaultBoardNevada').show();
          $('#defaultBoardOhio').show();
          $('#defaultBoardOklahoma').show();
          $('#defaultBoardOregon').show();
          $('#defaultBoardPennsylvania').show();
          $('#defaultBoardPuertoRico').show();
          $('#defaultBoardRhodeIsland').show();
          $('#defaultBoardSouthCarolina').show();
          $('#defaultBoardSouthDakota').show();
          $('#defaultBoardTennessee').show();
          $('#defaultBoardTexas').show();
          $('#defaultBoardUtah').show();
          $('#defaultBoardVermont').show();
          $('#defaultBoardVirginia').show();
          $('#defaultBoardWashington').show();
          $('#defaultBoardWestVirginia').show();
          $('#defaultBoardWisconsin').show();
          $('#defaultBoardWyoming').show();
          $('#defaultBoardDistrictOfColumbia').show();
        }
    });
});


<!-- DISPLAY SELECTED CURRENCY ON UK | MAIN/LOCATIONS --->
$(document).ready(function (e) {
    $('#ChooseCurrencyUK').change(function () {
        if ($(this).val() == 'USD') {
          $('#usdAberdeen').show();
          $('#usdBath').show();
          $('#usdBelfast').show();
          $('#usdBirmingham').show();
          $('#usdBournemouth').show();
          $('#usdBrightonHove').show();
          $('#usdBristol').show();
          $('#usdCambridge').show();
          $('#usdCardiff').show();
          $('#usdColchester').show();
          $('#usdDerby').show();
          $('#usdExeter').show();
          $('#usdGlasgow').show();
          $('#usdHull').show();
          $('#usdChelmsford').show();
          $('#usdLeeds').show();
          $('#usdLeicester').show();
          $('#usdLiverpool').show();
          $('#usdLondon').show();
          $('#usdManchester').show();
          $('#usdMiddlesbrough').show();
          $('#usdNewcastle').show();
          $('#usdNorwich').show();
          $('#usdNottingham').show();
          $('#usdOxford').show();
          $('#usdPeterborough').show();
          $('#usdPlymouth').show();
          $('#usdPortsmouth').show();
          $('#usdSalisbury').show();
          $('#usdSheffield').show();
          $('#usdSouthampton').show();
          $('#usdSwansea').show();

          $('#eurAberdeen').hide();
          $('#eurBath').hide();
          $('#eurBelfast').hide();
          $('#eurBirmingham').hide();
          $('#eurBournemouth').hide();
          $('#eurBrightonHove').hide();
          $('#eurBristol').hide();
          $('#eurCambridge').hide();
          $('#eurCardiff').hide();
          $('#eurColchester').hide();
          $('#eurDerby').hide();
          $('#eurExeter').hide();
          $('#eurGlasgow').hide();
          $('#eurHull').hide();
          $('#eurChelmsford').hide();
          $('#eurLeeds').hide();
          $('#eurLeicester').hide();
          $('#eurLiverpool').hide();
          $('#eurLondon').hide();
          $('#eurManchester').hide();
          $('#eurMiddlesbrough').hide();
          $('#eurNewcastle').hide();
          $('#eurNorwich').hide();
          $('#eurNottingham').hide();
          $('#eurOxford').hide();
          $('#eurPeterborough').hide();
          $('#eurPlymouth').hide();
          $('#eurPortsmouth').hide();
          $('#eurSalisbury').hide();
          $('#eurSheffield').hide();
          $('#eurSouthampton').hide();
          $('#eurSwansea').hide();

          $('#gbpAberdeen').hide();
          $('#gbpBath').hide();
          $('#gbpBelfast').hide();
          $('#gbpBirmingham').hide();
          $('#gbpBournemouth').hide();
          $('#gbpBrightonHove').hide();
          $('#gbpBristol').hide();
          $('#gbpCambridge').hide();
          $('#gbpCardiff').hide();
          $('#gbpColchester').hide();
          $('#gbpDerby').hide();
          $('#gbpExeter').hide();
          $('#gbpGlasgow').hide();
          $('#gbpHull').hide();
          $('#gbpChelmsford').hide();
          $('#gbpLeeds').hide();
          $('#gbpLeicester').hide();
          $('#gbpLiverpool').hide();
          $('#gbpLondon').hide();
          $('#gbpManchester').hide();
          $('#gbpMiddlesbrough').hide();
          $('#gbpNewcastle').hide();
          $('#gbpNorwich').hide();
          $('#gbpNottingham').hide();
          $('#gbpOxford').hide();
          $('#gbpPeterborough').hide();
          $('#gbpPlymouth').hide();
          $('#gbpPortsmouth').hide();
          $('#gbpSalisbury').hide();
          $('#gbpSheffield').hide();
          $('#gbpSouthampton').hide();
          $('#gbpSwansea').hide();

          $('#defaultBoardAberdeen').hide();
          $('#defaultBoardBath').hide();
          $('#defaultBoardBelfast').hide();
          $('#defaultBoardBirmingham').hide();
          $('#defaultBoardBournemouth').hide();
          $('#defaultBoardBrightonHove').hide();
          $('#defaultBoardBristol').hide();
          $('#defaultBoardCambridge').hide();
          $('#defaultBoardCardiff').hide();
          $('#defaultBoardColchester').hide();
          $('#defaultBoardDerby').hide();
          $('#defaultBoardExeter').hide();
          $('#defaultBoardGlasgow').hide();
          $('#defaultBoardHull').hide();
          $('#defaultBoardChelmsford').hide();
          $('#defaultBoardLeeds').hide();
          $('#defaultBoardLeicester').hide();
          $('#defaultBoardLiverpool').hide();
          $('#defaultBoardLondon').hide();
          $('#defaultBoardManchester').hide();
          $('#defaultBoardMiddlesbrough').hide();
          $('#defaultBoardNewcastle').hide();
          $('#defaultBoardNorwich').hide();
          $('#defaultBoardNottingham').hide();
          $('#defaultBoardOxford').hide();
          $('#defaultBoardPeterborough').hide();
          $('#defaultBoardPlymouth').hide();
          $('#defaultBoardPortsmouth').hide();
          $('#defaultBoardSalisbury').hide();
          $('#defaultBoardSheffield').hide();
          $('#defaultBoardSouthampton').hide();
          $('#defaultBoardSwansea').hide();

        } else if ($(this).val() == 'EUR') {
          $('#usdAberdeen').hide();
          $('#usdBath').hide();
          $('#usdBelfast').hide();
          $('#usdBirmingham').hide();
          $('#usdBournemouth').hide();
          $('#usdBrightonHove').hide();
          $('#usdBristol').hide();
          $('#usdCambridge').hide();
          $('#usdCardiff').hide();
          $('#usdColchester').hide();
          $('#usdDerby').hide();
          $('#usdExeter').hide();
          $('#usdGlasgow').hide();
          $('#usdHull').hide();
          $('#usdChelmsford').hide();
          $('#usdLeeds').hide();
          $('#usdLeicester').hide();
          $('#usdLiverpool').hide();
          $('#usdLondon').hide();
          $('#usdManchester').hide();
          $('#usdMiddlesbrough').hide();
          $('#usdNewcastle').hide();
          $('#usdNorwich').hide();
          $('#usdNottingham').hide();
          $('#usdOxford').hide();
          $('#usdPeterborough').hide();
          $('#usdPlymouth').hide();
          $('#usdPortsmouth').hide();
          $('#usdSalisbury').hide();
          $('#usdSheffield').hide();
          $('#usdSouthampton').hide();
          $('#usdSwansea').hide();


          $('#eurAberdeen').show();
          $('#eurBath').show();
          $('#eurBelfast').show();
          $('#eurBirmingham').show();
          $('#eurBournemouth').show();
          $('#eurBrightonHove').show();
          $('#eurBristol').show();
          $('#eurCambridge').show();
          $('#eurCardiff').show();
          $('#eurColchester').show();
          $('#eurDerby').show();
          $('#eurExeter').show();
          $('#eurGlasgow').show();
          $('#eurHull').show();
          $('#eurChelmsford').show();
          $('#eurLeeds').show();
          $('#eurLeicester').show();
          $('#eurLiverpool').show();
          $('#eurLondon').show();
          $('#eurManchester').show();
          $('#eurMiddlesbrough').show();
          $('#eurNewcastle').show();
          $('#eurNorwich').show();
          $('#eurNottingham').show();
          $('#eurOxford').show();
          $('#eurPeterborough').show();
          $('#eurPlymouth').show();
          $('#eurPortsmouth').show();
          $('#eurSalisbury').show();
          $('#eurSheffield').show();
          $('#eurSouthampton').show();
          $('#eurSwansea').show();

          $('#gbpAberdeen').hide();
          $('#gbpBath').hide();
          $('#gbpBelfast').hide();
          $('#gbpBirmingham').hide();
          $('#gbpBournemouth').hide();
          $('#gbpBrightonHove').hide();
          $('#gbpBristol').hide();
          $('#gbpCambridge').hide();
          $('#gbpCardiff').hide();
          $('#gbpColchester').hide();
          $('#gbpDerby').hide();
          $('#gbpExeter').hide();
          $('#gbpGlasgow').hide();
          $('#gbpHull').hide();
          $('#gbpChelmsford').hide();
          $('#gbpLeeds').hide();
          $('#gbpLeicester').hide();
          $('#gbpLiverpool').hide();
          $('#gbpLondon').hide();
          $('#gbpManchester').hide();
          $('#gbpMiddlesbrough').hide();
          $('#gbpNewcastle').hide();
          $('#gbpNorwich').hide();
          $('#gbpNottingham').hide();
          $('#gbpOxford').hide();
          $('#gbpPeterborough').hide();
          $('#gbpPlymouth').hide();
          $('#gbpPortsmouth').hide();
          $('#gbpSalisbury').hide();
          $('#gbpSheffield').hide();
          $('#gbpSouthampton').hide();
          $('#gbpSwansea').hide();

          $('#defaultBoardAberdeen').hide();
          $('#defaultBoardBath').hide();
          $('#defaultBoardBelfast').hide();
          $('#defaultBoardBirmingham').hide();
          $('#defaultBoardBournemouth').hide();
          $('#defaultBoardBrightonHove').hide();
          $('#defaultBoardBristol').hide();
          $('#defaultBoardCambridge').hide();
          $('#defaultBoardCardiff').hide();
          $('#defaultBoardColchester').hide();
          $('#defaultBoardDerby').hide();
          $('#defaultBoardExeter').hide();
          $('#defaultBoardGlasgow').hide();
          $('#defaultBoardHull').hide();
          $('#defaultBoardChelmsford').hide();
          $('#defaultBoardLeeds').hide();
          $('#defaultBoardLeicester').hide();
          $('#defaultBoardLiverpool').hide();
          $('#defaultBoardLondon').hide();
          $('#defaultBoardManchester').hide();
          $('#defaultBoardMiddlesbrough').hide();
          $('#defaultBoardNewcastle').hide();
          $('#defaultBoardNorwich').hide();
          $('#defaultBoardNottingham').hide();
          $('#defaultBoardOxford').hide();
          $('#defaultBoardPeterborough').hide();
          $('#defaultBoardPlymouth').hide();
          $('#defaultBoardPortsmouth').hide();
          $('#defaultBoardSalisbury').hide();
          $('#defaultBoardSheffield').hide();
          $('#defaultBoardSouthampton').hide();
          $('#defaultBoardSwansea').hide();

        } else if ($(this).val() == 'GBP') {
          $('#usdAberdeen').hide();
          $('#usdBath').hide();
          $('#usdBelfast').hide();
          $('#usdBirmingham').hide();
          $('#usdBournemouth').hide();
          $('#usdBrightonHove').hide();
          $('#usdBristol').hide();
          $('#usdCambridge').hide();
          $('#usdCardiff').hide();
          $('#usdColchester').hide();
          $('#usdDerby').hide();
          $('#usdExeter').hide();
          $('#usdGlasgow').hide();
          $('#usdHull').hide();
          $('#usdChelmsford').hide();
          $('#usdLeeds').hide();
          $('#usdLeicester').hide();
          $('#usdLiverpool').hide();
          $('#usdLondon').hide();
          $('#usdManchester').hide();
          $('#usdMiddlesbrough').hide();
          $('#usdNewcastle').hide();
          $('#usdNorwich').hide();
          $('#usdNottingham').hide();
          $('#usdOxford').hide();
          $('#usdPeterborough').hide();
          $('#usdPlymouth').hide();
          $('#usdPortsmouth').hide();
          $('#usdSalisbury').hide();
          $('#usdSheffield').hide();
          $('#usdSouthampton').hide();
          $('#usdSwansea').hide();

          $('#eurAberdeen').hide();
          $('#eurBath').hide();
          $('#eurBelfast').hide();
          $('#eurBirmingham').hide();
          $('#eurBournemouth').hide();
          $('#eurBrightonHove').hide();
          $('#eurBristol').hide();
          $('#eurCambridge').hide();
          $('#eurCardiff').hide();
          $('#eurColchester').hide();
          $('#eurDerby').hide();
          $('#eurExeter').hide();
          $('#eurGlasgow').hide();
          $('#eurHull').hide();
          $('#eurChelmsford').hide();
          $('#eurLeeds').hide();
          $('#eurLeicester').hide();
          $('#eurLiverpool').hide();
          $('#eurLondon').hide();
          $('#eurManchester').hide();
          $('#eurMiddlesbrough').hide();
          $('#eurNewcastle').hide();
          $('#eurNorwich').hide();
          $('#eurNottingham').hide();
          $('#eurOxford').hide();
          $('#eurPeterborough').hide();
          $('#eurPlymouth').hide();
          $('#eurPortsmouth').hide();
          $('#eurSalisbury').hide();
          $('#eurSheffield').hide();
          $('#eurSouthampton').hide();
          $('#eurSwansea').hide();

          $('#gbpAberdeen').show();
          $('#gbpBath').show();
          $('#gbpBelfast').show();
          $('#gbpBirmingham').show();
          $('#gbpBournemouth').show();
          $('#gbpBrightonHove').show();
          $('#gbpBristol').show();
          $('#gbpCambridge').show();
          $('#gbpCardiff').show();
          $('#gbpColchester').show();
          $('#gbpDerby').show();
          $('#gbpExeter').show();
          $('#gbpGlasgow').show();
          $('#gbpHull').show();
          $('#gbpChelmsford').show();
          $('#gbpLeeds').show();
          $('#gbpLeicester').show();
          $('#gbpLiverpool').show();
          $('#gbpLondon').show();
          $('#gbpManchester').show();
          $('#gbpMiddlesbrough').show();
          $('#gbpNewcastle').show();
          $('#gbpNorwich').show();
          $('#gbpNottingham').show();
          $('#gbpOxford').show();
          $('#gbpPeterborough').show();
          $('#gbpPlymouth').show();
          $('#gbpPortsmouth').show();
          $('#gbpSalisbury').show();
          $('#gbpSheffield').show();
          $('#gbpSouthampton').show();
          $('#gbpSwansea').show();

          $('#defaultBoardAberdeen').hide();
          $('#defaultBoardBath').hide();
          $('#defaultBoardBelfast').hide();
          $('#defaultBoardBirmingham').hide();
          $('#defaultBoardBournemouth').hide();
          $('#defaultBoardBrightonHove').hide();
          $('#defaultBoardBristol').hide();
          $('#defaultBoardCambridge').hide();
          $('#defaultBoardCardiff').hide();
          $('#defaultBoardColchester').hide();
          $('#defaultBoardDerby').hide();
          $('#defaultBoardExeter').hide();
          $('#defaultBoardGlasgow').hide();
          $('#defaultBoardHull').hide();
          $('#defaultBoardChelmsford').hide();
          $('#defaultBoardLeeds').hide();
          $('#defaultBoardLeicester').hide();
          $('#defaultBoardLiverpool').hide();
          $('#defaultBoardLondon').hide();
          $('#defaultBoardManchester').hide();
          $('#defaultBoardMiddlesbrough').hide();
          $('#defaultBoardNewcastle').hide();
          $('#defaultBoardNorwich').hide();
          $('#defaultBoardNottingham').hide();
          $('#defaultBoardOxford').hide();
          $('#defaultBoardPeterborough').hide();
          $('#defaultBoardPlymouth').hide();
          $('#defaultBoardPortsmouth').hide();
          $('#defaultBoardSalisbury').hide();
          $('#defaultBoardSheffield').hide();
          $('#defaultBoardSouthampton').hide();
          $('#defaultBoardSwansea').hide();

        } else {
          $('#usdAberdeen').hide();
          $('#usdBath').hide();
          $('#usdBelfast').hide();
          $('#usdBirmingham').hide();
          $('#usdBournemouth').hide();
          $('#usdBrightonHove').hide();
          $('#usdBristol').hide();
          $('#usdCambridge').hide();
          $('#usdCardiff').hide();
          $('#usdColchester').hide();
          $('#usdDerby').hide();
          $('#usdExeter').hide();
          $('#usdGlasgow').hide();
          $('#usdHull').hide();
          $('#usdChelmsford').hide();
          $('#usdLeeds').hide();
          $('#usdLeicester').hide();
          $('#usdLiverpool').hide();
          $('#usdLondon').hide();
          $('#usdManchester').hide();
          $('#usdMiddlesbrough').hide();
          $('#usdNewcastle').hide();
          $('#usdNorwich').hide();
          $('#usdNottingham').hide();
          $('#usdOxford').hide();
          $('#usdPeterborough').hide();
          $('#usdPlymouth').hide();
          $('#usdPortsmouth').hide();
          $('#usdSalisbury').hide();
          $('#usdSheffield').hide();
          $('#usdSouthampton').hide();
          $('#usdSwansea').hide();

          $('#eurAberdeen').hide();
          $('#eurBath').hide();
          $('#eurBelfast').hide();
          $('#eurBirmingham').hide();
          $('#eurBournemouth').hide();
          $('#eurBrightonHove').hide();
          $('#eurBristol').hide();
          $('#eurCambridge').hide();
          $('#eurCardiff').hide();
          $('#eurColchester').hide();
          $('#eurDerby').hide();
          $('#eurExeter').hide();
          $('#eurGlasgow').hide();
          $('#eurHull').hide();
          $('#eurChelmsford').hide();
          $('#eurLeeds').hide();
          $('#eurLeicester').hide();
          $('#eurLiverpool').hide();
          $('#eurLondon').hide();
          $('#eurManchester').hide();
          $('#eurMiddlesbrough').hide();
          $('#eurNewcastle').hide();
          $('#eurNorwich').hide();
          $('#eurNottingham').hide();
          $('#eurOxford').hide();
          $('#eurPeterborough').hide();
          $('#eurPlymouth').hide();
          $('#eurPortsmouth').hide();
          $('#eurSalisbury').hide();
          $('#eurSheffield').hide();
          $('#eurSouthampton').hide();
          $('#eurSwansea').hide();

          $('#gbpAberdeen').hide();
          $('#gbpBath').hide();
          $('#gbpBelfast').hide();
          $('#gbpBirmingham').hide();
          $('#gbpBournemouth').hide();
          $('#gbpBrightonHove').hide();
          $('#gbpBristol').hide();
          $('#gbpCambridge').hide();
          $('#gbpCardiff').hide();
          $('#gbpColchester').hide();
          $('#gbpDerby').hide();
          $('#gbpExeter').hide();
          $('#gbpGlasgow').hide();
          $('#gbpHull').hide();
          $('#gbpChelmsford').hide();
          $('#gbpLeeds').hide();
          $('#gbpLeicester').hide();
          $('#gbpLiverpool').hide();
          $('#gbpLondon').hide();
          $('#gbpManchester').hide();
          $('#gbpMiddlesbrough').hide();
          $('#gbpNewcastle').hide();
          $('#gbpNorwich').hide();
          $('#gbpNottingham').hide();
          $('#gbpOxford').hide();
          $('#gbpPeterborough').hide();
          $('#gbpPlymouth').hide();
          $('#gbpPortsmouth').hide();
          $('#gbpSalisbury').hide();
          $('#gbpSheffield').hide();
          $('#gbpSouthampton').hide();
          $('#gbpSwansea').hide();

          $('#defaultBoardAberdeen').show();
          $('#defaultBoardBath').show();
          $('#defaultBoardBelfast').show();
          $('#defaultBoardBirmingham').show();
          $('#defaultBoardBournemouth').show();
          $('#defaultBoardBrightonHove').show();
          $('#defaultBoardBristol').show();
          $('#defaultBoardCambridge').show();
          $('#defaultBoardCardiff').show();
          $('#defaultBoardColchester').show();
          $('#defaultBoardDerby').show();
          $('#defaultBoardExeter').show();
          $('#defaultBoardGlasgow').show();
          $('#defaultBoardHull').show();
          $('#defaultBoardChelmsford').show();
          $('#defaultBoardLeeds').show();
          $('#defaultBoardLeicester').show();
          $('#defaultBoardLiverpool').show();
          $('#defaultBoardLondon').show();
          $('#defaultBoardManchester').show();
          $('#defaultBoardMiddlesbrough').show();
          $('#defaultBoardNewcastle').show();
          $('#defaultBoardNorwich').show();
          $('#defaultBoardNottingham').show();
          $('#defaultBoardOxford').show();
          $('#defaultBoardPeterborough').show();
          $('#defaultBoardPlymouth').show();
          $('#defaultBoardPortsmouth').show();
          $('#defaultBoardSalisbury').show();
          $('#defaultBoardSheffield').show();
          $('#defaultBoardSouthampton').show();
          $('#defaultBoardSwansea').show();
        }
    });
});

<!-- DISPLAY SELECTED CURRENCY ON CZ | MAIN/LOCATIONS --->
$(document).ready(function (e) {
    $('#ChooseCurrencyCZ').change(function () {
        if ($(this).val() == 'USD') {
          $('#usdPrague').show();
          $('#usdBrno').show();

          $('#eurPrague').hide();
          $('#eurBrno').hide();

          $('#gbpPrague').hide();
          $('#gbpBrno').hide();

          $('#defaultBoardPrague').hide();
          $('#defaultBoardBrno').hide();

        } else if ($(this).val() == 'EUR') {
          $('#usdPrague').hide();
          $('#usdBrno').hide();

          $('#eurPrague').show();
          $('#eurBrno').show();

          $('#gbpPrague').hide();
          $('#gbpBrno').hide();

          $('#defaultBoardPrague').hide();
          $('#defaultBoardBrno').hide();

        } else if ($(this).val() == 'GBP') {
          $('#usdPrague').hide();
          $('#usdBrno').hide();

          $('#eurPrague').hide();
          $('#eurBrno').hide();

          $('#gbpPrague').show();
          $('#gbpBrno').show();

          $('#defaultBoardPrague').hide();
          $('#defaultBoardBrno').hide();

        } else {
          $('#usdPrague').hide();
          $('#usdBrno').hide();

          $('#eurPrague').hide();
          $('#eurBrno').hide();

          $('#gbpPrague').hide();
          $('#gbpBrno').hide();

          $('#defaultBoardPrague').show();
          $('#defaultBoardBrno').show();
        }
    });
});

<!-- DISPLAY SELECTED CURRENCY ON SP | MAIN/LOCATIONS --->
$(document).ready(function (e) {
    $('#ChooseCurrencySP').change(function () {
        if ($(this).val() == 'USD') {
          $('#usdAlicante').show();
          $('#usdBarcelona').show();
          $('#usdMadrid').show();
          $('#usdMalaga').show();
          $('#usdSeville').show();
          $('#usdValencia').show();

          $('#eurAlicante').hide();
          $('#eurBarcelona').hide();
          $('#eurMadrid').hide();
          $('#eurMalaga').hide();
          $('#eurSeville').hide();
          $('#eurValencia').hide();

          $('#gbpAlicante').hide();
          $('#gbpBarcelona').hide();
          $('#gbpMadrid').hide();
          $('#gbpMalaga').hide();
          $('#gbpSeville').hide();
          $('#gbpValencia').hide();

          $('#defaultBoardAlicante').hide();
          $('#defaultBoardBarcelona').hide();
          $('#defaultBoardMadrid').hide();
          $('#defaultBoardMalaga').hide();
          $('#defaultBoardSeville').hide();
          $('#defaultBoardValencia').hide();

        } else if ($(this).val() == 'EUR') {
          $('#usdAlicante').hide();
          $('#usdBarcelona').hide();
          $('#usdMadrid').hide();
          $('#usdMalaga').hide();
          $('#usdSeville').hide();
          $('#usdValencia').hide();

          $('#eurAlicante').show();
          $('#eurBarcelona').show();
          $('#eurMadrid').show();
          $('#eurMalaga').show();
          $('#eurSeville').show();
          $('#eurValencia').show();

          $('#gbpAlicante').hide();
          $('#gbpBarcelona').hide();
          $('#gbpMadrid').hide();
          $('#gbpMalaga').hide();
          $('#gbpSeville').hide();
          $('#gbpValencia').hide();

          $('#defaultBoardAlicante').hide();
          $('#defaultBoardBarcelona').hide();
          $('#defaultBoardMadrid').hide();
          $('#defaultBoardMalaga').hide();
          $('#defaultBoardSeville').hide();
          $('#defaultBoardValencia').hide();

        } else if ($(this).val() == 'GBP') {
          $('#usdAlicante').hide();
          $('#usdBarcelona').hide();
          $('#usdMadrid').hide();
          $('#usdMalaga').hide();
          $('#usdSeville').hide();
          $('#usdValencia').hide();

          $('#eurAlicante').hide();
          $('#eurBarcelona').hide();
          $('#eurMadrid').hide();
          $('#eurMalaga').hide();
          $('#eurSeville').hide();
          $('#eurValencia').hide();

          $('#gbpAlicante').show();
          $('#gbpBarcelona').show();
          $('#gbpMadrid').show();
          $('#gbpMalaga').show();
          $('#gbpSeville').show();
          $('#gbpValencia').show();

          $('#defaultBoardAlicante').hide();
          $('#defaultBoardBarcelona').hide();
          $('#defaultBoardMadrid').hide();
          $('#defaultBoardMalaga').hide();
          $('#defaultBoardSeville').hide();
          $('#defaultBoardValencia').hide();
        } else {
          $('#usdAlicante').hide();
          $('#usdBarcelona').hide();
          $('#usdMadrid').hide();
          $('#usdMalaga').hide();
          $('#usdSeville').hide();
          $('#usdValencia').hide();

          $('#eurAlicante').hide();
          $('#eurBarcelona').hide();
          $('#eurMadrid').hide();
          $('#eurMalaga').hide();
          $('#eurSeville').hide();
          $('#eurValencia').hide();

          $('#gbpAlicante').hide();
          $('#gbpBarcelona').hide();
          $('#gbpMadrid').hide();
          $('#gbpMalaga').hide();
          $('#gbpSeville').hide();
          $('#gbpValencia').hide();

          $('#defaultBoardAlicante').show();
          $('#defaultBoardBarcelona').show();
          $('#defaultBoardMadrid').show();
          $('#defaultBoardMalaga').show();
          $('#defaultBoardSeville').show();
          $('#defaultBoardValencia').show();
        }
    });
});

<!-- DISPLAY SELECTED CURRENCY ON IN | MAIN/LOCATIONS --->
$(document).ready(function (e) {
    $('#ChooseCurrencySP').change(function () {
        if ($(this).val() == 'USD') {
          $('#usdChennai').show();
          $('#usdHyderabad').show();
          $('#usdMumbai').show();
          $('#usdPatna').show();
          $('#usdRaipur').show();
          $('#usdAmdavad').show();
          $('#usdChandigarh').show();
          $('#usdFaridabad').show();
          $('#usdJamshedpur').show();
          $('#usdBangalore').show();
          $('#usdTrivandrum').show();
          $('#usdKochi').show();
          $('#usdBhopal').show();
          $('#usdIndore').show();
          $('#usdNagpur').show();
          $('#usdBhubaneswar').show();
          $('#usdLudhiana').show();
          $('#usdJaipur').show();
          $('#usdLucknow').show();
          $('#usdKanpur').show();
          $('#usdDehradun').show();
          $('#usdKolkata').show();

          $('#eurChennai').hide();
          $('#eurHyderabad').hide();
          $('#eurMumbai').hide();
          $('#eurPatna').hide();
          $('#eurRaipur').hide();
          $('#eurAmdavad').hide();
          $('#eurChandigarh').hide();
          $('#eurFaridabad').hide();
          $('#eurJamshedpur').hide();
          $('#eurBangalore').hide();
          $('#eurTrivandrum').hide();
          $('#eurKochi').hide();
          $('#eurBhopal').hide();
          $('#eurIndore').hide();
          $('#eurNagpur').hide();
          $('#eurBhubaneswar').hide();
          $('#eurLudhiana').hide();
          $('#eurJaipur').hide();
          $('#eurLucknow').hide();
          $('#eurKanpur').hide();
          $('#eurDehradun').hide();
          $('#eurKolkata').hide();

          $('#gbpChennai').hide();
          $('#gbpHyderabad').hide();
          $('#gbpMumbai').hide();
          $('#gbpPatna').hide();
          $('#gbpRaipur').hide();
          $('#gbpAmdavad').hide();
          $('#gbpChandigarh').hide();
          $('#gbpFaridabad').hide();
          $('#gbpJamshedpur').hide();
          $('#gbpBangalore').hide();
          $('#gbpTrivandrum').hide();
          $('#gbpKochi').hide();
          $('#gbpBhopal').hide();
          $('#gbpIndore').hide();
          $('#gbpNagpur').hide();
          $('#gbpBhubaneswar').hide();
          $('#gbpLudhiana').hide();
          $('#gbpJaipur').hide();
          $('#gbpLucknow').hide();
          $('#gbpKanpur').hide();
          $('#gbpDehradun').hide();
          $('#gbpKolkata').hide();

          $('#defaultChennai').hide();
          $('#defaultHyderabad').hide();
          $('#defaultMumbai').hide();
          $('#defaultPatna').hide();
          $('#defaultRaipur').hide();
          $('#defaultAmdavad').hide();
          $('#defaultChandigarh').hide();
          $('#defaultFaridabad').hide();
          $('#defaultJamshedpur').hide();
          $('#defaultBangalore').hide();
          $('#defaultTrivandrum').hide();
          $('#defaultKochi').hide();
          $('#defaultBhopal').hide();
          $('#defaultIndore').hide();
          $('#defaultNagpur').hide();
          $('#defaultBhubaneswar').hide();
          $('#defaultLudhiana').hide();
          $('#defaultJaipur').hide();
          $('#defaultLucknow').hide();
          $('#defaultKanpur').hide();
          $('#defaultDehradun').hide();
          $('#defaultKolkata').hide();

        } else if ($(this).val() == 'EUR') {
          $('#usdChennai').hide();
          $('#usdHyderabad').hide();
          $('#usdMumbai').hide();
          $('#usdPatna').hide();
          $('#usdRaipur').hide();
          $('#usdAmdavad').hide();
          $('#usdChandigarh').hide();
          $('#usdFaridabad').hide();
          $('#usdJamshedpur').hide();
          $('#usdBangalore').hide();
          $('#usdTrivandrum').hide();
          $('#usdKochi').hide();
          $('#usdBhopal').hide();
          $('#usdIndore').hide();
          $('#usdNagpur').hide();
          $('#usdBhubaneswar').hide();
          $('#usdLudhiana').hide();
          $('#usdJaipur').hide();
          $('#usdLucknow').hide();
          $('#usdKanpur').hide();
          $('#usdDehradun').hide();
          $('#usdKolkata').hide();

          $('#eurChennai').show();
          $('#eurHyderabad').show();
          $('#eurMumbai').show();
          $('#eurPatna').show();
          $('#eurRaipur').show();
          $('#eurAmdavad').show();
          $('#eurChandigarh').show();
          $('#eurFaridabad').show();
          $('#eurJamshedpur').show();
          $('#eurBangalore').show();
          $('#eurTrivandrum').show();
          $('#eurKochi').show();
          $('#eurBhopal').show();
          $('#eurIndore').show();
          $('#eurNagpur').show();
          $('#eurBhubaneswar').show();
          $('#eurLudhiana').show();
          $('#eurJaipur').show();
          $('#eurLucknow').show();
          $('#eurKanpur').show();
          $('#eurDehradun').show();
          $('#eurKolkata').show();

          $('#gbpChennai').hide();
          $('#gbpHyderabad').hide();
          $('#gbpMumbai').hide();
          $('#gbpPatna').hide();
          $('#gbpRaipur').hide();
          $('#gbpAmdavad').hide();
          $('#gbpChandigarh').hide();
          $('#gbpFaridabad').hide();
          $('#gbpJamshedpur').hide();
          $('#gbpBangalore').hide();
          $('#gbpTrivandrum').hide();
          $('#gbpKochi').hide();
          $('#gbpBhopal').hide();
          $('#gbpIndore').hide();
          $('#gbpNagpur').hide();
          $('#gbpBhubaneswar').hide();
          $('#gbpLudhiana').hide();
          $('#gbpJaipur').hide();
          $('#gbpLucknow').hide();
          $('#gbpKanpur').hide();
          $('#gbpDehradun').hide();
          $('#gbpKolkata').hide();

          $('#defaultChennai').hide();
          $('#defaultHyderabad').hide();
          $('#defaultMumbai').hide();
          $('#defaultPatna').hide();
          $('#defaultRaipur').hide();
          $('#defaultAmdavad').hide();
          $('#defaultChandigarh').hide();
          $('#defaultFaridabad').hide();
          $('#defaultJamshedpur').hide();
          $('#defaultBangalore').hide();
          $('#defaultTrivandrum').hide();
          $('#defaultKochi').hide();
          $('#defaultBhopal').hide();
          $('#defaultIndore').hide();
          $('#defaultNagpur').hide();
          $('#defaultBhubaneswar').hide();
          $('#defaultLudhiana').hide();
          $('#defaultJaipur').hide();
          $('#defaultLucknow').hide();
          $('#defaultKanpur').hide();
          $('#defaultDehradun').hide();
          $('#defaultKolkata').hide();

        } else if ($(this).val() == 'GBP') {
          $('#usdChennai').hide();
          $('#usdHyderabad').hide();
          $('#usdMumbai').hide();
          $('#usdPatna').hide();
          $('#usdRaipur').hide();
          $('#usdAmdavad').hide();
          $('#usdChandigarh').hide();
          $('#usdFaridabad').hide();
          $('#usdJamshedpur').hide();
          $('#usdBangalore').hide();
          $('#usdTrivandrum').hide();
          $('#usdKochi').hide();
          $('#usdBhopal').hide();
          $('#usdIndore').hide();
          $('#usdNagpur').hide();
          $('#usdBhubaneswar').hide();
          $('#usdLudhiana').hide();
          $('#usdJaipur').hide();
          $('#usdLucknow').hide();
          $('#usdKanpur').hide();
          $('#usdDehradun').hide();
          $('#usdKolkata').hide();

          $('#eurChennai').hide();
          $('#eurHyderabad').hide();
          $('#eurMumbai').hide();
          $('#eurPatna').hide();
          $('#eurRaipur').hide();
          $('#eurAmdavad').hide();
          $('#eurChandigarh').hide();
          $('#eurFaridabad').hide();
          $('#eurJamshedpur').hide();
          $('#eurBangalore').hide();
          $('#eurTrivandrum').hide();
          $('#eurKochi').hide();
          $('#eurBhopal').hide();
          $('#eurIndore').hide();
          $('#eurNagpur').hide();
          $('#eurBhubaneswar').hide();
          $('#eurLudhiana').hide();
          $('#eurJaipur').hide();
          $('#eurLucknow').hide();
          $('#eurKanpur').hide();
          $('#eurDehradun').hide();
          $('#eurKolkata').hide();

          $('#gbpChennai').show();
          $('#gbpHyderabad').show();
          $('#gbpMumbai').show();
          $('#gbpPatna').show();
          $('#gbpRaipur').show();
          $('#gbpAmdavad').show();
          $('#gbpChandigarh').show();
          $('#gbpFaridabad').show();
          $('#gbpJamshedpur').show();
          $('#gbpBangalore').show();
          $('#gbpTrivandrum').show();
          $('#gbpKochi').show();
          $('#gbpBhopal').show();
          $('#gbpIndore').show();
          $('#gbpNagpur').show();
          $('#gbpBhubaneswar').show();
          $('#gbpLudhiana').show();
          $('#gbpJaipur').show();
          $('#gbpLucknow').show();
          $('#gbpKanpur').show();
          $('#gbpDehradun').show();
          $('#gbpKolkata').show();

          $('#defaultChennai').hide();
          $('#defaultHyderabad').hide();
          $('#defaultMumbai').hide();
          $('#defaultPatna').hide();
          $('#defaultRaipur').hide();
          $('#defaultAmdavad').hide();
          $('#defaultChandigarh').hide();
          $('#defaultFaridabad').hide();
          $('#defaultJamshedpur').hide();
          $('#defaultBangalore').hide();
          $('#defaultTrivandrum').hide();
          $('#defaultKochi').hide();
          $('#defaultBhopal').hide();
          $('#defaultIndore').hide();
          $('#defaultNagpur').hide();
          $('#defaultBhubaneswar').hide();
          $('#defaultLudhiana').hide();
          $('#defaultJaipur').hide();
          $('#defaultLucknow').hide();
          $('#defaultKanpur').hide();
          $('#defaultDehradun').hide();
          $('#defaultKolkata').hide();
        } else {
          $('#usdChennai').hide();
          $('#usdHyderabad').hide();
          $('#usdMumbai').hide();
          $('#usdPatna').hide();
          $('#usdRaipur').hide();
          $('#usdAmdavad').hide();
          $('#usdChandigarh').hide();
          $('#usdFaridabad').hide();
          $('#usdJamshedpur').hide();
          $('#usdBangalore').hide();
          $('#usdTrivandrum').hide();
          $('#usdKochi').hide();
          $('#usdBhopal').hide();
          $('#usdIndore').hide();
          $('#usdNagpur').hide();
          $('#usdBhubaneswar').hide();
          $('#usdLudhiana').hide();
          $('#usdJaipur').hide();
          $('#usdLucknow').hide();
          $('#usdKanpur').hide();
          $('#usdDehradun').hide();
          $('#usdKolkata').hide();

          $('#eurChennai').hide();
          $('#eurHyderabad').hide();
          $('#eurMumbai').hide();
          $('#eurPatna').hide();
          $('#eurRaipur').hide();
          $('#eurAmdavad').hide();
          $('#eurChandigarh').hide();
          $('#eurFaridabad').hide();
          $('#eurJamshedpur').hide();
          $('#eurBangalore').hide();
          $('#eurTrivandrum').hide();
          $('#eurKochi').hide();
          $('#eurBhopal').hide();
          $('#eurIndore').hide();
          $('#eurNagpur').hide();
          $('#eurBhubaneswar').hide();
          $('#eurLudhiana').hide();
          $('#eurJaipur').hide();
          $('#eurLucknow').hide();
          $('#eurKanpur').hide();
          $('#eurDehradun').hide();
          $('#eurKolkata').hide();

          $('#gbpChennai').hide();
          $('#gbpHyderabad').hide();
          $('#gbpMumbai').hide();
          $('#gbpPatna').hide();
          $('#gbpRaipur').hide();
          $('#gbpAmdavad').hide();
          $('#gbpChandigarh').hide();
          $('#gbpFaridabad').hide();
          $('#gbpJamshedpur').hide();
          $('#gbpBangalore').hide();
          $('#gbpTrivandrum').hide();
          $('#gbpKochi').hide();
          $('#gbpBhopal').hide();
          $('#gbpIndore').hide();
          $('#gbpNagpur').hide();
          $('#gbpBhubaneswar').hide();
          $('#gbpLudhiana').hide();
          $('#gbpJaipur').hide();
          $('#gbpLucknow').hide();
          $('#gbpKanpur').hide();
          $('#gbpDehradun').hide();
          $('#gbpKolkata').hide();

          $('#defaultChennai').show();
          $('#defaultHyderabad').show();
          $('#defaultMumbai').show();
          $('#defaultPatna').show();
          $('#defaultRaipur').show();
          $('#defaultAmdavad').show();
          $('#defaultChandigarh').show();
          $('#defaultFaridabad').show();
          $('#defaultJamshedpur').show();
          $('#defaultBangalore').show();
          $('#defaultTrivandrum').show();
          $('#defaultKochi').show();
          $('#defaultBhopal').show();
          $('#defaultIndore').show();
          $('#defaultNagpur').show();
          $('#defaultBhubaneswar').show();
          $('#defaultLudhiana').show();
          $('#defaultJaipur').show();
          $('#defaultLucknow').show();
          $('#defaultKanpur').show();
          $('#defaultDehradun').show();
          $('#defaultKolkata').show();
        }
    });
});
