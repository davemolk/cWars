/*
https://www.codewars.com/kata/57a2013acf1fa5bfc4000921

Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.

*/

function find_average(array) {
  if (array.length === 0) return 0;
  return array.reduce((acc, n) => acc = acc + n, 0) / array.length;
}
