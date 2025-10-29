'use strict';
let neliö = 0;
const answer = confirm('Should I calculate square root?');
if(answer == false){
    document.getElementById('id1').textContent = 'The square root is not calculated.';
}
else if(answer == true){
    const luku = Number(prompt('Anna luku:'));
    neliö = Math.sqrt(luku)
    document.getElementById('id1').textContent = neliö;
}