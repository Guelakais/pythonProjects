#!/usr/bin/env python
#dmoj = coci16c1p1

monthlyMb = int(input())
n = int(input())

excess = 0

for i in range(n):
    used = int(input())
    excess += monthlyMb - used

print(excess + monthlyMb)