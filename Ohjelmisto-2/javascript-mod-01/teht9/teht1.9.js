'use strict';
const luku = Number(prompt('Anna luku:'));
let testi = 2;
let velho = 0;
while(testi < luku){
    if(luku % testi == 0){
        velho = 1;
    }
    testi = testi + 1;
}
if(velho == 1){
    document.getElementById('id1').textContent = 'Luku ' + luku + ' ei ole alkuluku.';
}
else{
    document.getElementById('id1').textContent = 'Luku '+luku+' on alkuluku.';
}