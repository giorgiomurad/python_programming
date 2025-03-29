# Problem from Starting Out With Python by Tony Gaddis
# Chapter 3: Simple Functions
#
# Problem 3.3:  Many financial experts advise that property owners should ensure
#               their homes or buildings for at least 80 percent of the amount it
#               would cost to replace the structure.
#               Write a program that asks the user to enter the replacement cost of
#               a building, and displays the minimum amount of insurance he or she
#               should buy for the property.
#
#
# Author: Giorgio Murad Murad

# Insurance Percentage
INSURANCE_PERCENTAGE = 0.8

#Prompting the user to enter the replacement cost of the property
replacementCost = float(input('Enter the replacement cost of the property: '))

# Defining the function the displays the minimum insurance amount
# based on the replacement cost
def propertyInsurance():
    insurance = INSURANCE_PERCENTAGE * replacementCost
    print(f'The minimum amount of property insurance is: ${insurance}')

# Calling the function to display the property insurance
propertyInsurance()