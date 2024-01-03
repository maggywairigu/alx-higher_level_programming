#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const tasks = JSON.parse(body);
      const completedTasksCount = {};
      const completedTasks = tasks.filter((task) => task.completed);

      completedTasks.forEach((task) => {
        if (completedTasksCount[task.userId]) {
          completedTasksCount[task.userId]++;
        } else {
          completedTasksCount[task.userId] = 1;
        }
      });

      console.log(completedTasksCount);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
