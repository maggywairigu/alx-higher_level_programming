#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = Array.from(args).map(Number);
function findSecondLargest (numbers) {
  if (numbers.length <= 1) {
    return 0;
  } else {
    const sortedNumbers = numbers.sort((a, b) => b - a);
    return sortedNumbers[1];
  }
}
const result = findSecondLargest(numbers);
console.log(result);
