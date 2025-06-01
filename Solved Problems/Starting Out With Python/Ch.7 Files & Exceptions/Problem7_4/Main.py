# Problem from Starting Out With Python by Tony Gaddis
# Chapter 7: Files & Exception
#
# Problem 7.4:  Assume there's a file containing a series of names called names.txt.
#               Write a program that reads all the names from the file and displays how
#               many names are written in the file.
#               (Use a variable to keep a count of the number of names in the file)
#
#
# Author: Giorgio Murad Murad

# Opening the file of names
file = open('names.txt', 'r')

# Reading and counting the number of names
count = 0
for line in file:
    count += 1

# Displaying the number of names in the file
print('The file contains {n} names.'.format(n=count))

# Closing the file
file.close()