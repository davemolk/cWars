/*
https://www.codewars.com/kata/54c27a33fb7da0db0100040e

Given an integral number, determine if it's a square number:

*/

const isSquare = function(n){
  return (Number.isInteger(Math.sqrt(n)))
}

/*
const isSquare = function(n){
  if (n < 0) return false
  return (Number.isInteger(Math.sqrt(n)))
}
*/
