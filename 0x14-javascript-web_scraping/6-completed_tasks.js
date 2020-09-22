#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (error, response, data) {
  if (error) {
    console.log(error);
  } else {
    const list = {};
    for (const task of JSON.parse(data)) {
      if (task.completed) {
        if (!list[task.userId]) {
          list[task.userId] = 1;
        } else {
          list[task.userId] += 1;
        }
      }
    }
    console.log(list);
  }
});
