#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movieData = JSON.parse(body);
      movieData.characters.forEach((url) => {
        request.get(url, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      });
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
