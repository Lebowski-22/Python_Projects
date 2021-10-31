"""

Day 5 - Exercise 2
by: Kenneth Castro


"""

while True:

    li = [int(item) for item in input("Enter a digit : ").split()]
    myTuple = tuple(li)

    for tu in range(0, 10):
        print(tu, end=' ')
        output = ''
        for i in range(myTuple.count(tu)):
            output += '*'
        print(output)


    again = input("Try Again?[Y/N]: ")

    if again == 'y' or again == 'Y':
        pass
    elif again == 'n' or again == 'N':
        print("Thank you")
        break
    else:
        print("Please enter [Y/N]")
        break



