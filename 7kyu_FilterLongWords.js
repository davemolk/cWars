/*
https://www.codewars.com/kata/5697fb83f41965761f000052

Write a function filter_long_words that takes a string sentence and an integer n.

Return a list of all words that are longer than n.

*/

function filterLongWords(sentence, n) {
  return sentence.split(' ').filter(word => word.length > n);
}
