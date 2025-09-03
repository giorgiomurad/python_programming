# Problem from Starting Out With Python by Tony Gaddis
# Chapter 10: Classes & Object-Oriented Programming
#
# Problem 10.5:     Write a class name RetailItem that holds data about an item in a retail store.
#                   The class should store the following data: item description, units in inventory, and price.
#
#                   Once you have written the class, write a program that creates three RetailItem objects with
#                   given information, and displays them:
#
#                               Description     Units       Price
#                   ----------------------------------------------
#                   Item #1     Jacket          12          59.95
#                   Item #2     Designer Jeans  40          34.95
#                   Item #3     Shirt           20          24.95
#
#
# Author: Giorgio Murad Murad
from RetailItem import RetailItem

# List to contain RetailItem objects
items = []

# Loop to gather item info from the user, initialize retail item objects,
# and store them in the item list
for i in range(1, 4):
    # Prompting the user to enter the retail item information
    print("Item #{}".format(i))
    description = input("Enter item description: ")
    units = int(input("Enter the number of items in the inventory: "))
    price = float(input("Enter the price per unit of the item: "))

    # Initializing a new RetailItem object, and adding this object to the list
    items.append(RetailItem(description, units, price))
    print()

# Loop to display information of every retail item
print(
            "{i:8s}\t{d:15s}\t{u:5s}\t{p:5s}"
            .format(i="", d="Description", u="Units", p="Price")
)
print("----------------------------------------------")
for i in range(0, len(items)):
    print("{i:8s}".format(i=f"Item #{i+1}"), end="\t")
    print(items[i])