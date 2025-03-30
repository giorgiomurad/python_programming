# Problem from Starting Out With Python by Tony Gaddis
# Chapter 2: Designing a Program
#
# Problem 2.3:  One acre of land is equivalent to 43,500 square feet.
#               Write a program that asks the user to enter the total number of square
#               feet in a tract of land, and calculates the number of acres in the tract.
#
#
# Author: Giorgio Murad Murad

# Initializing the amount of acre of land,
# and prompting the user to input the tract of land in square feet
ACRE_OF_LAND = 43500
sqr_ft = input('Enter the total number of square feet in a tract of land: ')

# Computing and displaying the total acres of the land
landAcres = float(sqr_ft) / ACRE_OF_LAND
print('The land is made up of ', landAcres, ' acres')