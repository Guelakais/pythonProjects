#!/usr/bin/env python
#dmoj = ccc11s2


def multipleChoice(nLines):
    
    response = inputhelper(nLines)
    answer = inputhelper(nLines)
    answercounter = sum(
        1 if(
            response[k] == answer[k]
            )else 0 for k in range(nLines)  
    )
    return answercounter

def inputhelper(lines):
    return "".join(input() for i in range(lines))

print(
    multipleChoice(int(input()))
    )