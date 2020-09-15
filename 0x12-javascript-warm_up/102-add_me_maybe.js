#!/usr/bin/node
exports.addMeMaybe = function (number, thefunction) {
  return thefunction(number + 1);
};
