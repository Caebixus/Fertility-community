<!-- DISPLAY REGION FORM IF UNITED STATES IS SELECTED | OWNERS --->

var select = document.querySelector('#ChooseCurrency');
var selectOption = select.options[select.selectedIndex];
var lastSelected = localStorage.getItem('select');

if(lastSelected) {
    select.value = lastSelected;
}

select.onchange = function () {
   lastSelected = select.options[select.selectedIndex].value;
   console.log(lastSelected);
   localStorage.setItem('select', lastSelected);
   location.reload()
}

$(document).ready(function (e) {
    if(lastSelected){
      if (lastSelected == 'USD') {
        $('#quickInfoUSD').show();
        $('#quickInfoUSD1').show();
        $('#quickInfoUSD2').show();
        $('#quickInfoUSD3').show();
        $('#quickInfoUSD4').show();

        $('#quickInfoEUR').hide();
        $('#quickInfoEUR1').hide();
        $('#quickInfoEUR2').hide();
        $('#quickInfoEUR3').hide();
        $('#quickInfoEUR4').hide();

        $('#quickInfoGBP').hide();
        $('#quickInfoGBP1').hide();
        $('#quickInfoGBP2').hide();
        $('#quickInfoGBP3').hide();
        $('#quickInfoGBP4').hide();

      } else if (lastSelected == 'EUR') {
        $('#quickInfoUSD').hide();
        $('#quickInfoUSD1').hide();
        $('#quickInfoUSD2').hide();
        $('#quickInfoUSD3').hide();
        $('#quickInfoUSD4').hide();

        $('#quickInfoEUR').show();
        $('#quickInfoEUR1').show();
        $('#quickInfoEUR2').show();
        $('#quickInfoEUR3').show();
        $('#quickInfoEUR4').show();

        $('#quickInfoGBP').hide();
        $('#quickInfoGBP1').hide();
        $('#quickInfoGBP2').hide();
        $('#quickInfoGBP3').hide();
        $('#quickInfoGBP4').hide();

      } else if (lastSelected == 'GBP') {
        $('#quickInfoUSD').hide();
        $('#quickInfoUSD1').hide();
        $('#quickInfoUSD2').hide();
        $('#quickInfoUSD3').hide();
        $('#quickInfoUSD4').hide();

        $('#quickInfoEUR').hide();
        $('#quickInfoEUR1').hide();
        $('#quickInfoEUR2').hide();
        $('#quickInfoEUR3').hide();
        $('#quickInfoEUR4').hide();

        $('#quickInfoGBP').show();
        $('#quickInfoGBP1').show();
        $('#quickInfoGBP2').show();
        $('#quickInfoGBP3').show();
        $('#quickInfoGBP4').show();

      } else {
        $('#quickInfoUSD').show();
        $('#quickInfoUSD1').show();
        $('#quickInfoUSD2').show();
        $('#quickInfoUSD3').show();
        $('#quickInfoUSD4').show();

        $('#quickInfoEUR').hide();
        $('#quickInfoEUR1').hide();
        $('#quickInfoEUR2').hide();
        $('#quickInfoEUR3').hide();
        $('#quickInfoEUR4').hide();

        $('#quickInfoGBP').hide();
        $('#quickInfoGBP1').hide();
        $('#quickInfoGBP2').hide();
        $('#quickInfoGBP3').hide();
        $('#quickInfoGBP4').hide();
      }
    }
    else{
    $('#ChooseCurrency').change(function () {
        if ($(this).val() == 'USD') {
          $('#quickInfoUSD').show();
          $('#quickInfoUSD1').show();
          $('#quickInfoUSD2').show();
          $('#quickInfoUSD3').show();
          $('#quickInfoUSD4').show();

          $('#quickInfoEUR').hide();
          $('#quickInfoEUR1').hide();
          $('#quickInfoEUR2').hide();
          $('#quickInfoEUR3').hide();
          $('#quickInfoEUR4').hide();

          $('#quickInfoGBP').hide();
          $('#quickInfoGBP1').hide();
          $('#quickInfoGBP2').hide();
          $('#quickInfoGBP3').hide();
          $('#quickInfoGBP4').hide();

        } else if ($(this).val() == 'EUR') {
          $('#quickInfoUSD').hide();
          $('#quickInfoUSD1').hide();
          $('#quickInfoUSD2').hide();
          $('#quickInfoUSD3').hide();
          $('#quickInfoUSD4').hide();

          $('#quickInfoEUR').show();
          $('#quickInfoEUR1').show();
          $('#quickInfoEUR2').show();
          $('#quickInfoEUR3').show();
          $('#quickInfoEUR4').show();

          $('#quickInfoGBP').hide();
          $('#quickInfoGBP1').hide();
          $('#quickInfoGBP2').hide();
          $('#quickInfoGBP3').hide();
          $('#quickInfoGBP4').hide();

        } else if ($(this).val() == 'GBP') {
          $('#quickInfoUSD').hide();
          $('#quickInfoUSD1').hide();
          $('#quickInfoUSD2').hide();
          $('#quickInfoUSD3').hide();
          $('#quickInfoUSD4').hide();

          $('#quickInfoEUR').hide();
          $('#quickInfoEUR1').hide();
          $('#quickInfoEUR2').hide();
          $('#quickInfoEUR3').hide();
          $('#quickInfoEUR4').hide();

          $('#quickInfoGBP').show();
          $('#quickInfoGBP1').show();
          $('#quickInfoGBP2').show();
          $('#quickInfoGBP3').show();
          $('#quickInfoGBP4').show();

        } else {
          $('#quickInfoUSD').show();
          $('#quickInfoUSD1').show();
          $('#quickInfoUSD2').show();
          $('#quickInfoUSD3').show();
          $('#quickInfoUSD4').show();

          $('#quickInfoEUR').hide();
          $('#quickInfoEUR1').hide();
          $('#quickInfoEUR2').hide();
          $('#quickInfoEUR3').hide();
          $('#quickInfoEUR4').hide();

          $('#quickInfoGBP').hide();
          $('#quickInfoGBP1').hide();
          $('#quickInfoGBP2').hide();
          $('#quickInfoGBP3').hide();
          $('#quickInfoGBP4').hide();
        }
    });
  };
});
