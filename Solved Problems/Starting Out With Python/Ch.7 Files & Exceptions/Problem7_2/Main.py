# Problem from Starting Out With Python by Tony Gaddis
# Chapter 7: Files & Exception
#
# Problem 7.2:  Write a program that asks the user for the name of the file.
#               The program should display only the first five lines of the file's contents.
#               If the file contains less than five lines, it should display the file's entire
#               content.
#
#
# Author: Giorgio Murad Murad

# Asking the user to enter the name of the external file to be read by the program
file = input('Enter the name of the file (with the extension eg. .txt):\n')

# Opening the external file for reading
f1 = open(file, 'r')

# Counting the number of lines in the file
count = 0
for line in f1:
    count += 1

# Closing the f1
f1.close()

# Reopening the same file with another reference
f2 = open(file, 'r')

# Checking if the file includes less than five lines
# If yes, all the content of the file is displayed
# Otherwise, only the first five lines are displayed
if count < 5:
    content = f2.read()
    print(content)
else:
    for i in range(5):
        line = f2.readline()
        print(line)


# Closing f2
f2.close()