#!/usr/bin/node

const process = require('process');
const firstNo = parseInt(process.argv[2]);
const secondNo = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(firstNo, secondNo));
