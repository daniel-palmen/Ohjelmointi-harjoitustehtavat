'use strict';
const naem = prompt('Anna nimesi:');
const luku = Math.floor((Math.random() * 4) + 1);
let house = '';
if (luku == 1){
    house = 'Gryffindor';
}
else if (luku == 2){
    house = 'Slytherin';
}
else if (luku == 3){
    house = 'Hufflepuff';
}
else if (luku == 4){
    house = 'Ravenclaw';
}

document.getElementById('choise').textContent = naem + ', you are ' + house + '.';