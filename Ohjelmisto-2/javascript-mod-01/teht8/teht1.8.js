'use strict';
const ekaVuosi = Number(prompt('Anna aloitusvuosi:'));
const tokaVuosi = Number(prompt('Anna lopetusvuosi:'));
let array = [];
let vuosi = ekaVuosi
const list = document.getElementById('list');
while(vuosi < tokaVuosi + 1){
    if (vuosi % 400 == 0){
        array.push(vuosi);
    }
    else if (vuosi % 4 == 0 && vuosi % 100 !== 0){
        array.push(vuosi);
    }
    vuosi = vuosi + 1;
}
for (let i = 0; i < array.length; ++i) {
            let li = document.createElement('li');
            li.innerText = array[i];
            list.appendChild(li);
}