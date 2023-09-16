#!/usr/bin/node
const dict = require('./101-data.js');
const newDict = {};
for (const key in dict.dict) {
  const occurence = dict.dict[key];
  if (Object.prototype.hasOwnProperty.call(newDict, occurence)) {
    newDict[occurence].push(key);
  } else {
    newDict[occurence] = [key];
  }
}
console.log(newDict);
