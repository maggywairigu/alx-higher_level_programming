#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const num = parseInt(firstArg);
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
