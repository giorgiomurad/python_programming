# Problem from Starting Out With Python by Tony Gaddis
# Chapter 2: Designing a Program
#
# Problem 2.10: Joe has purchased some stock in Acme Products Inc.
#               The details of his purchase are as follows:
#                   - The number of shares purchased are 1000
#                   - Joe purchased $32.87 per share
#                   - Joe paid his stockbroker a commission amounting
#                     to 2 percent of the amount he paid for the stock
#
#               Two weeks later, Joe sold the stock.
#               The details of his sale are as follows:
#                   - The number of sold shares are 1000
#                   - The stock was sold for $33.92 per share
#                   - He paid his stockbroker another commission
#                     amounting to 2 percent of the amount received
#
#
#               Write a program that displays the following information:
#                       * The amount Joe paid for the stock
#                       * The amount of commission paid when Joe bought the stock
#                       * The amount Joe sold the stock for
#                       * The amount of commission paid when Joe sold the stock
#                       * The amount left after selling the stock and paying the commission (both times)
#                         (If the amount left is positive, then Joe made a profit)
#
#
# Author: Giorgio Murad Murad

# Declaring variables on Joe's stock purchase
sharesPurchased = 1000
pricePerShare1 = 32.87
commission = 2 / 100

# Declaring variables on Joe's stock sale
sharesSold = 1000
pricePerShare2 = 33.92

# Computing the amount paid for the stocks and the commission,
# and the amount for the sale of stocks, and commission paid after the sale
amountPaid = sharesPurchased * pricePerShare1
commissionPaid1 = amountPaid * commission

amountEarned = sharesSold * pricePerShare2
commissionPaid2 = amountEarned * commission

# Computing the amount left after selling the stock, and paying the commission (both times)
amountLeft = amountEarned - (commissionPaid1 + commissionPaid2)

print((
    'Amount Paid: \t\t\t $ {paid: 3.2f}'
    '\nPurchase Commission: \t $ {pcommission: 3.2f}'
    '\nAmount Sold: \t\t\t $ {sold: 3.2f}'
    '\nSale Commission \t\t $ {scommission: 3.2f}'
    '\nAmount Left: \t\t\t $ {left: 3.2f}'
).format(
    paid=amountPaid, pcommission=commissionPaid1,
    sold=amountEarned, scommission=commissionPaid2,
    left=amountLeft
))