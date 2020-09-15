#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < Number(x); i++) { theFunction(); }
};
