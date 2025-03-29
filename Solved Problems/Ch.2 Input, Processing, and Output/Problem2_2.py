# Problem from Starting Out With Python by Tony Gaddis
# Chapter 2: Designing a Program
#
# Problem 2.2:  A company has determined that its annual profit is typically 23 percent.
#               Write a program that asks the user to enter the projected amount of total
#               sales, and displays the profit that will be made from that amount.
#
#
# Author: Giorgio Murad Murad

# Initiating the percentage amount, and prompting the user to input the total sales
percentage = 23 / 100
totalSales = input('Enter the amount of total sales: $')

# Computing and displaying the annual profit
annualProfit = percentage * float(totalSales)
print('The annual profit is $' + str(annualProfit))