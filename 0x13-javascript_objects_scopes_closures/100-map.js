#!/usr/bin/node

const list = require('./100-data.js').list;
const newlist = list.map((x, idx) => x * idx);

console.log(list);
console.log(newlist);
