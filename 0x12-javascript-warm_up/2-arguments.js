#!/usr/bin/node

//a script that prints a message depending on the number of arguments passed.

const num = process.argv.length;
console.log(num === 2 ? 'No argument' : num === 3 ? 'Argument found' : 'Arguments found');
