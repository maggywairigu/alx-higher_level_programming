#!/usr/bin/node
const args = process.argv.slice(2);
let numberOfArgs = 0;
for (arg in args){
    numberOfArgs++;
}
if (numberOfArgs === 0) {
  console.log('No argument');
} else {
  console.log(args);
}
