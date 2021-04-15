#!/usr/bin/python3

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('No pets named ' + name + ' were found.')
else:
    print(name + ' is my pet.')