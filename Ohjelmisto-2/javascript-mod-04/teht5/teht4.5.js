'use strict';
let testi = async function(){
const responce = await fetch('https://api.chucknorris.io/jokes/random');
console.log(responce);
}