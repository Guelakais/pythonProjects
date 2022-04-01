#!/usr/bin/env python
#wc17c1j2
def celsiusToFahrenheit(celsius):
    return celsius*(9/5)+32 if(
        -40 <= celsius and celsius <= 40
    ) else 'out of Range'

def fahrenheitToCelsius(Fahrenheit):
    return (5/9)*(Fahrenheit-32)

print(celsiusToFahrenheit(int(input())))