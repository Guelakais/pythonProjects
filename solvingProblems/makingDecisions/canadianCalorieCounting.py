#!/usr/bin/env python
#dmoj = ccc06j1

ordersTable = [
    [0,0,0,0,0],
    [
        0, #reference
        461, #Cheeseburger
        431, #Fishburger
        420, #VeggieBurger
        0, #nothing
    ],
    [
        0, #reference
        100, #Fries
        57, #Baked Potato
        70, #Chef Salad
        0, #nothing
    ],
    [
        0, #reference
        130, #Soft Drink
        160, #Orange Juice
        118, #Milk
        0, #nothing
    ],
    [
        0, #reference
        167, #Apple Pie
        266, #Sundae
        75, #Fruit Cup
        0, #nothing
    ]
]

def calorieCounting(burger, sideOrder, drink, dessert):
    return f"Your total Calorie count is {ordersTable[1][burger]+ordersTable[2][sideOrder]+ordersTable[3][drink]+ordersTable[4][dessert]}."

print(
    calorieCounting(
        int(input()), int(input()), int(input()), int(input())
        )
    )