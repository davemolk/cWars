'''
https://www.codewars.com/kata/58279e13c983ca4a2a00002a

You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return an array where each object will have a new property 'greeting' with the following string value:

Hi < firstName here >, what do you like the most about < language here >?

'''

def greet_developers(lst):
    for dev in lst:
        dev["greeting"] = f"Hi {dev['firstName']}, what do you like the most about {dev['language']}?"
    return lst
