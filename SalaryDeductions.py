"""

Day 7 - Exercise 2
by: Kenneth Castro

"""

def salaryDeductions(tax, gross): #calculate the 12%tax and gross salary
    """

    :param tax: float
    :param gross: float
    :return:
    """
    return tax * gross

def totalDeduction(sss,philhealth,otherLoan,tax): #calculate the total deductions
    """

    :param sss: float
    :param philhealth: float
    :param otherLoan:float
    :param tax:float
    :return:
    """
    total = sss + philhealth + otherLoan + tax
    return total
