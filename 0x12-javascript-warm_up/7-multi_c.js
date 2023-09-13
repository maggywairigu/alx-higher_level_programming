#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const num = parseInt(firstArg);
const str = 'C is fun';
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
