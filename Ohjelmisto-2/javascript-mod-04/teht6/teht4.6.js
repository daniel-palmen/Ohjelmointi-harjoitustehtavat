'use strict';
const haku = document.querySelector('#haku');
const target = document.querySelector('#target');
haku.addEventListener('submit', async function(event){
    target.innerHTML = '';
    event.preventDefault();
    let code = document.querySelector('input[id=query]').value;
    let jsonData = [];
    try{
        const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${code}`);
        const data = await response.json();
        jsonData = data.result;
        console.log(jsonData);
    } catch(error){
        console.log('EI TOIMI!');
        console.log(error.message);
    }
    for(let i=0;i<jsonData.length;i++){
        let article = document.createElement('article');
        article.innerHTML = `
        <p>${jsonData[i].value}</p>
        `
        target.appendChild(article);
    }
})