"""
Day 3 - Exercise 2
by: Kenneth Castro

"""

num = int(input("Enter a book call number : "))

invalid = 99

if num > invalid:
    if num >= 100 and num <= 199: print("Basement")
    elif num >= 200 and num <= 500 or num > 900:print("Main Floor")
    elif num >= 501 and num <= 900 and not(num >= 700 and num <= 750):print("Upper Floor")
    else: print("Archives")
else:
    print("Invalid number")