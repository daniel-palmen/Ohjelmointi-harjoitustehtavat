'use strict';
let list = [];
let end = 0;
while(end == 0){
    let luku = Number(prompt('Anna lukuja:'));
    for(let num of list){
        if(num == luku){
            end = 1;
            break;
        }
    }
    if(end == 1){
        break;
    }
    list.push(luku);
}
list.sort();
for(let num of list){
    console.log(num);
}