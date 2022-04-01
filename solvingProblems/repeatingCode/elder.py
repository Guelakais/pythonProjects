#!/usr/bin/env python
#dmoj = coci18c4p1

def elder(owner, numBattle):
    all_owner=owner
    num_owners=0
    for i in range(num_battle):
        duel=str(input())
        if duel[2]==owner:
            owner=duel[0]
            all_owner=all_owner+owner
    distOwner = set(all_owner)
    return f'{owner}\n{len(distOwner)}'


print(
    elder(input(), int(input()))
)
