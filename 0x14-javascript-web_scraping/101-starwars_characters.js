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
      const characterPromises = movieData.characters.map((url) => {
        return new Promise((resolve) => {
          request.get(url, (error, response, body) => {
            if (error) {
              console.error(error);
              resolve(null);
            } else {
              const characterData = JSON.parse(body);
              resolve(characterData.name);
            }
          });
        });
      });

      Promise.all(characterPromises).then((characterName) => {
        characterName.forEach((name) => {
          if (name !== null) {
            console.log(name);
          }
        });
      }).catch((promiseError) => {
        console.error(promiseError);
      });
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
