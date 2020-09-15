#!/usr/bin/node
const argv = process.argv.slice(2);
let max;

if (argv[1]) {
  argv.sort(function (a, b) { return Number(b) - Number(a); });
  max = argv[0];
} else {
  max = 0;
}
console.log(max);
