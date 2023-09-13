#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
const a = parseInt(firstArg);
const secondArg = args[1];
const b = parseInt(secondArg);
function add (a, b) {
  console.log(a + b);
}
add(a, b);
