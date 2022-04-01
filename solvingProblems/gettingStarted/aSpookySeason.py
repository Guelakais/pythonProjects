#!/usr/bin/env python
#wc16c1j1
def spookySeason(spooky):
    return f'sp{"o"*spooky}ky' if spooky >= 2 else 'not spooky enough'

print(spookySeason(int(input())))