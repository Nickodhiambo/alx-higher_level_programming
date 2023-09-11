#!/usr/bin/node

const process = require('process');
const arg = parseInt(process.argv[2]);

if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
