# Problem from Starting Out With Python by Tony Gaddis
# Chapter 7: Files & Exception
#
# Problem 7.1:  Assume that a file containing a series of integers is named numbers. txt and exists on the
#               computer's disk. Write a program that displays all of the numbers in the file.
#
#
# Author: Giorgio Murad Murad

file = open('numbers.txt', 'r')

x = file.read().split(' ')

for i in range(len(x)):
    print(x[i])