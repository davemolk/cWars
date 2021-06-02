'''
https://www.codewars.com/kata/coding-meetup-number-3-higher-order-functions-series-is-ruby-coming

You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return:

true if at least one Ruby developer has signed up; or
false if there will be no Ruby developers.

'''
def is_ruby_coming(lst): 
    for dev in lst:
        if dev["language"] == "Ruby":
            return True
    return False    

  
'''
def is_ruby_coming(lst): 
    return any(dev["language"] == "Ruby" for dev in lst)
