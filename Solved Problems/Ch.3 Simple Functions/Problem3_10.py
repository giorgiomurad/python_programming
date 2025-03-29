# Problem from Starting Out With Python by Tony Gaddis
# Chapter 3: Simple Functions
#
# Problem 3.10: A retail company must file a monthly sales tax report listing
#               the total sales for the month, and the amount of state and county
#               sales tax.
#               The state sales tax rate is four percent, and the county sales tax
#               rate is two percent.
#               Write a program that asks the user to enter the total sales for the
#               month, and displays the following:
#                       . The amount of county sales tax
#                       . The amount of state sales tax
#                       . The total amount of sales tax-
#
#
# Author: Giorgio Murad Murad

# Declaring the state and county sales tax rates
STATE_TAX = 4 / 100
COUNTY_TAX = 2 / 100
TOTAL_TAX = STATE_TAX + COUNTY_TAX

# Prompting the user to enter the monthly sale
monthlySales = float(input('Enter the monthly sale in dollars: '))


# Function to display the sales tax
def salesTax(sales, tax, status):
    temp = sales * tax
    print('The {} sales tax is ${t:.2f}'.format(status, t=temp))


# Displaying the sales taxes
salesTax(monthlySales, STATE_TAX, 'state')
salesTax(monthlySales, COUNTY_TAX, 'county')
salesTax(monthlySales, TOTAL_TAX, 'total')