/*
https://www.codewars.com/kata/515dfd2f1db09667a0000003

Complete the keysAndValues function so that it takes in an object and returns the keys and values as separate arrays.
*/

function keysAndValues(data){
  return [[...Object.keys(data)], [...Object.values(data)]];
}
