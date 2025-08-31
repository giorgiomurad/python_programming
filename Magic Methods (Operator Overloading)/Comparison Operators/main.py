from MyNumber import MyNumber

# Initializing MyNumber object with value
number = MyNumber(5)


# 1. __lt__()
number1 = MyNumber(5)
print("Number is less than Number 1:", number < number1, end="\n\n")

# 2. __le__()
number2 = MyNumber(5)
print("Number is less than or equal to Number 2:", number <= number2, end="\n\n")

# 3. __eq__()
number3 = MyNumber(5)
print("Number is equal to Number 3:", number == number3, end="\n\n")

# 4. __ne__()
number4 = MyNumber(8)
print("Number is not equal to Number 4:", number != number4, end="\n\n")

# 5. __gt__()
number5 = MyNumber(7)
print("Number is greater than Number 5:", number > number5, end="\n\n")

# 6. __ge__()
number6 = MyNumber(8)
print("Number is greater than or equal to Number 6:", number > number6, end="\n\n")