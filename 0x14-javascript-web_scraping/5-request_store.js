#!/usr/bin/node

const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (error, header, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
