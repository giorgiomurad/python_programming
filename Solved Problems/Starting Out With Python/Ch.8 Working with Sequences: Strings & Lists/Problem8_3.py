# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.3:  Write a program that reads a string from the user containing a date in format mm/dd/yyyy.
#               The program should then print the same date, but in format [month] [day], [year].
#
#               For Example:    If the user enters 06/05/2022, the program should print June 5, 2022
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter a date in the format mm/dd/yyyy
date1 = input('Enter the date in format mm/dd/yyyy: ')

# Turning the date string into a list of string elements,
# and assigning every element value into a separate variable
date_list = date1.split('/')
month = int(date_list[0])
day = int(date_list[1])
year = int(date_list[2])

# Deducing the month
if month == 1:
    month = 'January'
elif month == 2:
    month = 'February'
elif month == 3:
    month = 'March'
elif month == 4:
    month = 'April'
elif month == 5:
    month = 'May'
elif month == 6:
    month = 'June'
elif month == 7:
    month = 'July'
elif month == 8:
    month = 'August'
elif month == 9:
    month = 'September'
elif month == 10:
    month = 'October'
elif month == 11:
    month = 'November'
elif month == 12:
    month = 'December'

# Printing the final result
print(f'The date is {month} {day}, {year}')