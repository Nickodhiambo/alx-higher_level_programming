#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Extract url to scrap from command line
const url = process.argv[2];

// Extract file path to dump url contents
const file = process.argv[3];

// Make a GET request to url
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // Write response to a file
    fs.writeFile(file, body, 'utf-8', function (error, data) {
      if (error) {
        console.error(error);
      }
    });
  }
});
