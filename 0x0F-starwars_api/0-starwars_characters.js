#!/usr/bin/node

const request = require('request');
const idMovi = process.argv.slice(2, 3);
const urlMovi = `https://swapi-api.hbtn.io/api/films/${idMovi}`;
const info = {
  url: urlMovi,
  method: 'GET'
};

request(info, async function (error, req, body) {
  if (error) {
    return console.log(error);
  }
  const char = JSON.parse(body).characters;
  for (const c in char) {
    await new Promise((resolve, reject) => {
      request(char[c], (error, req, body) => {
        if (error) {
          return console.log(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});