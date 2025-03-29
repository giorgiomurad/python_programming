# Problem from Starting Out With Python by Tony Gaddis
# Chapter 3: Simple Functions
#
# Problem 3.5:  A county collects property taxes on the assessment value of the
#               property, which is 60 percent of the property's actual value.
#               For example, if an acre of land is valued at $10,000, it's assessment
#               value is $6,000. The property tax is then 64 cents for every $100 of
#               the assessment value. So, the tax for the acre assessed at $6,000 will
#               be $38.40.
#               Write a program that asks for the actual value of a piece of property,
#               and displays the assessment value, and the property tax.
#
#
# Author: Giorgio Murad Murad

# Prompting the user to enter the actual value of a land
price = float(input("Enter the actual price of land: "))

# Function to display the land's assessment value, and property tax
def assess():
    assessment = price * 60 / 100
    propTax = (assessment / 100) * 0.64
    print('The assessment value is: \t $%3.2f'% assessment)
    print('The property tax is: \t\t $%3.2f'% propTax)

# Calling the function
assess()