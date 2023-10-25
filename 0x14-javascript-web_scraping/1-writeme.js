#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
const text = process.argv[3];

fs.writeFile(fileName, text, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
