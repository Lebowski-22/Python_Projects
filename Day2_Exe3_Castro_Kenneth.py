"""
Day 2 - Exercise 3
by: Kenneth Castro

"""


import random


name = input("Enter your name: ")
betAmount = int(input("Enter bet amount: "))
luckyNumber = input("Enter your lucky numbers: ")

result1 = "----- draw\tresults -----"
print(result1.upper())
print(f"Name: {name.title()}")
print(f"Amount: {betAmount}")

rnd2 = random.randint(2, 5)

print(f"Multiplier x{rnd2}")
print(f"Prize: {betAmount * rnd2}")
print(f"Entry No's: {luckyNumber}")

result2 = "* d r a w\tr e s u l t *"
print(result2.upper())

for i in range(6):
    number = random.randint(1, 49)
    print(number, end=" ")
