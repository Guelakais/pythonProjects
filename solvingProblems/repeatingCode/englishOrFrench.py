#!/usr/bin/env python
#dmoj = ccc11s1

def tTsOrsSCounter(sequence):
    tTs= 0
    sS= 0
    for char in sequence:
        if char == 'T' or char == 't':
            tTs += 1
        elif char == 's' or char == 'S':
            sS += 1
    return tTs, sS

def englishOrFrench(konsonant1, konsonant2):
    return 'English' if(konsonant1 > konsonant2)else 'French'

def inputmanager(userinPut):
    tss, ss = tTsOrsSCounter(
        "".join(
            input() for i in range(userinPut)
            )
        )
    return englishOrFrench(tss, ss)
  
print(
    inputmanager(int(input()))
)