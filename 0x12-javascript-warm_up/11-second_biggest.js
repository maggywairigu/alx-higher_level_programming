#!/usr/bin/node
function findSecondLargest (numbers) {
  const sortedNumbers = numbers.sort((a, b) => b - a);

  if (sortedNumbers.length >= 2) {
    return sortedNumbers[1];
  } else {
    return 0;
  }
}
const args = process.argv.slice(2).map(Number);
const result = findSecondLargest(args);
console.log(result);
