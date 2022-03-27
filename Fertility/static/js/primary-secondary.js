<!-- DISPLAY REGION FORM IF UNITED STATES IS SELECTED | OWNERS --->

var select = document.querySelector('#ChooseCurrency');
var selectOption = select.options[select.selectedIndex];
var lastSelected = localStorage.getItem('select');

var myTreatmentCostsUSDCurrency = document.querySelectorAll('.treatmentCostsUSDCurrency');
var myTreatmentCostsEURCurrency = document.querySelectorAll('.treatmentCostsEURCurrency');
var myTreatmentCostsGBPCurrency = document.querySelectorAll('.treatmentCostsGBPCurrency');

var myUSDTreatmentCostsUSDCurrency = document.querySelectorAll('.EURtreatmentCostsUSDCurrency');
var myEURTreatmentCostsEURCurrency = document.querySelectorAll('.EURtreatmentCostsEURCurrency');
var myGBPTreatmentCostsGBPCurrency = document.querySelectorAll('.EURtreatmentCostsGBPCurrency');

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
        for (var i=0;i<myTreatmentCostsUSDCurrency.length;i+=1){
            myTreatmentCostsUSDCurrency[i].style.display = "initial";
        }
        for (var i=0;i<myUSDTreatmentCostsUSDCurrency.length;i+=1){
            myUSDTreatmentCostsUSDCurrency[i].style.display = "initial";
        }
        for (var i=0;i<myTreatmentCostsEURCurrency.length;i+=1){
            myTreatmentCostsEURCurrency[i].style.display = "none";
        }
        for (var i=0;i<myEURTreatmentCostsEURCurrency.length;i+=1){
            myEURTreatmentCostsEURCurrency[i].style.display = "none";
        }
        for (var i=0;i<myTreatmentCostsGBPCurrency.length;i+=1){
            myTreatmentCostsGBPCurrency[i].style.display = "none";
        }
        for (var i=0;i<myGBPTreatmentCostsGBPCurrency.length;i+=1){
            myGBPTreatmentCostsGBPCurrency[i].style.display = "none";
        }

      } else if (lastSelected == 'EUR') {
        for (var i=0;i<myTreatmentCostsUSDCurrency.length;i+=1){
            myTreatmentCostsUSDCurrency[i].style.display = "none";
        }
        for (var i=0;i<myUSDTreatmentCostsUSDCurrency.length;i+=1){
            myUSDTreatmentCostsUSDCurrency[i].style.display = "none";
        }
        for (var i=0;i<myTreatmentCostsEURCurrency.length;i+=1){
            myTreatmentCostsEURCurrency[i].style.display = "initial";
        }
        for (var i=0;i<myEURTreatmentCostsEURCurrency.length;i+=1){
            myEURTreatmentCostsEURCurrency[i].style.display = "initial";
        }
        for (var i=0;i<myTreatmentCostsGBPCurrency.length;i+=1){
            myTreatmentCostsGBPCurrency[i].style.display = "none";
        }
        for (var i=0;i<myGBPTreatmentCostsGBPCurrency.length;i+=1){
            myGBPTreatmentCostsGBPCurrency[i].style.display = "none";
        }

      } else if (lastSelected == 'GBP') {
        for (var i=0;i<myTreatmentCostsUSDCurrency.length;i+=1){
            myTreatmentCostsUSDCurrency[i].style.display = "none";
        }
        for (var i=0;i<myUSDTreatmentCostsUSDCurrency.length;i+=1){
            myUSDTreatmentCostsUSDCurrency[i].style.display = "none";
        }
        for (var i=0;i<myTreatmentCostsEURCurrency.length;i+=1){
            myTreatmentCostsEURCurrency[i].style.display = "none";
        }
        for (var i=0;i<myEURTreatmentCostsEURCurrency.length;i+=1){
            myEURTreatmentCostsEURCurrency[i].style.display = "none";
        }
        for (var i=0;i<myTreatmentCostsGBPCurrency.length;i+=1){
            myTreatmentCostsGBPCurrency[i].style.display = "initial";
        }
        for (var i=0;i<myGBPTreatmentCostsGBPCurrency.length;i+=1){
            myGBPTreatmentCostsGBPCurrency[i].style.display = "initial";
        }

      } else {
        for (var i=0;i<myTreatmentCostsUSDCurrency.length;i+=1){
            myTreatmentCostsUSDCurrency[i].style.display = "initial";
        }
        for (var i=0;i<myUSDTreatmentCostsUSDCurrency.length;i+=1){
            myUSDTreatmentCostsUSDCurrency[i].style.display = "initial";
        }
        for (var i=0;i<myTreatmentCostsEURCurrency.length;i+=1){
            myTreatmentCostsEURCurrency[i].style.display = "none";
        }
        for (var i=0;i<myEURTreatmentCostsEURCurrency.length;i+=1){
            myEURTreatmentCostsEURCurrency[i].style.display = "none";
        }
        for (var i=0;i<myTreatmentCostsGBPCurrency.length;i+=1){
            myTreatmentCostsGBPCurrency[i].style.display = "none";
        }
        for (var i=0;i<myGBPTreatmentCostsGBPCurrency.length;i+=1){
            myGBPTreatmentCostsGBPCurrency[i].style.display = "none";
        }
      }
    }
    else{
    $('#ChooseCurrency').change(function () {
        if ($(this).val() == 'USD') {
            for (var i=0;i<myTreatmentCostsUSDCurrency.length;i+=1){
                myTreatmentCostsUSDCurrency[i].style.display = "initial";
            }
            for (var i=0;i<myUSDTreatmentCostsUSDCurrency.length;i+=1){
                myUSDTreatmentCostsUSDCurrency[i].style.display = "initial";
            }
            for (var i=0;i<myTreatmentCostsEURCurrency.length;i+=1){
                myTreatmentCostsEURCurrency[i].style.display = "none";
            }
            for (var i=0;i<myEURTreatmentCostsEURCurrency.length;i+=1){
                myEURTreatmentCostsEURCurrency[i].style.display = "none";
            }
            for (var i=0;i<myTreatmentCostsGBPCurrency.length;i+=1){
                myTreatmentCostsGBPCurrency[i].style.display = "none";
            }
            for (var i=0;i<myGBPTreatmentCostsGBPCurrency.length;i+=1){
                myGBPTreatmentCostsGBPCurrency[i].style.display = "none";
            }

        } else if ($(this).val() == 'EUR') {
            for (var i=0;i<myTreatmentCostsUSDCurrency.length;i+=1){
                myTreatmentCostsUSDCurrency[i].style.display = "none";
            }
            for (var i=0;i<myUSDTreatmentCostsUSDCurrency.length;i+=1){
                myUSDTreatmentCostsUSDCurrency[i].style.display = "none";
            }
            for (var i=0;i<myTreatmentCostsEURCurrency.length;i+=1){
                myTreatmentCostsEURCurrency[i].style.display = "initial";
            }
            for (var i=0;i<myEURTreatmentCostsEURCurrency.length;i+=1){
                myEURTreatmentCostsEURCurrency[i].style.display = "initial";
            }
            for (var i=0;i<myTreatmentCostsGBPCurrency.length;i+=1){
                myTreatmentCostsGBPCurrency[i].style.display = "none";
            }
            for (var i=0;i<myGBPTreatmentCostsGBPCurrency.length;i+=1){
                myGBPTreatmentCostsGBPCurrency[i].style.display = "none";
            }

        } else if ($(this).val() == 'GBP') {
            for (var i=0;i<myTreatmentCostsUSDCurrency.length;i+=1){
                myTreatmentCostsUSDCurrency[i].style.display = "none";
            }
            for (var i=0;i<myUSDTreatmentCostsUSDCurrency.length;i+=1){
                myUSDTreatmentCostsUSDCurrency[i].style.display = "none";
            }
            for (var i=0;i<myTreatmentCostsEURCurrency.length;i+=1){
                myTreatmentCostsEURCurrency[i].style.display = "none";
            }
            for (var i=0;i<myEURTreatmentCostsEURCurrency.length;i+=1){
                myEURTreatmentCostsEURCurrency[i].style.display = "none";
            }
            for (var i=0;i<myTreatmentCostsGBPCurrency.length;i+=1){
                myTreatmentCostsGBPCurrency[i].style.display = "initial";
            }
            for (var i=0;i<myGBPTreatmentCostsGBPCurrency.length;i+=1){
                myGBPTreatmentCostsGBPCurrency[i].style.display = "initial";
            }

        } else {
            for (var i=0;i<myTreatmentCostsUSDCurrency.length;i+=1){
                myTreatmentCostsUSDCurrency[i].style.display = "initial";
            }
            for (var i=0;i<myUSDTreatmentCostsUSDCurrency.length;i+=1){
                myUSDTreatmentCostsUSDCurrency[i].style.display = "initial";
            }
            for (var i=0;i<myTreatmentCostsEURCurrency.length;i+=1){
                myTreatmentCostsEURCurrency[i].style.display = "none";
            }
            for (var i=0;i<myEURTreatmentCostsEURCurrency.length;i+=1){
                myEURTreatmentCostsEURCurrency[i].style.display = "none";
            }
            for (var i=0;i<myTreatmentCostsGBPCurrency.length;i+=1){
                myTreatmentCostsGBPCurrency[i].style.display = "none";
            }
            for (var i=0;i<myGBPTreatmentCostsGBPCurrency.length;i+=1){
                myGBPTreatmentCostsGBPCurrency[i].style.display = "none";
            }
        }
    });
  };
});
