# Problem from Starting Out With Python by Tony Gaddis
# Chapter 3: Simple Functions
#
# Problem 3.9:  A painting company has determined that for every 115 square feet of
#               wall space, one gallon of paint and eight hours of labor will be required.
#               The company charges $20 per hour for labor.
#               Write a program that asks the user to enter the square feet of wall space
#               to be painted and the price of paint per gallon.
#               The program should display the following:
#                   . The number of gallons of paint required
#                   . The hours of labor required for completion
#                   . The cost of the paint
#                   . The labor charges
#                   . The total cost of the paint job
#
#
# Author: Giorgio Murad Murad
import math

# Declaring the company's hourly labor charge
# (Global Variable)
HOURLY_LABOR = 20

# Prompting the user to enter the square feet of wall space to be painted
# And the price of one gallon of paint
squareFeet = float(input('Enter the square feet of wall space to be painted: '))
gallonPrice = float(input('Enter the price of one gallon of paint: '))


# Function that takes the number of square feet wall space, and displays the
# number of gallons of paint and hours of labor required
def laborGallons(wallSpace, pricePerGallon):
    gallons = math.ceil(wallSpace / 115)
    hours = (wallSpace / 115) * 8
    print('The number of gallons required is', gallons, 'gallons.')
    print('The number of labor hours required is', hours, 'hours.')
    paintCost(gallons, hours, pricePerGallon)

# Function that displays the cost of paint and labor, and the total cost of the
# paint job
def paintCost(gallons, hours, pricePerGallon):
    paintPrice = int(gallons * pricePerGallon)
    laborCharge = hours * HOURLY_LABOR
    totalCost = paintPrice + laborCharge
    print('The total paint cost is ${}'.format(paintPrice))
    print('The total labor cost is ${lc:.2f}'.format(lc=laborCharge))
    print('The total total cost is ${tc:.2f}'.format(tc=totalCost))


# Calling the function to display the results
laborGallons(squareFeet, gallonPrice)