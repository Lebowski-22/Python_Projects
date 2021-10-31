
"""

Day 7 - Exercise 1
by: Kenneth Castro

"""


def deposit(outstandingBalance,enterDeposit):   #function Deposit(the amount will be added to the outstanding balance

    totalDeposit = outstandingBalance + enterDeposit
    return totalDeposit


def withdraw(outstandingBalance, enterWithdraw):    #function Withdraw(the amount will be deducted from the outstanding balance)

    totalWithdraw = outstandingBalance - enterWithdraw
    return totalWithdraw


def inquire(outstandingBalance):    #function Inquire(display the outstanding balance)

    print(f"Your current balance is {outstandingBalance}")
    return outstandingBalance


def terminate():    #function to end the program
    exit("Thank you")


def pinChecker():   #function to check if the PIN number is correct or not

    print()
    pinNum = int(input("Enter PIN number: "))

    if pinNumber != pinNum:
        print("Invalid PIN number")
        return False
    else:
        return True


initialAmount = int(input("Enter initial amount: "))
pinNumber = int(input("Enter PIN number: "))

outstandingBalance = initialAmount

cont = True
while cont:
    print()
    print("""**** SELECT TRANSACTION ****
[1] Deposit
[2] Withdraw
[3] Inquire
[4] Exit """)

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if pinChecker():

            enterDeposit = int(input("Enter amount: "))
            print(f"You have successfully deposited an amount of {enterDeposit}")
            deposit(outstandingBalance, enterDeposit)
            outstandingBalance += enterDeposit

    elif choice == 2:

        if pinChecker():
            enterWithdraw = int(input("Enter amount to withdraw: "))
            if enterWithdraw > outstandingBalance:
                print("Withdrawal Denied! No enough balance.")
            else:
                withdraw(outstandingBalance, enterWithdraw)
                outstandingBalance -= enterWithdraw

    elif choice == 3:

        if pinChecker():
            inquire(outstandingBalance)

    elif choice == 4:

        terminate()

    else:
        print("Invalid input")
        cont = True





















