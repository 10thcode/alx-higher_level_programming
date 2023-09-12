#!/usr/bin/node

const firstArg = Number(process.argv[2]);

if (firstArg) {
  console.log('My number: ' + firstArg);
} else {
  console.log('Not a number');
}
