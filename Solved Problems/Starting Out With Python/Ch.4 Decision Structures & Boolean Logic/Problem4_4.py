# Problem from Starting Out With Python by Tony Gaddis
# Chapter 4: Decision Structures & Boolean Logic
#
# Problem 4.4:  Serendipity Booksellers has a book club that awards points to
#               its customers based on the number of books purchased each month.
#               The points are awarded as follows:
#                   . If the customer purchases 0 books, he/she earns 0 points
#                   . If the customer purchases 1 book, he/she earns 5 points
#                   . If the customer purchases 2 books, he/she earns 15 points
#                   . If the customer purchases 3 books, he/she earns 30 points
#                   . If the customer purchases 4 books, he/she earns 60 points
#
#               Write a program that asks the user to enter the number of books
#               purchased this month, and displays the number of points earned-
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the number of books purchased
books = int(input('Enter the number of books purchased: '))

# Deducing the number of points awarded according to the number of books purchased
points = 0
if books == 1:
    points = 5
elif books == 2:
    points = 15
elif books == 3:
    points = 30
elif books >= 4:
    points = 60

# Displaying the number of points earned
if points > 0:
    print('For purchasing', books, 'books, you were awarded', points, 'points.')
elif points == 0:
    print('No books were purchased, so no points were awarded.')
else:
    print('Invalid Inputted Number. Please try again.')