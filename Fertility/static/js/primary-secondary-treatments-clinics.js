<!-- DISPLAY REGION FORM IF UNITED STATES IS SELECTED | OWNERS --->

var select = document.querySelector('#ChooseCurrency');
var selectOption = select.options[select.selectedIndex];
var lastSelected = localStorage.getItem('select');

var myTreatmentCostsUSDCurrency = document.querySelectorAll('.treatmentCostsUSDCurrency'),
    i = 0,
    l = myTreatmentCostsUSDCurrency.length;
var myTreatmentCostsEURCurrency = document.querySelectorAll('.treatmentCostsEURCurrency'),
    i = 0,
    l = myTreatmentCostsEURCurrency.length;
var myTreatmentCostsGBPCurrency = document.querySelectorAll('.treatmentCostsGBPCurrency'),
    i = 0,
    l = myTreatmentCostsGBPCurrency.length;

var myEURTreatmentCostsEURCurrency = document.querySelectorAll('.EURtreatmentCostsEURCurrency'),
    i = 0,
    l = myEURTreatmentCostsEURCurrency.length;
var myUSDTreatmentCostsUSDCurrency = document.querySelectorAll('.EURtreatmentCostsUSDCurrency'),
    i = 0,
    l = myUSDTreatmentCostsUSDCurrency.length;
var myGBPTreatmentCostsGBPCurrency = document.querySelectorAll('.EURtreatmentCostsGBPCurrency'),
    i = 0,
    l = myGBPTreatmentCostsGBPCurrency.length;

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
        for (i; i < l; i++) {
            myTreatmentCostsUSDCurrency[i].style.display = 'initial';
            myUSDTreatmentCostsUSDCurrency[i].style.display = 'initial';
            myTreatmentCostsEURCurrency[i].style.display = 'none';
            myEURTreatmentCostsEURCurrency[i].style.display = 'none';
            myTreatmentCostsGBPCurrency[i].style.display = 'none';
            myGBPTreatmentCostsGBPCurrency[i].style.display = 'none';
        }

      } else if (lastSelected == 'EUR') {
        for (i; i < l; i++) {
            myTreatmentCostsUSDCurrency[i].style.display = 'none';
            myUSDTreatmentCostsUSDCurrency[i].style.display = 'none';
            myTreatmentCostsEURCurrency[i].style.display = 'initial';
            myEURTreatmentCostsEURCurrency[i].style.display = 'initial';
            myTreatmentCostsGBPCurrency[i].style.display = 'none';
            myGBPTreatmentCostsGBPCurrency[i].style.display = 'none';
        }

      } else if (lastSelected == 'GBP') {
        for (i; i < l; i++) {
            myTreatmentCostsUSDCurrency[i].style.display = 'none';
            myUSDTreatmentCostsUSDCurrency[i].style.display = 'none';
            myTreatmentCostsEURCurrency[i].style.display = 'none';
            myEURTreatmentCostsEURCurrency[i].style.display = 'none';
            myTreatmentCostsGBPCurrency[i].style.display = 'initial';
            myGBPTreatmentCostsGBPCurrency[i].style.display = 'initial';
        }

      } else {
        for (i; i < l; i++) {
            myTreatmentCostsUSDCurrency[i].style.display = 'initial';
            myUSDTreatmentCostsUSDCurrency[i].style.display = 'initial';
            myTreatmentCostsEURCurrency[i].style.display = 'none';
            myEURTreatmentCostsEURCurrency[i].style.display = 'none';
            myTreatmentCostsGBPCurrency[i].style.display = 'none';
            myGBPTreatmentCostsGBPCurrency[i].style.display = 'none';
        }
      }
    }
    else{
    $('#ChooseCurrency').change(function () {
        if ($(this).val() == 'USD') {
          for (i; i < l; i++) {
            myTreatmentCostsUSDCurrency[i].style.display = 'initial';
            myUSDTreatmentCostsUSDCurrency[i].style.display = 'initial';
            myTreatmentCostsEURCurrency[i].style.display = 'none';
            myEURTreatmentCostsEURCurrency[i].style.display = 'none';
            myTreatmentCostsGBPCurrency[i].style.display = 'none';
            myGBPTreatmentCostsGBPCurrency[i].style.display = 'none';
          }

        } else if ($(this).val() == 'EUR') {
          for (i; i < l; i++) {
            myTreatmentCostsUSDCurrency[i].style.display = 'none';
            myUSDTreatmentCostsUSDCurrency[i].style.display = 'none';
            myTreatmentCostsEURCurrency[i].style.display = 'initial';
            myEURTreatmentCostsEURCurrency[i].style.display = 'initial';
            myTreatmentCostsGBPCurrency[i].style.display = 'none';
            myGBPTreatmentCostsGBPCurrency[i].style.display = 'none';
          }

        } else if ($(this).val() == 'GBP') {
          for (i; i < l; i++) {
            myTreatmentCostsUSDCurrency[i].style.display = 'none';
            myUSDTreatmentCostsUSDCurrency[i].style.display = 'none';
            myTreatmentCostsEURCurrency[i].style.display = 'none';
            myEURTreatmentCostsEURCurrency[i].style.display = 'none';
            myTreatmentCostsGBPCurrency[i].style.display = 'initial';
            myGBPTreatmentCostsGBPCurrency[i].style.display = 'initial';
          }

        } else {
          for (i; i < l; i++) {
            myTreatmentCostsUSDCurrency[i].style.display = 'initial';
            myUSDTreatmentCostsUSDCurrency[i].style.display = 'initial';
            myTreatmentCostsEURCurrency[i].style.display = 'none';
            myEURTreatmentCostsEURCurrency[i].style.display = 'none';
            myTreatmentCostsGBPCurrency[i].style.display = 'none';
            myGBPTreatmentCostsGBPCurrency[i].style.display = 'none';
          }
        }
    });
  };
});
