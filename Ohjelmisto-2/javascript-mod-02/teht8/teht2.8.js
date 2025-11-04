'use strict';

function concat(list){
    let text = '';
    for(let sana of list){
        text = text+sana;
    }
    return text;
}

let list = ['kissa','koira','hevonen'];

document.getElementById('id1').textContent = concat(list);
