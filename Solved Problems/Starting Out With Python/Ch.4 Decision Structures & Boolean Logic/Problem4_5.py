# Problem from Starting Out With Python by Tony Gaddis
# Chapter 4: Decision Structures & Boolean Logic
#
# Problem 4.5:  A software company sells a package that retails for $99.
#               Quantity discounts are given according to the following table:
#
#                   ---------------------------------
#                   |   Quantity    ||  Discount    |
#                   |   10 - 19     ||      20%     |
#                   |   20 - 49     ||      30%     |
#                   |   50 - 99     ||      40%     |
#                   |   100 or more ||      50%     |
#                   ---------------------------------
#
#               Write a program that asks the user for the quantity purchased,
#               and displays the amount of the discount, and the total amount
#               of purchase after the discount.
#
#
# Author: Giorgio Murad Murad

# Declaring the unit price
UNIT_PRICE = 99

# Prompting the user to enter the quantity purchased
qtyPurchased = int(input("Enter the quantity purchased: "))

# Finding the discount according to the quantity purchased
if qtyPurchased >= 100:
    discount = 50
elif qtyPurchased >= 50:
    discount = 40
elif qtyPurchased >= 20:
    discount = 30
elif qtyPurchased >= 10:
    discount = 20
else:
    discount = 0

# Calculating the price of the purchase
if discount > 0:
    price = (qtyPurchased * UNIT_PRICE) * (discount / 100)
else:
    price = qtyPurchased * UNIT_PRICE

# Displaying the quantity purchase, the discount, and the total price of the purchase
print(
    'Quantity Purchased: {q}'
    '\nDiscount: {d}%'
    '\nPurchase Price: ${p:.2f}'
    .format(q=qtyPurchased, d=discount, p=price)
)