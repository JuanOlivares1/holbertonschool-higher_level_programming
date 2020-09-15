#!/usr/bin/node
const output = Number(process.argv[2]);
if (output) {
  console.log('My number: ' + output);
} else {
  console.log('Not a number');
}
