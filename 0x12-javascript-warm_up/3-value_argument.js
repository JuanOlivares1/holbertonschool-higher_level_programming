#!/usr/bin/node
let output;

if (process.argv[2] !== undefined) {
  output = process.argv[2];
} else {
  output = 'No argument';
}
console.log(output);
