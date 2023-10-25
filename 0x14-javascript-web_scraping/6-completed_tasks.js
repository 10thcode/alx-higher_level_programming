#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (error, header, body) => {
  let data = [];

  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body);
  }

  const obj = {};

  for (let i = 0; i < data.length; i++) {
    if (data[i].completed) {
      if (obj[data[i].userId] === undefined) {
        obj[data[i].userId] = 1;
      } else {
        obj[data[i].userId] += 1;
      }
    }
  }

  console.log(obj);
});
