#!/usr/bin/python3

import random
messages = ['It is certain', 'It is decidedly so', 'Yes definitely', 'Reply hazy try again', 'Ask again later', 'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very doubtful']

print(messages[random.randint(0, len(messages) -1 )]) # produces a random number which is passed to the list named 'messages', and returns the index of the list, plus the value of that indexes