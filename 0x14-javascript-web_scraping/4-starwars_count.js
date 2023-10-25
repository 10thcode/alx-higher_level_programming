#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (error, header, body) => {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    let characters = [];
    let numberOfFilms = 0;

    for (let i = 0; i < result.length; i++) {
      characters = result[i].characters;

      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes(18)) {
          numberOfFilms++;
        }
      }
    }

    console.log(numberOfFilms);
  }
});
