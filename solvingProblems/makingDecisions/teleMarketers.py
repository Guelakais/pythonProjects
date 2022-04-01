#!/usr/bin/env python
#dmoj = ccc18j1

def teleMarketers(num1, num2, num3, num4):
    return 'ignore' if(
        (num1 == 8 or num1 == 9) and 
        (num4 == 8 or num4 ==9) and
        (num2 == num3)) else 'answer'

print(
    teleMarketers(
        int(input()),int(input()), int(input()), int(input())
            )
        )