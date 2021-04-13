#!/usr/bin/python3

import random
# remember, when an argument is defined as part of the function, a value is required when the function gets called.
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask me again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1,9) # generates random number from 1-9
fortune = getAnswer(r) # passes random number from r variable into getAnswer
print(fortune) # prints results of fortune

# print(getAnswer(random.randint(1,9))) <--- cleaner implementation of results