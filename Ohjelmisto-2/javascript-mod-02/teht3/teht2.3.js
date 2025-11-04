'use strict';
let list = [];
let maara = 6;
for(let i=0;i<maara;i++){
    let hmm = i + 1;
    let nimi = prompt('Anna '+hmm+'. koiran nimi:');
    list.push(nimi);
}
list.sort();
list.reverse();
let paikka = document.getElementById('id1');
for(let nimi of list){
    let li = document.createElement('li');
    li.textContent = nimi;
    paikka.appendChild(li);
}