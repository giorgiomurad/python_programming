class RetailItem:
    # Initializer that initializes the retail item
    def __init__(self, description, units, price):
        self.setDescription(description)
        self.setUnits(units)
        self.setPrice(price)

    # Function that sets the item description
    def setDescription(self, description):
        self.__description = description

    # Function that sets the number of item
    def setUnits(self, units):
        self.__units = units

    # Function that sets the price per unit
    def setPrice(self, price):
        self.__price = price

    # Function that return the item description
    def getDescription(self):
        return self.__description

    # Function that returns the number of units
    def getUnits(self):
        return self.__units

    # Function that returns the price per unit
    def getPrice(self):
        return self.__price

    # Function that returns the item information
    def __str__(self):
        return (
            "{d:15s}\t{u:5d}\t$ {p:5.2f}"
            .format(d=self.__description, u=self.__units, p=self.__price)
        )