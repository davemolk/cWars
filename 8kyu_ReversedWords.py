'''
https://www.codewars.com/kata/51c8991dee245d7ddf00000e

Complete the solution so that it reverses all of the words within the string passed in.

'''
def reverse_words(s):
    words = s.split(' ')
    return ' '.join(reversed(words))
