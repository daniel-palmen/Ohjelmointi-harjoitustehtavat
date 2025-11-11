'use strict';
const tvForm = document.querySelector('#tvForm');
const target = document.querySelector('#results');
tvForm.addEventListener('submit', async function(event) {
    target.innerHTML = '';
    event.preventDefault();
    let jsonData = [];
    const code = document.querySelector('input[id=query]').value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`);
        jsonData = await response.json();
        console.log(jsonData);
    } catch (error) {
        console.log('EI TOIMI!!!!');
        console.log(error.message);
    }
    for(let i=0;i<jsonData.length;i++){
        let article = document.createElement('article');
        article.innerHTML =article.innerHTML + `
        <h2>${jsonData[i].show.name}</h2>
        <a href='${jsonData[i].show.url}' target='_blank'>Linkki</a>
        <p></p>
        <img src='${jsonData[i].show.image?.medium}' alt='${jsonData[i].show.name}'>
        <div>${jsonData[i].show.summary}</div>
        `
        target.appendChild(article);
    }
});