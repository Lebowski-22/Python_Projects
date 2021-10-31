"""
Day 2 - Exercise 2
by: Kenneth Castro

"""

name = input("Enter text : ")
num = int(input("Enter number : "))

text1 = (name[-num:])
text2 = (name[:-num])

print(text1.upper() + text2)





