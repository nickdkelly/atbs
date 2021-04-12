#! /usr/bin/python3

while True:
    print('Who are you?')
    name = input()
    if name != 'Nick':
        continue # continue makes the loop restart from the beginning. As in: it's continuing to loop.
    print('Hello, Nick. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break # remember, breaks take you out of the loop and back to the same indentation level as where the loop starts
print('Access Granted.')    