#!/usr/bin/node
const square = Number(process.argv[2]);
if (!Number.isNaN(square)) {
  for (let i = 0; i < square; i++) {
    let row = '';
    for (let j = 0; j < square; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
