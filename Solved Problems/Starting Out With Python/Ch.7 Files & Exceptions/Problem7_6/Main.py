# Problem from Starting Out With Python by Tony Gaddis
# Chapter 7: Files & Exception
#
# Problem 7.6:  Assume there's a file containing a series of numbers called numbers.txt.
#               Write a program that reads all the numbers, and displays their average.
#
#
# Author: Giorgio Murad Murad

# Opening the text file containing the numbers
file = open('numbers.txt', 'r')

# Reading and placing the numbers in a list
numbers = file.read()
numbers = numbers.replace('\n', ' ')
numbers = numbers.split(' ')

# Retrieving the total number of numbers, and computing the total sum
sum = 0
count = 0
for number in numbers:
    sum += int(number)
    count += 1

# Computing the average
avg = sum / count

# Displaying the average
print('The average of all the numbers is', avg)

# Closing the file
file.close()