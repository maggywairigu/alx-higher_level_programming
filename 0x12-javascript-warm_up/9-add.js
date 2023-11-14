#!/usr/bin/node
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
function add (a, b) {
  return a + b;
}
if (!Number.isNaN(num1) && !Number.isNaN(num2)) {
  const sum = add(num1, num2);
  console.log(sum);
} else {
  console.log('NaN');
}
