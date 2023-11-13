#!/usr/bin/node
const value = process.argv[2];
const myInt = parseInt(value);
const final = 'My number: ' + myInt;
if (!Number.isNaN(myInt)) {
  console.log(final);
} else {
  console.log('Not a number');
}
