#!/usr/bin/env python
#dmoj = coci18c3p1

def magnus(letter):
    blockHONI = 0
    blockH = 0
    blockHO = 0
    blockHON = 0
    for char in letter:
        if char == 'H':
            blockH += 1
        elif blockH >= 1 and char == 'O':
            blockHO += 1
        elif blockHO >=1 and char == 'N':
            blockHON +=1
        elif blockHON >=1 and char == 'I':
            blockHONI +=1
            blockH = 0
            blockHO = 0
            blockHON = 0
    return blockHONI

print(
    magnus(input())
)