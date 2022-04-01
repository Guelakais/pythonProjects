#!/usr/bin/env python
#wc18c3j1
def anHonestDaySWork(paint, bottleNeed, earnings):
    return paint//bottleNeed*earnings+paint%bottleNeed

print(anHonestDaySWork(int(input()), int(input()), int(input())))