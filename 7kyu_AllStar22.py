'''
https://www.codewars.com/kata/5865cff66b5699883f0001aa/train/python

Create a function that takes an integer argument of seconds and converts the value into a string describing how many hours and minutes comprise that many seconds.

Any remaining seconds left over are ignored.

Note:
The string output needs to be in the specific form - "X hour(s) and X minute(s)"
'''

def to_time(seconds):
    hours = int(seconds / (60 * 60))  
    minutes = int(seconds / 60) - hours * 60
    return f"{hours} hour(s) and {minutes} minute(s)"
