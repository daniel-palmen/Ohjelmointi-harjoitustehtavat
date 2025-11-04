'use strict';
let x = 0;
let luvut = [];
let pituus = 0;
while(x<5){
    let luku = Number(prompt('Anna lukuja:'));
    luvut.push(luku);
    x = x + 1;
};
pituus = luvut.length;
for(pituus > 0; pituus--;){
    console.log(luvut.pop());
};