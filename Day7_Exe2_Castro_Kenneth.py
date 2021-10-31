"""

Day 7 - Exercise 2
by: Kenneth Castro

"""
#import modules
import GrossSalary as salary
import SalaryDeductions as deduct
import NetSalary as net

while True:
    def main():

        """

        :return: return value if True

        """

        empName = input("Employee Name: ")
        contactHrs = float(input("Enter number of hours: "))
        sss = float(input("SSS contributions: "))
        philhealthCont = float(input("Phil. health: "))
        otherLoan = float(input("Other loan: "))

        flatRate = 550
        tax = .12

        print("========== P A Y S L I P ==========")
        print()
        print("========== EMPLOYEE INFORMATION ==========")
        print(f"Employee Name: {empName.title()}")
        print(f"Rendered Hours: {contactHrs}")
        print(f"Rate per hour: {flatRate}")
        total = salary.grossSalary(contactHrs=contactHrs, flatRate=flatRate)
        print(f"Gross salary: {float(round(total,2))}")
        print()
        print("========== DEDUCTIONS ==========")
        print(f"SSS: {round(sss,2)}")
        print(f"PhilHealth: {round(philhealthCont,2)}")
        print(f"Other Loan: {round(otherLoan,2)}")
        totalTax = deduct.salaryDeductions(tax=tax,gross=total)
        print(f"Tax: {round(totalTax,2)}")
        totalDeduct = deduct.totalDeduction(sss=sss,philhealth=philhealthCont,otherLoan=otherLoan,tax=totalTax)
        print(f"Total Deductions: {round(totalDeduct,2)}")
        netSalary = net.netSalary(grossSalary=total, totalDeduct= totalDeduct)
        print()
        print(f"NET Salary: {float(round(netSalary, 2))}")
        print()
        code = input("Do you want to continue?[Y/N]: ")

        if code == 'y' and 'Y':
            return True
        elif code == 'n' and 'Y':
            exit()
        else:
            print("invalid input")
            exit()



    main()

