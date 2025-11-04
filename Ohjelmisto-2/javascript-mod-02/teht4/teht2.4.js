'use strict';
let list = [];
let luku = 1;
while(luku !=0){
    luku = Number(prompt('Anna lukuja, 0 lopettaa:'));
    if(luku == 0){
        break;
    }
    list.push(luku);
}
list.sort();
list.reverse();
for(let i=0;i<list.length;i++){
    console.log(list[i]);
}