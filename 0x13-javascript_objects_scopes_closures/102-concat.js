#!/usr/bin/node

const fs = require('fs');
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the content of the first source file
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    return;
  }

  // Read the content of the second source file
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      return;
    }

      fs.writeFile(destinationFile, 'utf8', (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(data1);
      console.log(data2);
    });
  });
});
