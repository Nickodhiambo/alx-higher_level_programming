#!/usr/bin/node

// Import the fs module
const fs = require('fs');

// Extract file path from command line
const file = process.argv[2];

// Extract file content from command line
const content = process.argv[3];

// Write contents into the file
fs.writeFile(file, content, 'utf-8', error => {
  if (error) {
    console.log(error);
  }
});
