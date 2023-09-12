#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c) {
    if (c) {
      let row = '';

      for (let i = 0; i < this.width; i += 1) {
        row = `${row}${c}`;
      }

      for (let i = 0; i < this.width; i += 1) {
        console.log(row);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
