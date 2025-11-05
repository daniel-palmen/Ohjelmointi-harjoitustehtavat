'use strict';
const start = document.getElementById('start');
let vastaus = 0;
start.addEventListener('click', function(){
    let input = document.getElementById('calculation').value;
    if(input.includes('+') == true){
        let lasku = input.split('+');
        vastaus = Number(lasku[0]) + Number(lasku[1]);
    }
    else if(input.includes('-') == true){
        let lasku = input.split('-');
        vastaus = Number(lasku[0]) - Number(lasku[1]);
    }
    else if(input.includes('*') == true){
        let lasku = input.split('*');
        vastaus = Number(lasku[0]) * Number(lasku[1]);
    }
    else if(input.includes('/') == true){
        let lasku = input.split('/');
        vastaus = Number(lasku[0]) / Number(lasku[1]);
    }
    let result = document.getElementById('result').textContent = vastaus;
})