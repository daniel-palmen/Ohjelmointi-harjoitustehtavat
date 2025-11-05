'use strict';
const trigger = document.getElementById('trigger');
trigger.addEventListener("mouseover", function(){
    const target = document.getElementById('target').src = "img/picB.jpg";
});
trigger.addEventListener("mouseout", function(){
    const target = document.getElementById('target').src = "img/picA.jpg";
});