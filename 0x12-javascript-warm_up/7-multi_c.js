#!/usr/bin/node
const occurences = Number(process.argv[2]);
if (!Number.isNaN(occurences)) {
  let i;
  for (i = 0; i < occurences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
