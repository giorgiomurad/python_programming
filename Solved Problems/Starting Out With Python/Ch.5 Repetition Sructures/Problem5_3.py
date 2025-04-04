# Problem from Starting Out With Python by Tony Gaddis
# Chapter 5: Repetition Structures
#
# Problem 5.3:  Write a program that asks the user for the amount he or she budgeted for a month.
#               A loop should then prompt the user to enter each of his or her expenses for the
#               month, and keep running a total. When the loop finishes, the program should display
#               the total amount, and if the user is over or under budget.
#
#
# Author: Giorgio Murad Murad

# Amount of total expenses
expenses = 0

# Prompting the user to enter the amount he or she budgeted for a month
budget = float(input("Enter your monthly budget: "))

# While Loop
nextExpense = True
count = 1
while nextExpense:
    expense = float(input('Enter the value of expense' + str(count) + ': '))
    expenses += expense

    choice = input('Continue adding expense values? (Y/N)')
    nextExpense = choice.upper() == 'Y'
    print()

# Displaying the final result
# The total amount of expenses, and if the user is over or under budget
print('Total Expense: %.2f'% expenses)
if expenses >= budget:
    under = expenses - budget
    print('You are %.2f'% under, 'dollars under budget.')
else:
    over = budget - expenses
    print('You are %.2f'% over, 'dollars over the budget.')