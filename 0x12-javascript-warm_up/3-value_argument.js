#!/usr/bin/node
const args = process.argv.slice(2);
const firstArg = args[0];
if (firstArg !== undefined) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
