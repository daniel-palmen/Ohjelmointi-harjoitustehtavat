'use strict';
const names = ['John', 'Paul', 'Jones'];
const paikka = document.getElementById('target');
for(let name of names){
    paikka.innerHTML = paikka.innerHTML+`
    <li>${name}</li>`
}