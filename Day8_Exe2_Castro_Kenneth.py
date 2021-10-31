"""

Day 8 - Exercise 2
by: Kenneth Castro

"""

name = input("Enter name: ")
mathGrade = int(input("Math Grade: "))
sciGrade = int(input("Science Grade: "))
engGrade = int(input("English Grade: "))


class Students:

    def __init__(self, name, mathGrade, sciGrade, engGrade ): # init method to instantiated / collect student info
        self.name = name
        self.mathGrade = mathGrade
        self.sciGrade = sciGrade
        self.engGrade = engGrade


    def __ave(self): #computed average method

        addGrade = (self.mathGrade, self.sciGrade, self.engGrade)
        average = sum(addGrade) // len(addGrade)
        return average

    def __passFailed(self): #to determine Passed or Failed method

        if self.__ave() >= 0 and self.__ave() < 74:
            return "Remarks: Failed"

        elif self.__ave() >= 75 and self.__ave() < 100:
            return "Remarks: Passed"

        else:
             return "Average must not be less than 0 or greater than 100"



    def result(self): # result method

        print(f"Name: {stud.name.title()}")
        print(f"Math Grade: {stud.mathGrade}")
        print(f"Science Grade: {stud.sciGrade}")
        print(f"English Grade: {stud.engGrade}")
        print(f"Average: {stud.__ave()}")
        print(stud.__passFailed())

print()
stud = Students(name, mathGrade, sciGrade, engGrade)
stud.result()













