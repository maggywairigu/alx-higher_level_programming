#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const num = parseInt(firstArg);
const result = 'My number: ' + num;
if (!isNaN(num)) {
  console.log(result);
} else {
  console.log('Not a number');
}
