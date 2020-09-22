#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, data) {
  let counter = 0;
  if (error) {
    console.log(error);
  } else {
    for (const film of JSON.parse(data).results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          aux += 1;
        }
      }
    }
    console.log(aux);
  }
});
