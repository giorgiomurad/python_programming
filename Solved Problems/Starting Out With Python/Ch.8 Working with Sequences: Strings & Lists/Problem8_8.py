# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.8:  Write a program that asks the user to enter a store's sales for each day of the week.
#               The amounts should be stored in a list. Use a loop to calculate the total sales of
#               the week, and display the result.
#
#
# Author: Giorgio Murad Murad

# Initializing variables required for this program
weeklySales = []
totalSales = 0

# Initializing list of string containing the days of the week (Excluding Sunday)
weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Asking the user to enter the store's sales for each day of the week
# Adding the sale amount to the list of weekly sales, and added to the totalSales
for weekDay in weekDays:
    sale = float(input('How much did the store sell on {day}?\t'.format(day=weekDay)))
    weeklySales.append(sale)
    totalSales += sale

print()
print()
print()

# Displaying the sales amount for each day of the week
for i in range(len(weeklySales)):
    print('{day:<15}:\t${sale:>2.2f}'.format(day=weekDays[i], sale=weeklySales[i]))

# Finally, displaying the total sale amount after the whole week
print('Total Sale : ${sale:3.2f}'.format(sale=totalSales))