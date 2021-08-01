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
    $('#js_ivf_faqs').show();
  } else {
    $('#js_ivf_cost').hide();
    $('#js_ivf_faqs').hide();
  }
});

$('#id_ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_ivf_cost').show();
    $('#js_ivf_faqs').show();
  } else {
    $('#js_ivf_cost').hide();
    $('#js_ivf_faqs').hide();
  }
});

$('#mild_ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_mild_ivf_cost').show();
    $('#js_mild_ivf_faqs').show();
  } else {
    $('#js_mild_ivf_cost').hide();
    $('#js_mild_ivf_faqs').hide();
  }
});

$('#id_mild_ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_mild_ivf_cost').show();
    $('#js_mild_ivf_faqs').show();
  } else {
    $('#js_mild_ivf_cost').hide();
    $('#js_mild_ivf_faqs').hide();
  }
});

$('#ovarian_ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_ovarian_ivf_cost').show();
    $('#js_ovarian_ivf_faqs').show();
  } else {
    $('#js_ovarian_ivf_cost').hide();
    $('#js_ovarian_ivf_faqs').hide();
  }
});

$('#id_ovarian_ivf_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_ovarian_ivf_cost').show();
    $('#js_ovarian_ivf_faqs').show();
  } else {
    $('#js_ovarian_ivf_cost').hide();
    $('#js_ovarian_ivf_faqs').hide();
  }
});



<!-- 2. řádka --->
$('#iui_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_iui_cost').show();
    $('#js_iui_faqs').show();
  } else {
    $('#js_iui_cost').hide();
    $('#js_iui_faqs').hide();
  }
});

$('#id_iui_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_iui_cost').show();
    $('#js_iui_faqs').show();
  } else {
    $('#js_iui_cost').hide();
    $('#js_iui_faqs').hide();
  }
});

$('#icsi_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_icsi_cost').show();
    $('#js_icsi_faqs').show();
  } else {
    $('#js_icsi_cost').hide();
    $('#js_icsi_faqs').hide();
  }
});

$('#id_icsi_treatment').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_icsi_cost').show();
    $('#js_icsi_faqs').show();
  } else {
    $('#js_icsi_cost').hide();
    $('#js_icsi_faqs').hide();
  }
});

<!-- 3. řádka --->

$('#egg_donation').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_egg_cost').show();
    $('#js_egg_faqs').show();
  } else {
    $('#js_egg_cost').hide();
    $('#js_egg_faqs').hide();
  }
});

$('#id_egg_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_egg_cost').show();
    $('#js_egg_faqs').show();
  } else {
    $('#js_egg_cost').hide();
    $('#js_egg_faqs').hide();
  }
});

$('#known_egg_donation').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_known_egg_cost').show();
    $('#js_known_egg_faqs').show();
  } else {
    $('#js_known_egg_cost').hide();
    $('#js_known_egg_faqs').hide();
  }
});

$('#id_known_egg_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_known_egg_cost').show();
    $('#js_known_egg_faqs').show();
  } else {
    $('#js_known_egg_cost').hide();
    $('#js_known_egg_faqs').hide();
  }
});

$('#sperm_donation').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_sperm_cost').show();
    $('#js_sperm_faqs').show();
  } else {
    $('#js_sperm_cost').hide();
    $('#js_sperm_faqs').hide();
  }
});

$('#id_sperm_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_sperm_cost').show();
    $('#js_sperm_faqs').show();
  } else {
    $('#js_sperm_cost').hide();
    $('#js_sperm_faqs').hide();
  }
});

$('#known_sperm_donation').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_known_sperm_cost').show();
    $('#js_known_sperm_faqs').show();
  } else {
    $('#js_known_sperm_cost').hide();
    $('#js_known_sperm_faqs').hide();
  }
});

