#!/usr/bin/env python
#dmoj = dmopc16c1p0

def pizzaSatisfaction(width, cheese):
    return f'C.C. is {satisValid(width, cheese)} satisfied with her pizza.'

def satisValid(length, percent):
    return 'absolutely' if(
        length == 3 and percent >= 95
    ) else 'fairly' if(
        length == 1 and percent <= 50
    ) else 'very'

print(pizzaSatisfaction(int(input()),int(input())))