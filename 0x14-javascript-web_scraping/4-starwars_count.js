#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const wedgeAntillesId = 18;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const filmsData = JSON.parse(body);
      const filmsWithWedge = filmsData.results.filter((film) =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)
      );
      console.log(filmsWithWedge.length);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