$('#id_known_sperm_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_known_sperm_cost').show();
    $('#js_known_sperm_faqs').show();
  } else {
    $('#js_known_sperm_cost').hide();
    $('#js_known_sperm_faqs').hide();
  }
});

$('#embryo_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_embryo_cost').show();
    $('#js_embryo_faqs').show();
  } else {
    $('#js_embryo_cost').hide();
    $('#js_embryo_faqs').hide();
  }
});

$('#id_embryo_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_embryo_cost').show();
    $('#js_embryo_faqs').show();
  } else {
    $('#js_embryo_cost').hide();
    $('#js_embryo_faqs').hide();
  }
});

$('#known_embryo_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_known_embryo_cost').show();
    $('#js_known_embryo_faqs').show();
  } else {
    $('#js_known_embryo_cost').hide();
    $('#js_known_embryo_faqs').hide();
  }
});

$('#id_known_embryo_donor_recipients').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_known_embryo_cost').show();
    $('#js_known_embryo_faqs').show();
  } else {
    $('#js_known_embryo_cost').hide();
    $('#js_known_embryo_faqs').hide();
  }
});

<!-- 4. řádka --->

$('#egg_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_egg_freezing').show();
    $('#js_egg_freezing_faqs').show();
  } else {
    $('#js_egg_freezing').hide();
    $('#js_egg_freezing_faqs').hide();
  }
});

$('#id_egg_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_egg_freezing').show();
    $('#js_egg_freezing_faqs').show();
  } else {
    $('#js_egg_freezing').hide();
    $('#js_egg_freezing_faqs').hide();
  }
});

$('#embryo_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_embryo_freezing').show();
    $('#js_embryo_freezing_faqs').show();
  } else {
    $('#js_embryo_freezing').hide();
    $('#js_embryo_freezing_faqs').hide();
  }
});

$('#id_embryo_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_embryo_freezing').show();
    $('#js_embryo_freezing_faqs').show();
  } else {
    $('#js_embryo_freezing').hide();
    $('#js_embryo_freezing_faqs').hide();
  }
});

$('#sperm_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_sperm_freezing').show();
    $('#js_sperm_freezing_faqs').show();
  } else {
    $('#js_sperm_freezing').hide();
    $('#js_sperm_freezing_faqs').hide();
  }
});

$('#id_sperm_freezing').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_sperm_freezing').show();
    $('#js_sperm_freezing_faqs').show();
  } else {
    $('#js_sperm_freezing').hide();
    $('#js_sperm_freezing_faqs').hide();
  }
});

$('#assisted_hatching').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_assisted_hatching').show();
    $('#js_assisted_hatching_faqs').show();
  } else {
    $('#js_assisted_hatching').hide();
    $('#js_assisted_hatching_faqs').hide();
  }
});

<!-- 5. řádka --->

$('#surrogacy').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_surrogacy_cost').show();
    $('#js_surrogacy_faqs').show();
  } else {
    $('#js_surrogacy_cost').hide();
    $('#js_surrogacy_faqs').hide();
  }
});

$('#id_surrogacy').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_surrogacy_cost').show();
    $('#js_surrogacy_faqs').show();
  } else {
    $('#js_surrogacy_cost').hide();
    $('#js_surrogacy_faqs').hide();
  }
});

$('#pgd').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_pgd_cost').show();
    $('#js_pgd_cost_faqs').show();
  } else {
    $('#js_pgd_cost').hide();
    $('#js_pgd_cost_faqs').hide();
  }
});

$('#vasectomy_reversal').on('change', function(){
  if ( $(this).is(":checked")) {
    $('#js_vasectomy_reversal').show();
    $('#js_vasectomy_reversal_faqs').show();
  } else {
    $('#js_vasectomy_reversal').hide();
    $('#js_vasectomy_reversal_faqs').hide();
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


if (localStorage.getItem('popup') != 'shown') {
  $('.popup-banner').show();
  $('#formModal').modal('show')
  localStorage.setItem('popup','shown')
};
