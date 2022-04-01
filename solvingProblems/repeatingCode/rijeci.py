#!/usr/bin/env python
#dmoj = coci13c3p1

FibArray = [0, 1]
 
def fibonacci(n):
   
    if n <= 0:
        print("Incorrect input")

    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib

def arrayHolder(nana):
    fibonacci(nana+1)
    return f'{FibArray[nana-1]} {FibArray[nana]}' 

print(arrayHolder(int(input())))
