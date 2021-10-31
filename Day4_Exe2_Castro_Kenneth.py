"""
Day 4 - Exercise 2
by: Kenneth Castro

"""
while True:
    num = int(input("Enter a number: "))
    sum = 0

    for ctr in range(1, num+1):
        print(ctr, end=' ')
        sum += ctr
    print(f"\nThe sum from {1} to {num} is {sum} ")

    again = input("Try Again?[Y/N]: ")
    if again == 'y' or again == 'Y':
        pass
    elif again == 'n' or again == 'N':
        print("Thank you")
        break
    else:
        print("Please enter [Y/N]")
        break


