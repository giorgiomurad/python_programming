# Problem from Starting Out With Python by Tony Gaddis
# Chapter 2: Designing a Program
#
# Problem 2.6:  Write a program that will ask the user to enter the amount of the purchase.
#               The program should then display the purchase amount, the state sales tax,
#               the county sales tax, the total sales tax, and the total amount.
#               (Assume the state sales tax is 4 percent, and the county sales tax is 2 percent)
#
#
# Author: Giorgio Murad Murad

# Tax Amounts
STATE_TAX = 4 / 100
COUNTY_TAX = 2 / 100
TOTAL_TAX = STATE_TAX + COUNTY_TAX

# Prompting the user to input the purchase amount
purchase = float(input("Enter the purchase price: "))

# Computing the sales tax, county tax, total tax, total amount
stateTax = purchase * STATE_TAX
countyTax = purchase * COUNTY_TAX
totalTax = stateTax + countyTax
totalAmount = purchase + totalTax

# Displaying results
print('Purchase Amount: %3.2f \t $'% purchase)
print('State Tax: \t\t %3.2f \t $'% stateTax)
print('County Tax: \t %3.2f \t $'% countyTax)
print('Total Tax: \t\t %3.2f \t $'% totalTax)
print('Total Amount: \t %3.2f \t $' % totalAmount)