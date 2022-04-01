#!/usr/bin/env python
#dmoj = ccc15j1

def aboutFebruary18(month, day):
    return 'Before' if(
        (month < 2) or
        (month == 2 and day < 18)
    ) else 'After' if(
        (month > 2) or 
        (month == 2 and day > 18)
    ) else 'Special'

print(
    aboutFebruary18(
        int(input()), int(input())
    )
)