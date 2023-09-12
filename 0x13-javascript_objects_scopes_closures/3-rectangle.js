#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';

    for (let i = 0; i < this.width; i += 1) {
      row = `${row}X`;
    }

    for (let i = 0; i < this.height; i += 1) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
