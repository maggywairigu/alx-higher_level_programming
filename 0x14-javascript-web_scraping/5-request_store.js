#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      fs.writeFileSync(filePath, body, 'utf-8');
    } catch (writeError) {
      console.error(writeError);
    }
  }
});
