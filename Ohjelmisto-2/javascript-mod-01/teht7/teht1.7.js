'use strict';
const määrä = Number(prompt('Anna heittojen määrä:'));
let kierros = 0;
let summa = 0;
while(määrä > kierros){
    kierros = kierros + 1;
    const luku = Math.floor((Math.random() * 6)+1);
    summa = summa + luku;
}
document.getElementById('id1').textContent = 'Heittojen summa on ' + summa;