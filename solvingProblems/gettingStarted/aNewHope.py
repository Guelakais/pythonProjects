#!/usr/bin/env python
#wc15c2j1

def aNewHope(dist):
    return f"A long time ago in a galaxy {'far, '*(dist-1)if(1 <= dist or dist >= 5)else 'not '}far away..." 

print(aNewHope(int(input())))