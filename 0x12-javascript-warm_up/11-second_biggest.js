#!/usr/bin/node

const process = require('process');
const myArray = (process.argv);
const count = process.argv.length - 2;

function findSecondLargest (array) {
  if (array.length < 4) {
    return 0;
  }
  let largest = array[2];
  let secondLargest = array[2];
  for (let i = 3; i < array.length; i++) {
    if (array[i] > largest) {
      secondLargest = largest;
      largest = array[i];
    } else if (array[i] > secondLargest && array[i] !== largest) {
      secondLargest = array[i];
    }
  }
  return secondLargest;
}

if (count === 0) {
  console.log('0');
} else if (count === 1) {
  console.log('0');
} else {
  console.log(findSecondLargest(myArray));
}
