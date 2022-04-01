#!/usr/bin/env python
#dmoj = ccc07j1

def whoIsInTheMiddle(first, second, third):
    return first if(
        validator(first, second, third)
    ) else second if(
        validator(second, first, third)
    ) else third

def validator(digit1, digit2, digit3):
    return (digit2 > digit1 and digit1 > digit3) or(digit3 > digit1 and digit1 > digit2)

print(whoIsInTheMiddle(int(input()),int(input()), int(input())))