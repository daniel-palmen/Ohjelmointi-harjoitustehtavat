'use strict';

function noppa(){
    let luku = Math.floor((Math.random() * 6)+1);
    return luku;
}

let list = [];
let end = 0;
while(end == 0){
    let luku = noppa();
    list.push(luku);
    if(luku == 6){
        break;
    }
}
let paikka = document.getElementById('id1');
for(let num of list){
    let li = document.createElement('li');
    li.textContent = num;
    paikka.appendChild(li);
}