#!/usr/bin/node

const firstArg = Number(process.argv[2]);

function factorial (x) {
  if (x) {
    return x * factorial(x - 1);
  } else {
    return 1;
  }
}

console.log(factorial(firstArg));
