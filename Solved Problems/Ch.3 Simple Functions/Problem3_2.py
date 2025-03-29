# Problem from Starting Out With Python by Tony Gaddis
# Chapter 3: Simple Functions
#
# Problem 3.2:  Rewrite program 2.6, but this time using functions.
#
#
# Author: Giorgio Murad Murad

# Tax Amounts (Also declared as Global Variables)
STATE_TAX = 4 / 100
COUNTY_TAX = 2 / 100
TOTAL_TAX = STATE_TAX + COUNTY_TAX

# Prompting the user to input the purchase amount
purchase = float(input("Enter the purchase price: "))


# ----- DEFINING FUNCTIONS -----
#
# Function to display the state tax
def stateTax():
    tax = STATE_TAX * purchase
    print('State Tax: \t\t %3.2f \t $' % tax)

# Function to display the county tax
def countyTax():
    tax = COUNTY_TAX * purchase
    print('County Tax: \t %3.2f \t $' % tax)

# Function to display the total tax
def totalTax():
    tax = TOTAL_TAX * purchase
    print('Total Tax: \t\t %3.2f \t $' % tax)
    totalAmount(tax)

# Function to display the total amount
def totalAmount(value):
    total = purchase + value
    print('Total Amount: \t %3.2f \t $' % total)

# Function the displays the purchase amount, and calls all the other functions
def mainPurchase():
    print('Purchase Amount: %3.2f \t $' % purchase)
    stateTax()
    countyTax()
    totalTax()


# Calling the main function to display all the results
mainPurchase()