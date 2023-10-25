#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
let characters = [];

request(url, (error, header, body) => {
  if (error) {
    console.log(error);
  } else {
    characters = JSON.parse(body).characters;
    const makeRequest = getMakeRequest();
    makeRequest(characters);
  }
});

function getMakeRequest () {
  let i = 0;

  return function makeRequest (characters) {
    request(characters[i], (error, header, body) => {
      if (error) {
        console.log(error);
      } else {
        console.log(JSON.parse(body).name);
        i++;
        if (i < characters.length) {
          makeRequest(characters);
        }
      }
    });
  };
}
