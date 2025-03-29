# Problem from Starting Out With Python by Tony Gaddis
# Chapter 2: Designing a Program
#
# Problem 2.8:  Write a program that calculates the total amount of meal purchased
#               at a restaurant. The program should ask the user to enter the charge
#               for the food, and then calculate the amount of a 15 percent tip and
#               7 percent sales tax.
#               Display each of these amounts, and the total.
#
#
# Author: Giorgio Murad Murad

# Declaring the tip percentage and sales tax
TIP_PERCENTAGE = 15 / 100
SALES_TAX = 7 / 100

# Prompting the user to enter the price of the meal
mealPrice = float(input('Enter the price of the meal: '))

# Computing the tip and the sales tax according to the meal price
tip = mealPrice * TIP_PERCENTAGE
salesTax = mealPrice * SALES_TAX

# Displaying the results
print(
    'Meal Price: \t $ %5.2f'% mealPrice,
    '\nTip: \t\t\t $ %5.2f'% tip,
    '\nSales Tax: \t\t $ %5.2f'% salesTax,
)