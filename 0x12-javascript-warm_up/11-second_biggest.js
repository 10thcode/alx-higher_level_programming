#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const secondBiggest = args.sort((a, b) => {
    return a - b;
  })[args.length - 2];
  console.log(Number(secondBiggest));
}
