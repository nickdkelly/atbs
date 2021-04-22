#!/usr/bin/python3

def stringer(stringList):
    if not stringList:
        print('List is empty')
    else:
        stringList.insert(-1, 'and ')
        for ele in stringList:
                print(ele, end='' + ' ')    
        print('\n') # fixes no trailing newline at end of string. was displaying a % shell prompt   

inputList = ['apples', 'pears', 'oranges', 'cats']
#inputList=[]
stringer(inputList)
