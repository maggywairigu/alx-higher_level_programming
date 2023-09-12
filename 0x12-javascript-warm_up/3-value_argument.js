#!/usr/bin/node
const args = process.argv.slice(2);
const numberOfArgs = args.length;
if (numberOfArgs === 0) {
  console.log('No argument');
} else {
  console.log(args);
}
