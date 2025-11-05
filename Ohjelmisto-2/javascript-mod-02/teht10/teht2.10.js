'use strict';
let array = [];
const numOfCan = Number(prompt('Anna äänestettävien määrä:'));
for(let i=0;i<numOfCan;i++){
    let cname = prompt('Anna äänestettävien nimet:');
    let person = {name: cname, votes: 0};
    array.push(person);
}
const voters = Number(prompt('Anna äänestäjien määrä:'));
for(let i=0;i<voters;i++){
    let vote = prompt('Anna ääni:');
    for(let j=0;j<array.length;j++){
        if(vote == array[j].name){
            array[j].votes++;
        }
    }
}
array.sort((a, b) => b.votes - a.votes);
console.log(`Voittaja on ${array[0].name} ${array[0].votes} äänellä.`);
console.log('lopputulos:');
for(let i=0;i<array.length;i++){
    console.log(array[i].name+': '+array[i].votes+' ääntä');
}