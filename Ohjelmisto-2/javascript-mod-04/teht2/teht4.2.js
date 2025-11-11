'use strict';
const tvForm = document.querySelector('#tvForm');
tvForm.addEventListener('submit', async function(event) {
    event.preventDefault();
    const code = document.querySelector('input[id=query]').value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${code}`);
        const jsonData = await response.json();
        console.log(jsonData);
    } catch (error) {
        console.log(error.message);
    }
});