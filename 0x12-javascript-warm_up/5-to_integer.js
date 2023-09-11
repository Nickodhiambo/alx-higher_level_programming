#!/usr/bin/node

const process = require('process');
const arg = parseInt(process.argv[2]);

if (!isNaN(arg)) {
  console.log('My number:', arg);
} else {
  console.log('Not a number');
}
