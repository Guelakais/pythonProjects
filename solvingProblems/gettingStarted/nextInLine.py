#!/usr/bin/env python
#ccc13j1

def nextInLine(yungest, middle):
    return middle+middle-yungest if(
        (yungest <=50
        )and(0 <= yungest
        )and(yungest <= middle
        )and(middle <= 50
        ))else "false order"

print(nextInLine(int(input()), int(input())))