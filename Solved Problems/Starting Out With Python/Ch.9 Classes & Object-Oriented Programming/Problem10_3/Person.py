class Person:
    def __init__(self, name, address, age, phone):
        self.setName(name)
        self.setAddress(address)
        self.setAge(age)
        self.setPhone(phone)

    def setName(self, name):
        self.__name = name

    def setAddress(self, address):
        self.__address = address

    def setAge(self, age):
        self.__age = age

    def setPhone(self, phone):
        self.__phone = phone

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getAge(self):
        return self.__age

    def getPhone(self):
        return self.__phone