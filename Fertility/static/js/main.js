<!-- DISPLAY REGION FORM IF UNITED STATES IS SELECTED | OWNERS --->
$(document).ready(function (e) {
    $('#ChooseCurrency').change(function () {
        if ($(this).val() == 'USD') {
            $('#usdBoard1a').show();
            $('#usdBoard1b').show();
            $('#usdBoard1c').show();
            $('#eurBoard2a').hide();
            $('#eurBoard2b').hide();
            $('#eurBoard2c').hide();
            $('#gbpBoard3a').hide();
            $('#gbpBoard3b').hide();
            $('#gbpBoard3c').hide();
            $('#defaultBoard1a').hide();
            $('#defaultBoard1b').hide();
            $('#defaultBoard1c').hide();
        } else if ($(this).val() == 'EUR') {
            $('#usdBoard1a').hide();
            $('#usdBoard1b').hide();
            $('#usdBoard1c').hide();
            $('#eurBoard2a').show();
            $('#eurBoard2b').show();
            $('#eurBoard2c').show();
            $('#gbpBoard3a').hide();
            $('#gbpBoard3b').hide();
            $('#gbpBoard3c').hide();
            $('#defaultBoard1a').hide();
            $('#defaultBoard1b').hide();
            $('#defaultBoard1c').hide();
        } else if ($(this).val() == 'GBP') {
            $('#usdBoard1a').hide();
            $('#usdBoard1b').hide();
            $('#usdBoard1c').hide();
            $('#eurBoard2a').hide();
            $('#eurBoard2b').hide();
            $('#eurBoard2c').hide();
            $('#gbpBoard3a').show();
            $('#gbpBoard3b').show();
            $('#gbpBoard3c').show();
            $('#defaultBoard1a').hide();
            $('#defaultBoard1b').hide();
            $('#defaultBoard1c').hide();
        } else {
            $('#usdBoard1a').hide();
            $('#usdBoard1b').hide();
            $('#usdBoard1c').hide();
            $('#eurBoard2a').hide();
            $('#eurBoard2b').hide();
            $('#eurBoard2c').hide();
            $('#gbpBoard3a').hide();
            $('#gbpBoard3b').hide();
            $('#gbpBoard3c').hide();
            $('#defaultBoard1a').show();
            $('#defaultBoard1b').show();
            $('#defaultBoard1c').show();
        }
    });
});


<!-- DISPLAY REGION FORM IF UNITED STATES IS SELECTED | OWNERS --->
$(document).ready(function (e) {
    $('#id_clinicState').change(function () {
        if ($(this).val() == 'United States') {
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


<!-- DISPLAY REGION FORM IF UNITED STATES IS SELECTED | OWNERS --->
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
