'use strict';
let lista = [];
let määrä = Number(prompt('Give number of participants:'));
let kierros = 0;
while(kierros < määrä){
    let nimi = prompt('Give participants name:');
    lista.push(nimi);
    kierros++;
}
lista.sort();
let paikka = document.getElementById('id1');
for(let i=0;i<lista.length;i++){
    let li = document.createElement('li');
    li.textContent = lista[i];
    paikka.appendChild(li);
}