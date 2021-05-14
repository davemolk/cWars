/*
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9


Collect|
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

*/

function findShort(s) {
  const arr = s.split(' '); 
  return arr.reduce((acc, n) => n.length < acc ? acc = n.length : acc, arr[0].length);
}
