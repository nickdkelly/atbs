#!/usr/bin/python3

# This exercise stumped me a bit, I couldn't get it to loop down correctly. My program kept returning number / 2 forever. This answer helped me understand, and its this code that I used.
#https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

import sys

def collatz(number):
    try:
        if number % 2 == 0:
            print(number // 2)
            return number // 2

        
        else:    
            result = 3 * number + 1
            print(result)
            return result
        
    except KeyboardInterrupt:
        sys.exit()    

n = input('Enter a number: ')
while n != 1:
    n = collatz(int(n))