'use strict';

function even(list1){
    let list2 = [];
    for(let luku of list1){
        let lasku = luku % 2;
        if(lasku == 0){
            list2.push(luku);
        }
    }
    return list2;
}

let list1 = [1,2,3,4,5,6,7,8,9,10];
console.log(list1);
let list2 = even(list1);
console.log(list2);