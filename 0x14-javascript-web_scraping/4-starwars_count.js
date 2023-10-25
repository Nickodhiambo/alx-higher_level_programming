#!/usr/bin/node

// Import the request module
const request = require('request');

// Api url
const url = process.argv[2];

// Make a GET request to the API
request(url, function (error, response, body) {
  if (!error) {
    const contents = JSON.parse(body).results;

    // Count the number of movies where Wedge Antilles is present
    const moviesWithWedge = contents.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1 // if found
        : count; // if not found
    }, 0); // Initialize count to zero
    console.log(moviesWithWedge);
  }
});
