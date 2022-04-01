#!/usr/bin/env python
#dmoj = ccc19j1

def winningTeam(appleThreePoint, appleTwoPoint, appleOnePoint,\
    BananaThreePoint, BananaTwoPoint, BananaOnePoint):
    return 'A' if(
        calcer(appleThreePoint, appleTwoPoint, appleOnePoint) >
        calcer(BananaThreePoint, BananaTwoPoint, BananaOnePoint)
        )else 'B' if(
            calcer(appleThreePoint, appleTwoPoint, appleOnePoint) <
            calcer(BananaThreePoint, BananaTwoPoint, BananaOnePoint)
        ) else 'T'

def calcer(threePoint, twoPoint, onePoint):
    return 3*threePoint+2*twoPoint+onePoint

print(
    winningTeam(
        int(input()), int(input()), int(input()),int(input()), int(input()), int(input())
        )
    )