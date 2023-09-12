#!/usr/bin/node

const firstArg = Number(process.argv[2]);
let i = firstArg;
let j;
let hashes;

if (firstArg) {
  while (i > 0) {
    j = 0;
    hashes = '';
    while (j < firstArg) {
      hashes += 'X';
      j++;
    }
    console.log(hashes);
    i--;
  }
} else {
  console.log('Missing size');
}
