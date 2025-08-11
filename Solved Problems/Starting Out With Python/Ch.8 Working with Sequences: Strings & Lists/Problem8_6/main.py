# Problem from Starting Out With Python by Tony Gaddis
# Chapter 8: Working with Sequences: Strings and Lists
#
# Problem 8.6:  Write a program that reads from an external text file and displays the average number of words in the
#               text file.
#
#
# Author: Giorgio Murad Murad
import re

# Opening the text file
file = open('text.txt', 'r')

# initializing the required list and variable for the program
wordsPerLine = []
nbOfWords = 0

# Reading from the file to deduce the average number of words per sentence
for line in file:
    nbOfWords = 0
    line = re.split(r'[ ,.\n]', line)

    for word in line:
        if len(word) > 0:
            nbOfWords += 1

    wordsPerLine.append(nbOfWords)

# Computing and displaying the average number of words per line
print('The average number of words per line is:', sum(wordsPerLine) / len(wordsPerLine))

# Closing the file
file.close()
