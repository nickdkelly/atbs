#!/usr/bin/python3

def spam(divideBy): # the divideBy parameter is what the function is expecting to process when it runs
    try:
        return 42 / divideBy # this will be passed in when the spam function gets called
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2)) # here, we're passing in values to the spam function via the divideBy parameter
print(spam(12))
print(spam(0))
print(spam(1))