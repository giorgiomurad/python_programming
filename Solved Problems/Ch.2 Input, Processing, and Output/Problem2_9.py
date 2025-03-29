# Problem from Starting Out With Python by Tony Gaddis
# Chapter 2: Designing a Program
#
# Problem 2.9:  Write a program that converts a temperature in Celsius to
#               a temperature in Fahrenheit using the following formula:
#                       F = (9/5) * C + 32
#
#               The program should prompt the user to enter the temperature in
#               Celsius, and display the value of the temperature in Fahrenheit
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the value of the temperature in Celsius
celsius = float(input('Enter the temperature in Celsius: '))

# Calculating the temperature in Fahrenheit
fahrenheit = 9/5 * celsius + 32

# Displaying the result
print(f'The temperature in Fahrenheit is {fahrenheit}')