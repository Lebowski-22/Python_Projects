"""

Day 9 - Exercise 1
by: Kenneth Castro

"""
import os

cont = True
while cont:

    if os.path.exists('myTextFile.txt'):

        print("""
Record Keeping App
[1] Add Record
[2] View Record
[3] Clear all Records
[4] Exit """)

        code = int(input("Enter your choice: "))

        if code == 1:

            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")

            myFile = open('myTextFile.txt', 'a')
            myList = [name,email,address]
            myFile.writelines(' '.join(myList))
            myFile.close()

        elif code == 2:

            myFile = open('myTextFile.txt', 'r')
            content = myFile.read()
            print(content)
            myFile.close()

        elif code == 3:

            myFile = open('myTextFile.txt', 'w+')
            print("No more records found")
            myFile.close()

        elif code == 4:
            cont = False
            print("Thank you")

    else:
        myFile = open('myTextFile.txt', 'w')
        myFile.close()
