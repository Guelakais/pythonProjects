#!/usr/bin/env python
#dmoj = wc17c3j3

def uncrackable(password):
    return 'Invalid' if(
        len(password)<8 or
         len(password)>12 or
         passwordLoop(password) == False
        ) else 'Valid'

def passwordLoop(sequence):
    upperChar = 0
    lowerChar = 0
    digit = 0
    for elem in sequence:
        if elem.isupper() == True:
            upperChar += 1
        elif elem.islower() == True:
            lowerChar +=1
        elif elem.isdigit() == True:
            digit += 1
    return True if(
            (
                upperChar >= 2
            )and(
                lowerChar >= 3
            )and(
                digit >=1
            )
        )else False


print(
    uncrackable(input())
)