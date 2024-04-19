#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, { json: true }, (err, response, body) => {
  if (!err) {
    // Display each character name in the same order of the list "characters"
    const characterPromises = body.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, { json: true }, (err, response, body) => {
          if (!err) { resolve(body.name); }
        });
      });
    });
    Promise.all(characterPromises).then((characterNames) => {
      characterNames.forEach((characterName) => {
        console.log(characterName);
      });
    });
  }
});
