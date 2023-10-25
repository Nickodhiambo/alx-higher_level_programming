#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const dictionary = {};

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const contents = JSON.parse(body);
    contents.forEach(function (item) {
      if (item.completed === true) {
        const userid = item.userId;
        if (!(userid in dictionary)) {
          dictionary[userid] = 0;
        }
        dictionary[userid] += 1;
      }
    });
    console.log(dictionary);
  }
});
