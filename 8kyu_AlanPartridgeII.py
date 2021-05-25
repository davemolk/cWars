'''
https://www.codewars.com/kata/580a094553bd9ec5d800007d/train/python

Your job is simple, if (x) squared is more than 1000, return 'It's hotter than the sun!!', else, return 'Help yourself to a honeycomb Yorkie for the glovebox.'.

X will be a valid integer number.
X will be either a number or a string. Both are valid.

'''

def apple(x):
    return "It's hotter than the sun!!" if int(x)**2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."
