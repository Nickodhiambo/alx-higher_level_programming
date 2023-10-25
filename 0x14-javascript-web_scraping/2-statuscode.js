#!/usr/bin/node

// import the request module
const request = require('request');

// Fetch URL from command line
const url = process.argv[2];

// Make a GET request to the URL
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // If there are no errors during the request, print status code
    console.log('code:', response.statusCode);
  }
});
