# Problem from Starting Out With Python by Tony Gaddis
# Chapter 7: Files & Exception
#
# Problem 7.8:  Write a program that takes a player's name and golf score as input, and
#               writes the taken data into a file called golf.txt.
#               The program should later read from the text file the player's name and score
#               from the file and display them in the console.
#
#               +: Allow the program to write and read more than only one player
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the number of players
nbOfPlayers = int(input('Enter the number of golf players: '))

# Opening a file called 'golf.txt'. If the file doesn't exist, then a new file called 'golf.txt' is created
writer = open('golf.txt', 'w')

# Loop
# Asking the user to enter every player's name and golf score, and writing them to the file
for i in range(nbOfPlayers):
    name = input('Enter the name of player {}: '.format(i + 1))
    score = input('Enter the score of player {}: '.format(i + 1))

    writer.write('{}\t{}\n'.format(name, score))

# Closing the file for writing
writer.close()


# Reopening the file, but for reading
reader = open('golf.txt', 'r')

# Reading and displaying data from the file line by line
for line in reader:
    print(line)

# Closing the file for reading
reader.close()