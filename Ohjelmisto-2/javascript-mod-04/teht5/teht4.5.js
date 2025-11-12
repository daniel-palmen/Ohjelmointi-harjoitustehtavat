'use strict';
let testi = async function(){
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    const jsonData = await response.json();
    console.log(jsonData.value);
}
testi.call();