#!/usr/bin/node

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
let content = '';
const fs = require('fs');

fs.readFile(fileA, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  content = `${content}${data}`;

  fs.readFile(fileB, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }

    content = `${content}${data}`;

    fs.writeFile(fileC, content, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
