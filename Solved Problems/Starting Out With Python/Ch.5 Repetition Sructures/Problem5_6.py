# Problem from Starting Out With Python by Tony Gaddis
# Chapter 5: Repetition Structures
#
# Problem 5.6:  Write a program that displays a table converting a temperature value in Celsius
#               to a temperature value in Fahrenheit.
#               The following formula to convert Celsius to Fahrenheit is as follows:
#                       F = 9/5 C + 32
#
#               The program should display the values from 0 to 20 degrees Celsius.
#
#
# Author: Giorgio Murad Murad

# Displaying the table using a for-loop
print('Celsius \t | \t Fahrenheit')
for c in range(21):
    f = 9/5 * c + 32
    print('{dc:2d}\t\t\t | \t {df:2.2f}'.format(dc=c, df=f))