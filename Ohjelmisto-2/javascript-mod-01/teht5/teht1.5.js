'use strict';
const vuosi = Number(prompt('Anna vuosiluku'));

if (vuosi % 400 == 0){
    document.getElementById('id1').textContent = 'Vuosi ' + vuosi + ' on karkausvuosi';
}
else if (vuosi % 4 == 0 && vuosi % 100 !== 0){
    document.getElementById('id1').textContent = 'Vuosi ' + vuosi + ' on karkausvuosi';
}
else{
    document.getElementById('id1').textContent = 'Vuosi ' + vuosi + ' ei ole karkausvuosi';
}