#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, header, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (error, header, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
