# Problem from Starting Out With Python by Tony Gaddis
# Chapter 2: Designing a Program
#
# Problem 2.4:  A customer in a store is purchasing five items.
#               Write a program that asks for the price of each item, and displays the
#               subtotal, the amount of sales tax, and the total.
#               (Assume the sales tax is 6 percent)
#
#
# Author: Giorgio Murad Murad

# Declaring the sales tax
SALES_TAX = 6 / 100

# Prompting the user to enter the purchase amount of every item
item1 = float(input('Enter the price of item 1: '))
item2 = float(input('Enter the price of item 2: '))
item3 = float(input('Enter the price of item 3: '))
item4 = float(input('Enter the price of item 4: '))
item5 = float(input('Enter the price of item 5: '))

# Computing the total and the subtotal sales
total = item1 + item2 + item3 + item4 + item5
subtotal = total * SALES_TAX

# Printing the results
print()
print('Sales Tax: \t %5.2f \t'% SALES_TAX, end='%\n')
print('Subtotal: \t %5.2f \t$'% subtotal)
print('Total: \t\t %5.2f \t$'% total)