"""
Day 2 - Exercise 1
by: Kenneth Castro

"""


num = int(input("Enter positive integer : "))

firstDigit = int(num / 1000)
secDigit = int((num % 1000)/500)
thirdDigit = int(((num % 1000)%500)/100)
fourthDigit = int((((num % 1000)%500)%100)/50)
fifthDigit = int((((num % 1000)%500)%100)%50/20)
sixthDigit = int((((((num % 1000)%500)%100)%50)%20)/10)
seventhDigit = int(((((((num % 1000)%500)%100)%50)%20)%10)/5)
eighthDigit = int((((((((num % 1000)%500)%100)%50)%20)%10)%5)/1)



print(f"1000 - {firstDigit}")
print(f"500 - {secDigit}")
print(f"100 - {thirdDigit}")
print(f"50 - {fourthDigit}")
print(f"20 - {fifthDigit}")
print(f"10 - {sixthDigit}")
print(f"5 - {seventhDigit}")
print(f"1 - {eighthDigit}")





