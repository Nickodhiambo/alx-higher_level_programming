#!/usr/bin/node

// Import the request module
const request = require('request');

// Extract episode ID from command line
const id = process.argv[2];

// API url
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

// Send a GET request to the url
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
