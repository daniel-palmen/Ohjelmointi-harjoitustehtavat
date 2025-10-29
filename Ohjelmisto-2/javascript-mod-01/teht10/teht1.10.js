'use strict';
const määrä = Number(prompt('Anna noppien määrä:'));
const luku = Number(prompt('Anna haluttu summa:'));
let esiintymät = 0;
let kierrokset = 10000;

for(let i = 0; i < kierrokset; i++){
    let sum = 0;
    for(let j = 0; j < määrä; j++){
        sum += Math.floor((Math.random() * 6) + 1);
    }
    if(sum == luku){
        esiintymät++;
    }
}
let tuloste = (esiintymät / kierrokset) * 100;
tuloste = tuloste.toFixed(2);
document.getElementById('id1').textContent = 'Probability to get sum '+luku+' with '+määrä+' dice is '+tuloste+'%';