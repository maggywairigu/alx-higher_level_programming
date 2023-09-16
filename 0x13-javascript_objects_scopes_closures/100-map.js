#!/usr/bin/node
const array = require('./100-data.js');
const newArray = array.list.map((element, index) => element * index);
console.log(array.list);
console.log(newArray);
