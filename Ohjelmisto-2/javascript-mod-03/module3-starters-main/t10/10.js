'use strict';
const source  = document.getElementById('source');
const target = document.getElementById('target');
source.addEventListener('submit', (event)=>{
    event.preventDefault();
    let fName = source[0].value;
    let sName = source[1].value;
    target.textContent = `Your name is ${fName} ${sName}.`;
});