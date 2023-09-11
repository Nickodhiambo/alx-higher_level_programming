#!/usr/bin/node

const process = require('process');
const arg = parseInt(process.argv[2]);

function compFactorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return (n * compFactorial(n - 1));
  }
}
if (!isNaN(arg)) {
  console.log(compFactorial(arg));
} else {
  console.log('1');
}
