from MyNumber import MyNumber

# Initializing MyInteger object with value
number = MyNumber(5)


# 1. __add__()
number1 = MyNumber(2)
add = number + number1
print("The sum is", add.value, end="\n\n")

# 2. __sub__()
number2 = MyNumber(3)
sub = number - number2
print("The difference is", sub.value, end="\n\n")

# 3. __mul__()
number3 = MyNumber(2)
mul = number * number3
print("The multiplication is", mul.value, end="\n\n")

# 4. __truediv__()
number4 = MyNumber(4)
div = number / number4
print("The division is", div.value, end="\n\n")

# 5. __floordiv__()
number5 = MyNumber(4)
floor = number // number5
print("The floor division is", floor.value, end="\n\n")

# 6. __mod__()
number6 = MyNumber(6)
mod = number % number6
print("The remainder is", mod.value, end="\n\n")

# 7. __pow__()
number7 = MyNumber(3)
power = number ** number7
print("The power is", power.value, end="\n\n")