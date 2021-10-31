"""
Day 3 - Exercise 1
by: Kenneth Castro

"""


num1 = int(input("Enter 5 digit number: "))
string = str(num1)
print(f"Original: {num1}")
num2 = string[::-1]
print(f"New : {num2}")
if string == num2:
      print("It's a NUMERICAL PALINDROME")
else:
      print("It's not a NUMERICAL PALINDROME")

