#!/usr/bin/python3
import random

spam = random.randint(1, 3)

if spam == 1:
    print('Hello' + str(spam))
elif spam == 2:
    print('Howdy' + str(spam))
elif spam == 3:
    print('Greetings!' + str(spam))  