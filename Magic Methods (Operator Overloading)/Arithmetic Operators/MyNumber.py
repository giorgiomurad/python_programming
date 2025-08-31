class MyNumber:
    # Constructor initializing object with given value
    def __init__(self, value):
        self.value = value

    # 1. Function that returns MyNumber object carrying the additional value of this number and the given number
    def __add__(self, other):
        return MyNumber(self.value + other.value)

    # 2. Function that returns MyNumber object carrying the subtraction value
    def __sub__(self, other):
        return MyNumber(self.value - other.value)

    # 3. Function that returns MyNumber object carrying the multiplication value
    def __mul__(self, other):
        return MyNumber(self.value * other.value)

    # 4. Function that returns MyNumber object carrying the division value
    def __truediv__(self, other):
        return MyNumber(self.value / other.value)

    # 5. Function that returns MyNumber object carrying the floor division value
    def __floordiv__(self, other):
        return MyNumber(self.value // other.value)

    # 6. Function that returns MyNumber object carrying the radian value
    def __mod__(self, other):
        return MyNumber(self.value % other.value)

    # 7. Function that returns MyNumber object carrying this integer to the power of the other integer
    def __pow__(self, other):
        return MyNumber(self.value ** other.value)