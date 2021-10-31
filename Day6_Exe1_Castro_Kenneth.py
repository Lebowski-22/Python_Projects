"""
Day 6 - Exercise 1
by: Kenneth Castro

"""

import random


num1 = [int(item) for item in input("Enter first number : ")]
num2 = [int(item) for item in input("Enter second number : ")]

mySet1 = set(num1)
mySet2 = set(num2)

#Set A
for i in range(0,9):
    mySet1.add(random.randint(0,9))
print(f"Set A : {mySet1}") #print random numbers in set A ranging from 0 to 9
#Set B
for i in range(0, 9):
    mySet2.add(random.randint(0, 9))
print(f"Set B : {mySet2}") #print random numbers in set B ranging from 0 to 9
print()

while True:

    print("""--CHOOSE OPERATION--
[1] Union 
[2] Intersection 
[3] Difference 
[4] Symmetric Difference 
[5] Exit """)

    choice = input("Enter your choice: ")

    if choice == '1':
        unionOperator = mySet1.union(mySet2)
        print(f"Union Result : {unionOperator}") #print union result
        print()
    elif choice == '2':
        intersecOperator = mySet1.intersection(mySet2)
        print(f"Intersection Result : {intersecOperator}")#print intersection result
        print()
    elif choice == '3':
        diffOperator = mySet1.difference(mySet2)
        print(f"Difference Result : {diffOperator}")#print difference result
        print()
    elif choice == '4':
        symmetricOperator = mySet1.symmetric_difference(mySet2)
        print(f"Symmetric Difference Result : {symmetricOperator}") #print symmetric difference result
        print()
    elif choice == '5':
        print("Thank you")
        break

