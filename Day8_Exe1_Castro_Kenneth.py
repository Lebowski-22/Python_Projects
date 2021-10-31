"""

Day 8 - Exercise 1
by: Kenneth Castro

"""


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


cont = True
while cont:
    try:
        print()
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))

        print()
        print("""What operation do want to use?
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division """)

        print()
        code = int(input("Enter your choice: "))
        if code == 1:
            print(f"The sum of two numbers: {add(n1, n2)}")
            print()
        elif code == 2:
            print(f"The difference of two numbers: {subtract(n1, n2)}")
            print()
        elif code == 3:
            print(f"The product of two numbers: {multiply(n1,n2)}")
            print()
        elif code == 4:
            print(f"The quotient of two numbers: {divide(n1, n2)}")
            print()
        else:
            print("Enter valid choice!")



    except ValueError:
        print("Please input a number. ")

    except ZeroDivisionError:
        print("Cannot divide by 0. ")


    choice = input("Do you want to continue? [Y/N]: ")
    if choice == 'y' and 'Y':
        cont = True
    elif choice == 'n' and 'N':
        cont = False
    else:
        print("Enter [Y/N]")
        cont = False








