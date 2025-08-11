# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.11: Write program that asks the user to enter a series of 20 single-digit numbers, before
#               each and every number to a list.
#               The program should then display the following:
#                       . The lowest number in the list
#                       . The highest number in the list
#                       . The total sum of the numbers in the list
#                       . The average of the numbers in the list
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the series of numbers
series = input('Enter a series of 20 single-digit numbers:\n')

# Extracting each and every digit, and adding them to a list of integers
list = []
for number in series:
    list.append(int(number))

# Deducing the highest and lowest values from the list, and computing the total sum and the average
highest = max(list)
lowest = min(list)
total = sum(list)
average = total / len(list)

print()

# Displaying the final analysis
print('Numbers Analysis:')
print((
    '- The lowest number in the list: {l}\n'
    '- The highest number in the list: {h}\n'
    '- The total sum of the numbers in the list: {t}\n'
    '- The average of numbers in the list: {a:.2f}'
).format(
    l=lowest,
    h=highest,
    t=total,
    a=average
))