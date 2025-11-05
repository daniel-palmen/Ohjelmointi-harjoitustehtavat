'use strict';
let nappi = document.getElementById('start');
let vastaus = 0;
nappi.addEventListener("click", function(){
    let numb1 = Number(document.getElementById('num1').value);
    let numb2 = Number(document.getElementById('num2').value);
    let valikko = document.getElementById('operation');
    let valinta = valikko.value;
    if(valinta == 'add'){
        vastaus = numb1 + numb2;
    }
    else if(valinta == 'sub'){
        vastaus = numb1 - numb2;
    }
    else if(valinta == 'multi'){
        vastaus = numb1 * numb2;
    }
    else if(valinta == 'div'){
        vastaus = numb1 / numb2;
    }
    let result = document.getElementById('result').textContent = vastaus;
});
