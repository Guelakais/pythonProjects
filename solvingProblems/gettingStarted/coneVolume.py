#!/usr/bin/env python
#dmopc14c5p1
PI = 3.141592653589793

def volume(radius, height):
    return(
        (
            PI * 
            radius**2 * 
            height
            )/3
        )

print(volume(int(input()), int(input())))
