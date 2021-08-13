#!/usr/bin/node
const ut = require('util');
const request = ut.promisify(require('request'));
const moviID = process.argv[2];

async function starWarsChar (moviId) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + moviId;
  let response = await (await request(endpoint)).body;
  response = JSON.parse(response);
  const char = response.characters;

  for (let i = 0; i < char.length; i++) {
    const urlChar = char[i];
    let char = await (await request(urlChar)).body;
    character = JSON.parse(char);
    console.log(char.name);
  }
}

starWarsChar(moviID);
