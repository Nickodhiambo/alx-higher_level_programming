#!/usr/bin/node

// Import the file system module, fs
const fs = require('fs');

// Extract the file path from command line
const file = process.argv[2];

// Read the file
fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.error('Error reading file:', error);
    return;
  }
  console.log(data);
});
