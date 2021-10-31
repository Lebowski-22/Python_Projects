"""
Day 6 - Exercise 2
by: Kenneth Castro

"""
print("Record Keeping Program")

mydict = dict({})#create an empty dictionary

while True:


    print("""What do you want to do?
[1] Add data
[2] Delete data
[3] Display data
[4] End """)


    code = input("Enter code [1-4]: ")

    if code == '1':
        addKey = input("Enter key : ")
        addValue = input("Enter value :")
        mydict[addKey] = addValue #put the inputted key and value in the dictionary
    elif code == '2':
        delete = input("Enter key to delete:")
        mydict.pop(delete)  #delete or pop the certain key
    elif code == '3':
        print(mydict) #print all keys and values of dictionary
    elif code == '4':
        print("Thank you") #terminate
        break


