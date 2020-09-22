#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (_erro, response, data) {
  console.log(JSON.parse(data).title);
});
