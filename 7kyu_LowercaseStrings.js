/*
https://www.codewars.com/kata/5729fa716c7d26dc84000040


Create a function to lowercase all strings in an array. Non-string items should remain unchanged.

*/

function arrayLowerCase(arr) {
  return arr.map((n) => (typeof n === 'string' ? n.toLowerCase() : n));
}
