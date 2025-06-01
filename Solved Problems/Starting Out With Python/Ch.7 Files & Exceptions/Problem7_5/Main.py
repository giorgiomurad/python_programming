# Problem from Starting Out With Python by Tony Gaddis
# Chapter 7: Files & Exception
#
# Problem 7.5:  Assume there's a file containing a series of numbers called numbers.txt.
#               Write a program that reads all the numbers, and displays their sum.
#
#
# Author: Giorgio Murad Murad

# Opening the text file containing the numbers
file = open('numbers.txt', 'r')

# Reading and placing the numbers in a list
numbers = file.read()
numbers = numbers.replace('\n', ' ')
numbers = numbers.split(' ')

# Computing the total sum
sum = 0
for number in numbers:
    sum += int(number)

# Displaying the sum
print('The sum of all the integers is', sum)

# Closing the file
file.close()