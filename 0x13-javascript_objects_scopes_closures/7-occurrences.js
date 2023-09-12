#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;

  for (let i = 0; i < list.length; i += 1) {
    if (list[i] === searchElement) {
      occurences += 1;
    }
  }

  return occurences;
};
