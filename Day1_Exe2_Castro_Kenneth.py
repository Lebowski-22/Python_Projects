"""
Day 1 - Exercise 2
by: Kenneth Castro

"""

water1, water2 = input('Water Charge : ').split(' ')
sewage1, sewage2 = input('Sewage Charge: ').split(' ')
electric1, electric2 = input('Electric Charge : ').split(' ')
citytax1, citytax2 = input('City Tax : ').split(' ')

peso = "peso(s)"
cents = "cent(s)"

print("{:<20}{:^20}{:>20}".format(
    "Water Charge", water1 + " " + peso, water2 + " " + cents))
print("{:<20}{:^20}{:>20}".format(
    "Sewage Charge", sewage1 + " " + peso, sewage2 + " " + cents))
print("{:<20}{:^20}{:>20}".format(
    "Electric Charge", electric1 + " " + peso, electric2 + " " + cents))
print("{:<20}{:^20}{:>20}".format(
    "City Tax", citytax1 + " " + peso, citytax2 + " " + cents))
