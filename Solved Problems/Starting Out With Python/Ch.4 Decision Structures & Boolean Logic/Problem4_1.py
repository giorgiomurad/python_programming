# Problem from Starting Out With Python by Tony Gaddis
# Chapter 4: Decision Structures & Boolean Logic
#
# Problem 4.1:  Write a program that prompts the user to enter a number from one
#               to ten.
#               The program should then display the roman numeral version of that
#               number. If the inputted is not from one to ten, the program should
#               display an error message.
#
#
# Author: Giorgio Murad Murad

# Asking the user to enter a number from 1 to 10
number = int(input('Enter an integer from 1 to 10 to display it\'s roman numeral: '))

# Assigning the roman numeral to the roman variable according to the integer value
roman = ''
if number == 1:
    roman = 'I'
elif number == 2:
    roman = 'II'
elif number == 3:
    roman = 'III'
elif number == 4:
    roman = 'IV'
elif number == 5:
    roman = 'V'
elif number == 6:
    roman = 'VI'
elif number == 7:
    roman = 'VII'
elif number == 8:
    roman = 'VIII'
elif number == 9:
    roman = 'IX'
elif number == 10:
    roman = 'X'

# Printing the roman numeral if the integer value is valid.
# Otherwise, an error message is displayed
if len(roman) > 0:
    print('The roman numeral of the number is', roman)
else:
    print(
        'Invalid Number!'
        '\nEnter an integer from 1 to 10.'
    )