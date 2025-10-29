'use strict';
const num1 = Number(prompt('Anna kokonaisluku 1:'));
const num2 = Number(prompt('Anna kokonaisluku 2:'));
const num3 = Number(prompt('Anna kokonaisluku 3:'));

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

document.getElementById('sum').textContent = sum;
document.getElementById('product').textContent = product;
document.getElementById('average').textContent = average;