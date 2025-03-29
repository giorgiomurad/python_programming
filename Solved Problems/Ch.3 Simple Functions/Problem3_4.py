# Problem from Starting Out With Python by Tony Gaddis
# Chapter 3: Simple Functions
#
# Problem 3.4:  Write a program that asks the user to enter the monthly costs for
#               the following expenses incurred from operating his or her automobile:
#               Loan payment, insurance, gas, oil, tires, and maintenance.
#               The program should then display the total monthly cost of these expenses.
#
#
# Author: Giorgio Murad Murad

# Function to gather monthly costs from the user, and displaying the total monthly cost
def monthlyCost():
    loan = float(input('Enter the monthly loan: '))
    insurance = float(input('Enter the monthly cost of insurance: '))
    gas = float(input('Enter the monthly cost of gas: '))
    oil = float(input('Enter the monthly cost of oil: '))
    tires = float(input('Enter the monthly cost of tires: '))
    maintenance = float(input('Enter the monthly cost of maintenance: '))
    totalCost = loan + insurance + gas + oil + tires + maintenance
    print('The total monthly cost of the automobile is $' + str(totalCost))

# Calling the defined function
monthlyCost()