#!/usr/bin/node
let output;

if (process.argv[3] !== undefined) {
  output = 'Arguments found';
} else if (process.argv[2] !== undefined) {
  output = 'Argument found';
} else {
  output = 'No argument';
}
console.log(output);
