<!-- DISPLAY NONE US REGIONS IF UNITED STATES IS SELECTED --->

function showDiv(){
       getSelectValue = document.getElementById("States").value;
       if(getSelectValue == "US"){
           document.getElementById("regions").style.display="block";
       }else{
           document.getElementById("regions").style.display="none";
       }
   }


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
