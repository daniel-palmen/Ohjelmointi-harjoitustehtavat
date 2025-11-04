'use strict';

function noppa(sides){
    let luku = Math.floor((Math.random() * sides)+1);
    return luku;
}

let list = [];
let end = 0;
let sides = Number(prompt('Anna nopan sivujen määrä:'))
while(end == 0){
    let luku = noppa(sides);
    list.push(luku);
    if(luku == sides){
        break;
    }
}
let paikka = document.getElementById('id1');
for(let num of list){
    let li = document.createElement('li');
    li.textContent = num;
    paikka.appendChild(li);
}