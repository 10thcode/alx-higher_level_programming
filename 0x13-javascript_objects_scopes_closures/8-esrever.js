#!/usr/bin/node

exports.esrever = function (list) {
  let temp;

  for (let i = 0; i < Math.floor(list.length / 2); i++) {
    temp = list[i];
    list[i] = list[list.length - (1 + i)];
    list[list.length - (1 + i)] = temp;
  }

  return list;
};
