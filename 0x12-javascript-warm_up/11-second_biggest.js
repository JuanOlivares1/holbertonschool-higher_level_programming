#!/usr/bin/node
const argv = process.argv.slice(2);
let max;

if (argv[1]) {
  max = argv.sort(function (a, b) { return b - a; })[0];
} else {
  max = '0';
}
console.log(max);
