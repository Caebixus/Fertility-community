<!-- DISPLAY REGION FORM IF UNITED STATES IS SELECTED | OWNERS --->

var select = document.querySelector('#ChooseCurrency');
var selectOption = select.options[select.selectedIndex];
var lastSelected = localStorage.getItem('select');
var myPackageCostsUSDCurrency = document.querySelectorAll('.packageCostsUSDCurrency'),
    i = 0,
    l = myPackageCostsUSDCurrency.length;

var myPackageCostsEURCurrency = document.querySelectorAll('.packageCostsEURCurrency'),
    i = 0,
    l = myPackageCostsEURCurrency.length;

var myPackageCostsGBPCurrency = document.querySelectorAll('.packageCostsGBPCurrency'),
    i = 0,
    l = myPackageCostsGBPCurrency.length;


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
            myPackageCostsUSDCurrency[i].style.display = 'initial';
            myPackageCostsEURCurrency[i].style.display = 'none';
            myPackageCostsGBPCurrency[i].style.display = 'none';
        }

      } else if (lastSelected == 'EUR') {
        for (i; i < l; i++) {
            myPackageCostsUSDCurrency[i].style.display = 'none';
            myPackageCostsEURCurrency[i].style.display = 'initial';
            myPackageCostsGBPCurrency[i].style.display = 'none';
        }


      } else if (lastSelected == 'GBP') {
        for (i; i < l; i++) {
            myPackageCostsUSDCurrency[i].style.display = 'none';
            myPackageCostsEURCurrency[i].style.display = 'none';
            myPackageCostsGBPCurrency[i].style.display = 'initial';
        }

      } else {
        for (i; i < l; i++) {
            myPackageCostsUSDCurrency[i].style.display = 'initial';
            myPackageCostsEURCurrency[i].style.display = 'none';
            myPackageCostsGBPCurrency[i].style.display = 'none';
        }
      }
    }
    else{
    $('#ChooseCurrency').change(function () {
        if ($(this).val() == 'USD') {
          for (i; i < l; i++) {
              myPackageCostsUSDCurrency[i].style.display = 'initial';
              myPackageCostsEURCurrency[i].style.display = 'none';
              myPackageCostsGBPCurrency[i].style.display = 'none';
          }

        } else if ($(this).val() == 'EUR') {
          for (i; i < l; i++) {
              myPackageCostsUSDCurrency[i].style.display = 'none';
              myPackageCostsEURCurrency[i].style.display = 'initial';
              myPackageCostsGBPCurrency[i].style.display = 'none';
          }

        } else if ($(this).val() == 'GBP') {
          for (i; i < l; i++) {
              myPackageCostsUSDCurrency[i].style.display = 'none';
              myPackageCostsEURCurrency[i].style.display = 'none';
              myPackageCostsGBPCurrency[i].style.display = 'initial';
          }

        } else {
          for (i; i < l; i++) {
              myPackageCostsUSDCurrency[i].style.display = 'initial';
              myPackageCostsEURCurrency[i].style.display = 'none';
              myPackageCostsGBPCurrency[i].style.display = 'none';
          }
        }
    });
  };
});
