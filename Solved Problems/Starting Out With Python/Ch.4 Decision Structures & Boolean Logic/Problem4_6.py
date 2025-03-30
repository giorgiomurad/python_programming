# Problem from Starting Out With Python by Tony Gaddis
# Chapter 4: Decision Structures & Boolean Logic
#
# Problem 4.6:  The Fast Freight Shipping Company charges the following rates:
#                   -----------------------------------------------------------------------------
#                   |   Weight of Package                           ||      Rate Per Pound      |
#                   -----------------------------------------------------------------------------
#                   |   2 pounds or less                            ||          $1.10           |
#                   |   Over 2 pounds but not more than 6 pounds    ||          $2.20           |
#                   |   Over 6 pounds but not more than 10 pounds   ||          $3.70           |
#                   |   Over 10 pounds                              ||          $3.80           |
#                   -----------------------------------------------------------------------------
#
#               Write a program that asks the user to enter the package weight in pounds, and displays
#               the shipping charges.
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the package weight in pounds
weight = float(input("Enter the package weight in pounds: "))

# Calculating the shipping charge according to the package weight
if weight > 10:
    price = weight * 3.8
elif weight > 6:
    price = weight * 3.7
elif weight > 2:
    price = weight * 2.2
else:
    price = weight * 1.1

# Displaying the shipping charge
print("The shipping charge of the package is ${p:.2f}".format(p=price))