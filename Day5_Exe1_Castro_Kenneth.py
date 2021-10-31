"""

Day 5 - Exercise 1
by: Kenneth Castro


"""


li = []

li = [int(item) for item in input("Enter the numbers : ").split()]
ave = sum(li)/len(li) #get the average
print(f"Average = {ave}")
li2 = sorted(i for i in li if i < ave)#get below average
print(f"Those numbers below the average {li2}")
li3 = sorted(i for i in li if i > ave)#get above average
print(f"Those numbers above the average {li3}")











